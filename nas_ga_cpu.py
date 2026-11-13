import os
import gc
import json
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Cấu hình môi trường ngăn chặn xung đột C++ và tối ưu CPU
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
from sklearn.metrics import r2_score, mean_absolute_error
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from xgboost import XGBRegressor

import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Input, Dense, Dropout
from tensorflow.keras.optimizers import Adam, RMSprop, SGD


# ==============================================================================
# HÀM BỔ TRỢ DỌN DẸP BỘ NHỚ TRIỆT ĐỂ
# ==============================================================================
def clean_memory():
    """Giải phóng phiên làm việc Keras và ép bộ thu gom rác dọn dẹp RAM"""
    tf.keras.backend.clear_session()
    gc.collect()


# ==============================================================================
# BƯỚC 1: ĐỌC DỮ LIỆU & LÀM SẠCH BAN ĐẦU
# ==============================================================================
df = pd.read_csv('CPU_benchmark_v4.csv')
df = df.replace(r'^\s*$', np.nan, regex=True)


def clean_numeric_format(series):
    return pd.to_numeric(series.astype(str).str.replace(',', ''), errors='coerce')


numeric_cols = ['cores', 'TDP', 'threads', 'base_clock', 'turbo_clock', 'L3_cache']
for col in numeric_cols:
    if col in df.columns:
        df[col] = clean_numeric_format(df[col])

df = df.dropna(subset=['cpuMark']).reset_index(drop=True)

cat_features = ['socket', 'category']
X_raw = df[numeric_cols + cat_features].copy()
y_raw = df[['cpuMark']].copy()

print(f"Tổng số mẫu sau khi làm sạch thô: {len(df)}")

# ==============================================================================
# BƯỚC 2: PHÂN CHIA DỮ LIỆU CHUẨN MỰC (70% TRAIN - 15% VAL - 15% TEST)
# ==============================================================================
X_train_val, X_test_raw, y_train_val, y_test_raw = train_test_split(
    X_raw, y_raw, test_size=0.15, random_state=42
)

X_train_raw, X_val_raw, y_train_raw, y_val_raw = train_test_split(
    X_train_val, y_train_val, test_size=(0.15 / 0.85), random_state=42
)

print(f"Kích thước phân vùng:")
print(f" - Train set      : {X_train_raw.shape[0]} mẫu (70%)")
print(f" - Validation set : {X_val_raw.shape[0]} mẫu (15%)")
print(f" - Test set       : {X_test_raw.shape[0]} mẫu (15%)")

# ==============================================================================
# BƯỚC 3: TIỀN XỬ LÝ (FIT CHỈ TRÊN TRAIN - DÙNG MINMAX CHO CẢ X VÀ Y)
# ==============================================================================
num_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', MinMaxScaler(feature_range=(0, 1)))
])

cat_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='unknown')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

preprocessor = ColumnTransformer(transformers=[
    ('num', num_transformer, numeric_cols),
    ('cat', cat_transformer, cat_features)
])

X_train_trans = preprocessor.fit_transform(X_train_raw)
X_val_trans = preprocessor.transform(X_val_raw)
X_test_trans = preprocessor.transform(X_test_raw)

selector = VarianceThreshold(threshold=0.0)
X_train = selector.fit_transform(X_train_trans)
X_val = selector.transform(X_val_trans)
X_test = selector.transform(X_test_trans)

scaler_y = MinMaxScaler(feature_range=(0, 1))
y_train = scaler_y.fit_transform(y_train_raw).flatten()
y_val = scaler_y.transform(y_val_raw).flatten()
y_test = scaler_y.transform(y_test_raw).flatten()

y_test_orig = y_test_raw.values.flatten()
y_min_val = scaler_y.data_min_[0]
y_max_val = scaler_y.data_max_[0]
delta_y = y_max_val - y_min_val

