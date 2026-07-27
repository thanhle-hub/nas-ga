import matplotlib
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, OneHotEncoder, MinMaxScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.feature_selection import VarianceThreshold
import pygad
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam, RMSprop, SGD
from sklearn.metrics import r2_score
import matplotlib.pyplot as plt


# ==========================================
# BƯỚC 1: ĐỌC VÀ LÀM SẠCH THÔ
# ==========================================
df = pd.read_csv('CPU_benchmark_v4.csv')
df = df.replace(r'^\s*$', np.nan, regex=True)

def clean_numeric_format(column_name):
    return pd.to_numeric(df[column_name].astype(str).str.replace(',', ''), errors='coerce')

# Chỉ làm sạch các cột số thực sự cần thiết trong danh sách của Thành (Đã bỏ powerPerf)
numeric_cols_to_clean = ['cores', 'TDP', 'threads', 'base_clock', 'turbo_clock', 'L3_cache']
for col in numeric_cols_to_clean:
    if col in df.columns:
        df[col] = clean_numeric_format(col)

# Loại bỏ dòng không có target (cpuMark)
df = df.dropna(subset=['cpuMark']).reset_index(drop=True)

# ==========================================
# BƯỚC 2: PHÂN TÁCH ĐẶC TRƯNG (ĐÃ BỎ POWERPERF)
# ==========================================
# Chỉ có duy nhất TDP là đặc trưng số có khả năng bị khuyết (NaN)
num_features_with_nan = ['TDP']

# Các đặc trưng số mới thêm vào đều sạch 100%
num_features_clean = ['cores', 'threads', 'base_clock', 'turbo_clock', 'L3_cache']

# Các đặc trưng phân loại
cat_features = ['socket', 'category']

# Gom các đặc trưng đầu vào X và nhãn mục tiêu y
X = df[num_features_clean + num_features_with_nan + cat_features]
y = df['cpuMark'].values.reshape(-1, 1)

# ==========================================
# BƯỚC 3: PIPELINE TỰ ĐỘNG TỐI ƯU GỌN NHẸ (ĐÃ SỬA LỖI NaN)
# ==========================================

# Nhánh 1: Chỉ áp dụng Imputer + Scaler cho duy nhất cột 'TDP'
num_nan_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='median')),
    ('scaler', StandardScaler())
])

# Nhánh 2: Các cột số đã sạch -> Đi thẳng vào Scaler
num_clean_transformer = StandardScaler()

# Nhánh 3: Nhánh xử lý chuỗi chữ (Mã hóa One-Hot)
categorical_transformer = Pipeline(steps=[
    ('imputer', SimpleImputer(strategy='constant', fill_value='unknown')),
    ('onehot', OneHotEncoder(handle_unknown='ignore', sparse_output=False))
])

# Gộp các nhánh xử lý bằng ColumnTransformer
ct = ColumnTransformer(
    transformers=[
        ('num_nan', num_nan_transformer, num_features_with_nan),
        ('num_clean', num_clean_transformer, num_features_clean),
        ('cat', categorical_transformer, cat_features)
    ]
)

# Chuyển đổi toàn bộ Pipeline thành chuỗi tích hợp màng lọc an toàn cuối cùng
preprocessor = Pipeline(steps=[
    ('ct', ct),
    ('selector', VarianceThreshold()), # Loại bỏ các cột hằng số sau khi mã hóa
    ('final_imputer', SimpleImputer(strategy='median')) # <--- MÀNG LỌC GIA CỐ: Triệt tiêu mọi NaN phát sinh ngoài ý muốn
])

# ==========================================
# BƯỚC 4: THỰC THI VÀ CHUẨN HÓA Y
# ==========================================

# 1. Xử lý dữ liệu X qua Pipeline hoàn chỉnh
X_processed = preprocessor.fit_transform(X)

# 2. Xử lý Y (Dùng MinMaxScaler để đưa về khoảng [0, 1])
scaler_y = MinMaxScaler()
y_processed = scaler_y.fit_transform(y).flatten()

# 3. Chia tập dữ liệu thành Train và Test (80/20)
X_train_final, X_test_final, y_train_final, y_test_final = train_test_split(
    X_processed, y_processed, test_size=0.2, random_state=42
)

# 4. KIỂM TRA CUỐI CÙNG TRƯỚC KHI VÀO NAS
print("--- HOÀN TẤT TIỀN XỬ LÝ SẠCH VÀ TỐI ƯU ---")
print(f"Kiểm tra X có NaN không: {np.isnan(X_train_final).any()}")
print(f"Số lượng đặc trưng thực tế cung cấp cho mạng MLP: {X_train_final.shape[1]}")
print(f"Giá trị Y lớn nhất sau chuẩn hóa: {y_processed.max()}")

import random
from sklearn.metrics import r2_score

