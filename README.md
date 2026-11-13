# Neural Architecture Search using Genetic Algorithm (NAS-GA) for CPU Performance Prediction

Official repository for the paper: **"Neural Architecture Search using Genetic Algorithm for Accurate CPU Performance Prediction"**.

## Overview
This project implements an automated Neural Architecture Search framework driven by a Genetic Algorithm (NAS-GA) tailored for tabular microprocessor performance prediction (`cpuMark`). The search algorithm optimizes network depth, layer widths, activation functions, dropout regularization, and gradient optimizers across a 138-dimensional feature space derived from 1,618 curated Intel and AMD processor configurations.

## Repository Structure
- `nas_ga_cpu`: Complete pipeline including data preprocessing, 138-D feature encoding, evolutionary NAS-GA optimization, baseline comparisons, and evaluation.
- `CPU_benchmark_v4.csv`: Raw benchmark dataset derived from the CPU Benchmarks Compilation hosted on Kaggle and enriched with official PassMark hardware specifications (3,826 raw entries before filtering down to 1,618 Intel and AMD records).
- `runs_checkpoint.json`: Saved experimental checkpoints and evaluation metrics across 5 independent random seeds (`42, 10, 100, 2024, 777`).
- `Figure_4_Fitness_Curve.png` & `Figure_5_Predictions_vs_Reality.png`: Generated visualizations of evolutionary convergence and test-set prediction alignment.

## Requirements & Installation
The experiments were executed using Python 3.10 on a standard CPU workstation (Intel Core i5-10500H, 16 GB RAM). Install the required dependencies via:

```bash
pip install tensorflow scikit-learn numpy pandas matplotlib xgboost