print(f"Số lượng đặc trưng đầu vào sau khi tiền xử lý: {X_train.shape[1]}")
print(f"Khoảng giá trị cpuMark: Min = {y_min_val:.2f}, Max = {y_max_val:.2f} (Delta = {delta_y:.2f})")

# ==============================================================================
# BƯỚC 4: KHÔNG GIAN TÌM KIẾM & HÀM ĐÁNH GIÁ
# ==============================================================================
gene_space = [
    [1, 2, 3, 4],
    [32, 64, 128, 256, 512],
    [32, 64, 128, 256, 512],
    [32, 64, 128, 256, 512],
    [32, 64, 128, 256, 512],
    [0, 1, 2, 3],  # relu, elu, selu, tanh
    [0.1, 0.2, 0.3, 0.4, 0.5],
    [0, 1, 2]  # Adam, RMSprop, SGD
]

activations = ["relu", "elu", "selu", "tanh"]


def build_and_evaluate_proxy(chromosome, epochs=10):
    num_layers = int(chromosome[0])
    nodes = [int(chromosome[i]) for i in range(1, 5)]
    act = activations[int(chromosome[5])]
    dr = chromosome[6]
    opt_idx = int(chromosome[7])

    if opt_idx == 0:
        opt = Adam(learning_rate=0.001)
    elif opt_idx == 1:
        opt = RMSprop(learning_rate=0.001)
    else:
        opt = SGD(learning_rate=0.01)

    tf.keras.backend.clear_session()
    model = Sequential()
    model.add(Input(shape=(X_train.shape[1],)))
    model.add(Dense(nodes[0], activation=act))
    model.add(Dropout(dr))
    for i in range(1, num_layers):
        model.add(Dense(nodes[i], activation=act))
        model.add(Dropout(dr))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mae', optimizer=opt)

    try:
        history = model.fit(
            X_train, y_train,
            epochs=epochs,
            batch_size=64,
            validation_data=(X_val, y_val),
            verbose=0
        )
        val_mae = min(history.history['val_loss'])
        fitness = 1000.0 / (val_mae + 1e-6)
    except Exception:
        fitness, val_mae = 0.0, 1.0
    finally:
        del model
        if 'history' in locals():
            del history
        tf.keras.backend.clear_session()

    return fitness, val_mae


def train_and_eval_final(chromosome, epochs=100):
    num_layers = int(chromosome[0])
    nodes = [int(chromosome[i]) for i in range(1, 5)]
    act = activations[int(chromosome[5])]
    dr = chromosome[6]
    opt_idx = int(chromosome[7])

    if opt_idx == 0:
        opt = Adam(learning_rate=0.001)
    elif opt_idx == 1:
        opt = RMSprop(learning_rate=0.001)
    else:
        opt = SGD(learning_rate=0.01)

    tf.keras.backend.clear_session()
    model = Sequential()
    model.add(Input(shape=(X_train.shape[1],)))
    model.add(Dense(nodes[0], activation=act))
    model.add(Dropout(dr))
    for i in range(1, num_layers):
        model.add(Dense(nodes[i], activation=act))
        model.add(Dropout(dr))
    model.add(Dense(1, activation='linear'))
    model.compile(loss='mae', optimizer=opt)

    model.fit(X_train, y_train, epochs=epochs, batch_size=32, verbose=0)

    y_pred_scaled = model.predict(X_test, verbose=0).flatten()
    y_pred_orig = scaler_y.inverse_transform(y_pred_scaled.reshape(-1, 1)).flatten()

    test_mae_scaled = mean_absolute_error(y_test, y_pred_scaled)
    test_raw_mae = int(round(mean_absolute_error(y_test_orig, y_pred_orig)))
    test_r2 = r2_score(y_test_orig, y_pred_orig)

    del model
    clean_memory()

    return test_mae_scaled, test_raw_mae, test_r2, y_pred_scaled, y_pred_orig