# ==========================================
# THIẾT LẬP KHÔNG GIAN GENE (GIỐNG BÀI NAS-GA)
# ==========================================
gene_space_thanh = [
    [1, 2, 3, 4],  # Gene 0: num_layers (Số lớp từ 1 đến 4)
    [32, 64, 128, 256, 512],  # Gene 1: nodes Layer 1
    [32, 64, 128, 256, 512],  # Gene 2: nodes Layer 2
    [32, 64, 128, 256, 512],  # Gene 3: nodes Layer 3
    [32, 64, 128, 256, 512],  # Gene 4: nodes Layer 4
    [0, 1, 2, 3],  # Gene 5: activation index ("relu", "elu", "selu", "tanh")
    [0.1, 0.2, 0.3, 0.4, 0.5],  # Gene 6: dropout
    [0, 1, 2]  # Gene 7: optimizer index (Adam, RMSprop, SGD)
]


# ==========================================
# HÀM FITNESS_FUNC CHO RANDOM SEARCH
# ==========================================
def fitness_func_random(solution):
    num_layers = int(solution[0])
    nodes_list = [int(solution[1]), int(solution[2]), int(solution[3]), int(solution[4])]
    activation_idx = int(solution[5])
    dropout_rate = solution[6]
    optimizer_idx = int(solution[7])

    activations = ["relu", "elu", "selu", "tanh"]

    if optimizer_idx == 0:
        opt = Adam(learning_rate=0.001)
    elif optimizer_idx == 1:
        opt = RMSprop(learning_rate=0.001)
    else:
        opt = SGD(learning_rate=0.01)

    try:
        model = Sequential()
        # Lớp ẩn bắt buộc đầu tiên
        model.add(Dense(nodes_list[0], input_dim=X_train_final.shape[1], activation=activations[activation_idx]))
        model.add(Dropout(dropout_rate))

        # Các lớp ẩn tiếp theo dựa trên num_layers
        for i in range(1, num_layers):
            model.add(Dense(nodes_list[i], activation=activations[activation_idx]))
            model.add(Dropout(dropout_rate))

        model.add(Dense(1, activation='linear'))
        model.compile(loss='mae', optimizer=opt)

        # Huấn luyện nhanh 10 epochs giống hệt NAS-GA
        history = model.fit(
            X_train_final, y_train_final,
            epochs=10,
            batch_size=64,
            verbose=0,
            validation_split=0.2
        )

        val_mae = min(history.history['val_loss'])
        if np.isnan(val_mae): return 0

        # Trả về điểm Fitness theo công thức của Thành
        return 1000.0 / (val_mae + 1e-6)

    except Exception as e:
        return 0


# ==========================================
# THỰC THI THỬ NGHIỆM NGẪU NHIÊN VỚI 200 LƯỢT
# ==========================================
def run_random_search_nas(num_trials=870):
    print(f"\n--- BẮT ĐẦU RANDOM SEARCH NAS VỚI {num_trials} THỬ NGHIỆM ---")

    best_random_fitness = -1
    best_random_solution = None

    for trial in range(num_trials):
        # Lấy ngẫu nhiên các thông số cấu hình từ search space
        num_layers = random.choice(gene_space_thanh[0])
        nodes_1 = random.choice(gene_space_thanh[1])
        nodes_2 = random.choice(gene_space_thanh[2])
        nodes_3 = random.choice(gene_space_thanh[3])
        nodes_4 = random.choice(gene_space_thanh[4])
        activation_idx = random.choice(gene_space_thanh[5])
        dropout_rate = random.choice(gene_space_thanh[6])
        optimizer_idx = random.choice(gene_space_thanh[7])

        solution = [num_layers, nodes_1, nodes_2, nodes_3, nodes_4, activation_idx, dropout_rate, optimizer_idx]

        # Tính toán điểm thích nghi
        fitness = fitness_func_random(solution)

        if fitness > best_random_fitness:
            best_random_fitness = fitness
            best_random_solution = solution
            print(
                f"Lượt {trial + 1:03d} | Tìm thấy cấu hình tốt hơn -> Fitness: {best_random_fitness:.4f} | Số lớp: {num_layers}")

    return best_random_solution, best_random_fitness


# Chạy thuật toán tìm kiếm ngẫu nhiên làm Baseline
best_rand_sol, best_rand_fit = run_random_search_nas(num_trials=870)

# ==========================================
# ĐÁNH GIÁ CUỐI CÙNG KIẾN TRÚC RANDOM TRÊN TẬP TEST
# ==========================================
print("\n--- TIẾN HÀNH ĐÁNH GIÁ KIẾN TRÚC TỐI ƯU CỦA RANDOM NAS TRÊN TẬP TEST CHUẨN ---")

# Giải mã cấu hình tốt nhất tìm được từ Random Search
rand_num_layers = int(best_rand_sol[0])
rand_nodes_list = [int(best_rand_sol[1]), int(best_rand_sol[2]), int(best_rand_sol[3]), int(best_rand_sol[4])]
rand_activation_idx = int(best_rand_sol[5])
rand_dropout_rate = best_rand_sol[6]
rand_optimizer_idx = int(best_rand_sol[7])

activations = ["relu", "elu", "selu", "tanh"]