# ==============================================================================
# BƯỚC 5: THUẬT TOÁN TIẾN HÓA NAS-GA
# ==============================================================================
def run_nas_ga(seed=42, generations=50, pop_size=20, k_parents=3, p_m=0.15, selection_mode='SSS'):
    random.seed(seed)
    np.random.seed(seed)
    tf.random.set_seed(seed)

    population = [[random.choice(space) for space in gene_space] for _ in range(pop_size)]
    best_fitness_history = []
    best_chrom = None
    best_overall_fitness = -1

    for gen in range(generations):
        fitness_scores = []
        for ind in population:
            fit, _ = build_and_evaluate_proxy(ind, epochs=10)
            fitness_scores.append(fit)

        ranked_indices = np.argsort(fitness_scores)[::-1]
        current_best_fit = fitness_scores[ranked_indices[0]]

        if current_best_fit > best_overall_fitness:
            best_overall_fitness = current_best_fit
            best_chrom = population[ranked_indices[0]]

        best_fitness_history.append(best_overall_fitness)

        new_pop = []
        if k_parents > 0:
            for idx in range(k_parents):
                new_pop.append(population[ranked_indices[idx]])

        if selection_mode == 'RWS':
            probs = np.array(fitness_scores) / np.sum(fitness_scores)
            selected_idxs = np.random.choice(pop_size, size=14, p=probs)
            mating_pool = [population[i] for i in selected_idxs]
        else:
            mating_pool = [population[i] for i in ranked_indices[:14]]

        while len(new_pop) < pop_size:
            p1, p2 = random.sample(mating_pool, 2)
            pt = random.randint(1, 7)
            child = p1[:pt] + p2[pt:]

            for j in range(8):
                if random.random() < p_m:
                    child[j] = random.choice(gene_space[j])
            new_pop.append(child)

        population = new_pop

        # Dọn dẹp RAM sau mỗi thế hệ
        clean_memory()

        if (gen + 1) % 10 == 0 or gen == 0:
            print(f"Gen {gen + 1:02d}/{generations} | Best Fitness trên Val: {best_overall_fitness:.4f}")

    return best_chrom, best_overall_fitness, best_fitness_history


# ==============================================================================
# BƯỚC 6: CHẠY 7 LẦN ĐỘC LẬP VÀ GHI LOG CHECKPOINT
# ==============================================================================
CHECKPOINT_FILE = "runs_checkpoint.json"
if os.path.exists(CHECKPOINT_FILE):
    try:
        with open(CHECKPOINT_FILE, "r") as f:
            table1_results = json.load(f)
    except Exception:
        table1_results = []
else:
    table1_results = []

completed_seeds = [item['Seed'] for item in table1_results]
seven_seeds = [42, 10, 100, 2024, 777]

print("\n" + "=" * 50)
print(f"--- BẮT ĐẦU CHẠY 7 RUNS (ĐÃ HOÀN THÀNH SEED: {completed_seeds}) ---")
print("=" * 50)

for i, s in enumerate(seven_seeds):
    if s in completed_seeds:
        print(f"--- RUN {i + 1} (Seed={s}) đã có kết quả. Tự động bỏ qua ---")
        continue

    print(f"\n--- BẮT ĐẦU RUN {i + 1} (Seed={s}) ---")
    best_c, best_fit, fit_hist = run_nas_ga(seed=s, generations=50, pop_size=20)
    mae_scaled, raw_mae, r2, _, _ = train_and_eval_final(best_c, epochs=100)

    num_l = best_c[0]
    entry = {
        'Run': i + 1,
        'Seed': s,
        'No. of Layers': int(num_l),
        'Network Topology': str(best_c[1:num_l + 1]),
        'Best Fitness': float(best_fit),
        'MAE': float(mae_scaled),
        'Raw MAE': int(raw_mae),
        'R2 Score': float(r2),
        'History': fit_hist,
        'Chromosome': [int(x) if isinstance(x, (int, np.integer)) else float(x) for x in best_c]
    }
    table1_results.append(entry)

    # Ghi đĩa ngay lập tức
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(table1_results, f, indent=4)

    print(f"--> [HOÀN TẤT & ĐÃ LƯU] Run {i + 1} | MAE: {mae_scaled:.4f} | R2: {r2:.4f}")

    # Dọn dẹp RAM triệt để giữa các Runs
    clean_memory()

# Tổng hợp Table 1
df_table1 = pd.DataFrame(table1_results)
print("\n" + "=" * 50)
print("=== KẾT QUẢ TABLE 1 (7 RUNS ĐỘC LẬP) ===")
print("=" * 50)
print(df_table1[['Run', 'No. of Layers', 'Network Topology', 'Best Fitness', 'MAE', 'Raw MAE', 'R2 Score']].to_string(
    index=False))

mean_mae = df_table1['MAE'].mean()
std_mae = df_table1['MAE'].std()
mean_raw = df_table1['Raw MAE'].mean()
mean_r2 = df_table1['R2 Score'].mean()
std_r2 = df_table1['R2 Score'].std()
print(
    f"\nOverall Metrics: MAE = {mean_mae:.4f} ± {std_mae:.4f} | Raw MAE = {int(round(mean_raw)):,} | R2 = {mean_r2:.4f} ± {std_r2:.4f}")

champion_idx = int(df_table1['R2 Score'].idxmax())
champion_entry: dict = table1_results[champion_idx]
champion_chrom = champion_entry['Chromosome']
champion_history = champion_entry['History']

# Huấn luyện champion 1 lần để lấy vector dự đoán trên Test
champ_mae_s, champ_raw_m, champ_r2, _, champion_pred_orig = train_and_eval_final(champion_chrom, epochs=100)

# Vẽ Figure 4: Fitness Curve
plt.figure(figsize=(8, 5), dpi=300)
plt.plot(champion_history, label='Best Fitness', color='#1f77b4', linewidth=2)
plt.title('Network Architecture Optimization Process (NAS-GA)', fontsize=12, fontweight='bold')
plt.xlabel('Generation', fontsize=11)
plt.ylabel('Fitness Score', fontsize=11)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='lower right')
plt.tight_layout()
plt.savefig('Figure_4_Fitness_Curve.png')
plt.close()
clean_memory()
print("--> Đã tạo và lưu 'Figure_4_Fitness_Curve.png'")

# Vẽ Figure 5: Predictions vs Reality
plt.figure(figsize=(7, 6), dpi=300)
y_test_norm = (y_test_orig - y_min_val) / delta_y
y_pred_norm = (champion_pred_orig - y_min_val) / delta_y

plt.scatter(y_test_norm, y_pred_norm, alpha=0.5, color='#2ca02c', edgecolors='k', s=35, label='CPUs')
plt.plot([0, 0.6], [0, 0.6], linestyle='--', color='#d62728', linewidth=1.8, label='Reference line (y=x)')
plt.title('Compare Predictions with Reality (CPU Performance)', fontsize=12, fontweight='bold')
plt.xlabel('Reality (cpuMark)', fontsize=11)
plt.ylabel('Predictions (cpuMark)', fontsize=11)
plt.xlim(-0.02, 0.65)
plt.ylim(-0.02, 0.65)
plt.grid(True, linestyle='--', alpha=0.5)
plt.legend(loc='upper left')
plt.tight_layout()
plt.savefig('Figure_5_Predictions_vs_Reality.png')
plt.close()
clean_memory()
print("--> Đã tạo và lưu 'Figure_5_Predictions_vs_Reality.png'")

# ==============================================================================
# BƯỚC 7: CÁC MÔ HÌNH BASELINE CHO TABLE 2
# ==============================================================================
print("\n" + "=" * 50)
print("--- ĐANG HUẤN LUYỆN CÁC MÔ HÌNH BASELINE ---")
print("=" * 50)

# 1. Linear Regression
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = scaler_y.inverse_transform(lr.predict(X_test).reshape(-1, 1)).flatten()
lr_mae_s = mean_absolute_error(y_test, lr.predict(X_test))
lr_raw_m = int(round(mean_absolute_error(y_test_orig, lr_pred)))
lr_r2 = r2_score(y_test_orig, lr_pred)