if rand_optimizer_idx == 0:
    final_opt = Adam(learning_rate=0.001)
elif rand_optimizer_idx == 1:
    final_opt = RMSprop(learning_rate=0.001)
else:
    final_opt = SGD(learning_rate=0.01)

# Xây dựng lại mô hình tối ưu của Random Search
final_rand_model = Sequential()
final_rand_model.add(
    Dense(rand_nodes_list[0], input_dim=X_train_final.shape[1], activation=activations[rand_activation_idx]))
final_rand_model.add(Dropout(rand_dropout_rate))

for i in range(1, rand_num_layers):
    final_rand_model.add(Dense(rand_nodes_list[i], activation=activations[rand_activation_idx]))
    final_rand_model.add(Dropout(rand_dropout_rate))

final_rand_model.add(Dense(1, activation='linear'))
final_rand_model.compile(loss='mae', optimizer=final_opt)

# Huấn luyện sâu (Cần chạy số Epochs lớn, ví dụ 100 epochs để tối ưu tối đa giống như mô hình kiểm thử của GA)
final_rand_model.fit(
    X_train_final, y_train_final,
    epochs=100,
    batch_size=64,
    verbose=0
)

# Dự đoán trên tập Test
y_pred_scaled = final_rand_model.predict(X_test_final)

# Đảo chuẩn hóa (Inverse Scale) để đưa kết quả dự đoán về dải điểm cpuMark gốc
y_pred_original = scaler_y.inverse_transform(y_pred_scaled)
y_test_original = scaler_y.inverse_transform(y_test_final.reshape(-1, 1))

# Tính toán các chỉ số đánh giá cuối cùng
final_rand_mae = np.mean(np.abs(y_test_original - y_pred_original))
final_rand_r2 = r2_score(y_test_original, y_pred_original)

print("\n==========================================")
print("=== KẾT QUẢ CUỐI CÙNG CỦA RANDOM NAS ===")
print("==========================================")
print(f"Kiến trúc tối ưu: Số lớp = {rand_num_layers}, Nodes = {rand_nodes_list[:rand_num_layers]}")
print(f"Hàm kích hoạt: {activations[rand_activation_idx]} | Dropout: {rand_dropout_rate}")
print(f"Best Fitness trong quá trình Search: {best_rand_fit:.4f}")
print(f"MAE cuối cùng trên tập Test: {final_rand_mae:.4f}")
print(f"R2 Score cuối cùng trên tập Test: {final_rand_r2:.4f}")
print("==========================================")

# Đoạn code tính Scaled MAE cho Random Search
y_min = scaler_y.data_min_[0]
y_max = scaler_y.data_max_[0]

mae_original = 1357.3955
scaled_mae_random = mae_original / (y_max - y_min)

print(f"Dải giá trị cpuMark: Min = {y_min}, Max = {y_max}")
print(f"MAE ban đầu: {mae_original}")
print(f"--> Scaled MAE của Random Search NAS: {scaled_mae_random:.4f}")

# ==========================================
# BƯỚC BỔ SUNG: CHẠY XGBOOST LÀM BASELINE MẠNH CHO TABULAR DATA
# ==========================================
from xgboost import XGBRegressor

print("\n------------------------------------------")
print("--- ĐANG HUẤN LUYỆN MÔ HÌNH XGBOOST BASELINE ---")
print("------------------------------------------")

# 1. Khởi tạo mô hình XGBoost với các tham số chuẩn cho Tabular
xgb_model = XGBRegressor(
    n_estimators=300,  # Số lượng cây
    max_depth=6,  # Độ sâu tối đa của cây
    learning_rate=0.05,  # Tốc độ học
    subsample=0.8,
    colsample_bytree=0.8,
    random_state=42,
    n_jobs=-1,  # Chạy tối đa nhân CPU
)

# 2. Huấn luyện XGBoost trên cùng tập Train đã tiền xử lý
xgb_model.fit(X_train_final, y_train_final)

# 3. Dự đoán trên tập Test
y_pred_xgb_scaled = xgb_model.predict(X_test_final).reshape(-1, 1)

# 4. Đảo chuẩn hóa (Inverse Scale) về dải điểm cpuMark gốc
y_pred_xgb_original = scaler_y.inverse_transform(y_pred_xgb_scaled)

# 5. Tính toán các chỉ số đánh giá
xgb_mae_original = np.mean(np.abs(y_test_original - y_pred_xgb_original))
xgb_r2 = r2_score(y_test_original, y_pred_xgb_original)
xgb_scaled_mae = xgb_mae_original / (y_max - y_min)

print("\n==========================================")
print("=== KẾT QUẢ CUỐI CÙNG CỦA XGBOOST BASELINE ===")
print("==========================================")
print(f"R2 Score trên tập Test       : {xgb_r2:.4f}")
print(f"MAE điểm gốc (cpuMark)      : {xgb_mae_original:.4f}")
print(f"Scaled MAE (Chuẩn hóa [0,1]) : {xgb_scaled_mae:.4f}")
print("==========================================")