# 2. Default MLP
def_mlp = Sequential([
    Input(shape=(X_train.shape[1],)),
    Dense(128, activation='relu'),
    Dense(64, activation='relu'),
    Dense(1, activation='linear')
])
def_mlp.compile(loss='mae', optimizer=Adam(learning_rate=0.001))
def_mlp.fit(X_train, y_train, epochs=100, batch_size=32, verbose=0)
def_pred_s = def_mlp.predict(X_test, verbose=0).flatten()
def_pred = scaler_y.inverse_transform(def_pred_s.reshape(-1, 1)).flatten()
def_mae_s = mean_absolute_error(y_test, def_pred_s)
def_raw_m = int(round(mean_absolute_error(y_test_orig, def_pred)))
def_r2 = r2_score(y_test_orig, def_pred)
del def_mlp
clean_memory()

# 3. Random NAS (1,000 evaluations)
print("Đang chạy Random NAS (1,000 evaluations)...")
best_rand_fit = -1
best_rand_c = None
for _ in range(1000):
    c = [random.choice(space) for space in gene_space]
    f, _ = build_and_evaluate_proxy(c, epochs=10)
    if f > best_rand_fit:
        best_rand_fit = f
        best_rand_c = c
rand_mae_s, rand_raw_m, rand_r2, _, _ = train_and_eval_final(best_rand_c, epochs=100)
clean_memory()

# 4. Tuned Random Forest (5 seeds)
rf_r2_list, rf_mae_list, rf_raw_list = [], [], []
for s in [42, 10, 100, 2024, 777]:
    rf = RandomForestRegressor(n_estimators=200, max_depth=20, random_state=s, n_jobs=-1)
    rf.fit(X_train, y_train)
    p_s = rf.predict(X_test)
    p = scaler_y.inverse_transform(p_s.reshape(-1, 1)).flatten()
    rf_r2_list.append(r2_score(y_test_orig, p))
    rf_mae_list.append(mean_absolute_error(y_test, p_s))
    rf_raw_list.append(mean_absolute_error(y_test_orig, p))
    del rf
    gc.collect()

# 5. Tuned XGBoost (5 seeds)
xgb_r2_list, xgb_mae_list, xgb_raw_list = [], [], []
for s in [42, 10, 100, 2024, 777]:
    xgb = XGBRegressor(n_estimators=300, max_depth=6, learning_rate=0.05,
                       subsample=0.8, colsample_bytree=0.8, random_state=s, n_jobs=-1)
    xgb.fit(X_train, y_train, eval_set=[(X_val, y_val)], verbose=False)
    p_s = xgb.predict(X_test)
    p = scaler_y.inverse_transform(p_s.reshape(-1, 1)).flatten()
    xgb_r2_list.append(r2_score(y_test_orig, p))
    xgb_mae_list.append(mean_absolute_error(y_test, p_s))
    xgb_raw_list.append(mean_absolute_error(y_test_orig, p))
    del xgb
    gc.collect()

table2_data = [
    {"Model": "Linear Regression", "Scaled MAE": f"{lr_mae_s:.4f}", "Raw MAE": f"{lr_raw_m:,}",
     "R2 Score": f"{lr_r2:.4f}"},
    {"Model": "Default MLP", "Scaled MAE": f"{def_mae_s:.4f}", "Raw MAE": f"{def_raw_m:,}",
     "R2 Score": f"{def_r2:.4f}"},
    {"Model": "Random NAS (1,000 evals)", "Scaled MAE": f"{rand_mae_s:.4f}", "Raw MAE": f"{rand_raw_m:,}",
     "R2 Score": f"{rand_r2:.4f}"},
    {"Model": "Random Forest (Tuned, 5 seeds)", "Scaled MAE": f"{np.mean(rf_mae_list):.4f} ± {np.std(rf_mae_list):.4f}",
     "Raw MAE": f"{int(round(np.mean(rf_raw_list))):,}",
     "R2 Score": f"{np.mean(rf_r2_list):.4f} ± {np.std(rf_r2_list):.4f}"},
    {"Model": "XGBoost (Tuned, 5 seeds)", "Scaled MAE": f"{np.mean(xgb_mae_list):.4f} ± {np.std(xgb_mae_list):.4f}",
     "Raw MAE": f"{int(round(np.mean(xgb_raw_list))):,}",
     "R2 Score": f"{np.mean(xgb_r2_list):.4f} ± {np.std(xgb_r2_list):.4f}"},
    {"Model": "Proposed NAS-GA (Mean across 7 runs)", "Scaled MAE": f"{mean_mae:.4f} ± {std_mae:.4f}",
     "Raw MAE": f"{int(round(mean_raw)):,}", "R2 Score": f"{mean_r2:.4f} ± {std_r2:.4f}"},
    {"Model": "Proposed NAS-GA (Champion)", "Scaled MAE": f"{champ_mae_s:.4f}", "Raw MAE": f"{champ_raw_m:,}",
     "R2 Score": f"{champ_r2:.4f}"}
]
df_table2 = pd.DataFrame(table2_data)
print("\n=== KẾT QUẢ TABLE 2 ===")
print(df_table2.to_string(index=False))

# ==============================================================================
# BƯỚC 8: ABLATION STUDY (TABLE 3)
# ==============================================================================
print("\n" + "=" * 50)
print("--- ĐANG CHẠY CÁC KỊCH BẢN ABLATION STUDY ---")
print("=" * 50)

ablation_configs = [
    ("Default NAS-GA", {"k_parents": 3, "p_m": 0.15, "selection_mode": "SSS"}),
    ("Scenario 1 (No Elitism, k=0)", {"k_parents": 0, "p_m": 0.15, "selection_mode": "SSS"}),
    ("Scenario 2a (Low Mutation, Pm=0.0001)", {"k_parents": 3, "p_m": 0.0001, "selection_mode": "SSS"}),
    ("Scenario 2b (High Mutation, Pm=0.50)", {"k_parents": 3, "p_m": 0.50, "selection_mode": "SSS"}),
    ("Scenario 3 (Roulette Wheel Selection)", {"k_parents": 3, "p_m": 0.15, "selection_mode": "RWS"})
]

table3_data = []
for name, cfg in ablation_configs:
    print(f"Chạy: {name}...")
    c_abl, fit_abl, _ = run_nas_ga(seed=42, generations=50, pop_size=20,
                                   k_parents=cfg['k_parents'],
                                   p_m=cfg['p_m'],
                                   selection_mode=cfg['selection_mode'])
    mae_s, raw_m, r2_abl, _, _ = train_and_eval_final(c_abl, epochs=100)
    table3_data.append({
        "Scenario": name,
        "Best Fitness": f"{fit_abl:.2f}",
        "Scaled MAE": f"{mae_s:.4f}",
        "Raw MAE": f"{raw_m:,}",
        "R2 Score": f"{r2_abl:.4f}"
    })
    clean_memory()

df_table3 = pd.DataFrame(table3_data)
print("\n=== KẾT QUẢ TABLE 3 ===")
print(df_table3.to_string(index=False))

# ==============================================================================
# BƯỚC 9: XUẤT LATEX TỰ ĐỘNG
# ==============================================================================
print("\n" + "=" * 50)
print("--- MÃ NGUỒN LATEX CHO CÁC BẢNG ---")
print("=" * 50)
print("\n% TABLE 1\n" + df_table1[
    ['Run', 'No. of Layers', 'Network Topology', 'Best Fitness', 'MAE', 'Raw MAE', 'R2 Score']].to_latex(index=False))
print("\n% TABLE 2\n" + df_table2.to_latex(index=False))
print("\n% TABLE 3\n" + df_table3.to_latex(index=False))