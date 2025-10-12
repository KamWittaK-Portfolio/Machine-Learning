# 🧠 K-Nearest Neighbors (KNN) Machine Learning Pipeline

A complete end-to-end machine learning project built around the **K-Nearest Neighbors algorithm**, powered by **Azure compute resources** and integrated with modern **MLOps tools** for experiment tracking, reproducibility, and automation.

---

## 📋 Project Overview

This project builds a **K-Nearest Neighbors (KNN)** classifier using a modular, production-ready **machine learning pipeline**.
It follows modern **MLOps principles** for reproducibility, scalability, and continuous experimentation.

The pipeline retrieves data from **multiple sources** — such as CSV files, cloud storage, and databases — merges them into a single validated dataset, and performs cleaning, normalization, and encoding before model training and evaluation.
All experiments, metrics, and model versions are tracked through **MLflow**, while **Supabase** stores pipeline artifacts.
The entire workflow runs on **Azure virtual machines**, leveraging cloud compute for training and evaluation.

---

## 🧰 Tech Stack

---
| Category | Technology |
|-----------|-------------|
| Language | Python 3.12 |
| Compute Environment | Azure Virtual Machine |
| Pipeline Orchestration | ZenML |
| Experiment Tracking | MLflow |
| Artifact Storage | Supabase |
| Machine Learning | scikit-learn (KNN algorithm) | 
| Data Handling | pandas, numpy | 
| Testing | pytest |
| Environment Management| .env file (dotenv) |
| Logging | Python logging + ZenML/MLflow |
| Serialization | Pickle for saving models |
---

## 🧩 Pipeline Architecture

Each step of the pipeline is defined as a ZenML step:

| Step | File | Description |
|------|------|--------------|
| **Ingest** | `src/steps/ingest.py` | Collects and merges data from multiple sources. |
| **Preprocess** | `src/steps/preprocess.py` | Cleans, normalizes, and encodes features. |
| **Train** | `src/steps/train.py` | Trains the K-Nearest Neighbors model. |
| **Evaluate** | `src/steps/evaluate.py` | Evaluates model performance and logs metrics. |
| **Pipeline Definition** | `src/pipelines/train_pipeline.py` | Connects all steps into one reproducible pipeline. |


## ⚙️ How It Works

1. **Run the pipeline**
   ```bash
   python run.py
   ```
   This triggers the ZenML pipeline defined in `src/pipelines/train_pipeline.py`.

2. **Track experiments**
   - MLflow logs are automatically created under `/mlruns`.
   - Run the MLflow UI to view metrics and models:
     ```bash
     mlflow ui
     ```
     Access it via `http://localhost:5000`.

3. **Evaluate performance**
   - Evaluation results (e.g., accuracy) are stored in the MLflow run’s metrics directory.
   - You can compare different pipeline runs visually in the MLflow dashboard.

4. **Reproduce runs**
   - All pipeline steps are versioned.
   - Each run’s metadata (model, parameters, and metrics) is stored under `mlartifacts/`.

---

## 🧪 Testing

Run all unit tests to validate each step:

```bash
pytest
```

Test coverage includes:
- `test_ingest.py` — Verifies dataset loading.
- `test_preprocess.py` — Ensures preprocessing works correctly.
- `test_evaluate.py` — Checks evaluation logic and metric calculation.

---

## 🧵 Folder Structure

```
(3) K-Nearest Neighbors/
│
├── run.py                          # Entry point for running the pipeline
├── .env                            # Environment configuration
├── data/
│   └── KNNAlgorithmDataset.csv      # Input dataset
│
├── src/
│   ├── pipelines/
│   │   └── train_pipeline.py        # ZenML pipeline definition
│   └── steps/
│       ├── ingest.py
│       ├── preprocess.py
│       ├── train.py
│       └── evaluate.py
│
├── tests/                          # Unit tests for each pipeline step
├── mlruns/                         # MLflow tracking directory
├── mlartifacts/                    # MLflow artifact store
└── .zen/                           # ZenML configuration
```

---

## 🌐 Cloud + MLOps Integration

The project seamlessly combines:

- Azure Compute — executes pipelines and heavy ML workloads.
- MLflow — tracks runs, metrics, and models.
- Supabase — stores model artifacts and experiment data.
- ZenML — orchestrates all steps and manages pipeline logic.
- You can deploy MLflow with Docker for local or cloud tracking:

You can serve MLflow via Docker:

```bash
sudo docker run -d -p 5000:5000 \
  -v "$(pwd)/mlruns:/mlruns" \
  ghcr.io/mlflow/mlflow \
  mlflow server \
  --backend-store-uri sqlite:///mlflow.db \
  --default-artifact-root /mlruns \
  --host 0.0.0.0
```

---

## 🧠 Model Details

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Framework:** scikit-learn
- **Metrics:** Accuracy (and optionally precision/recall)
- **Model Output:** Serialized as `model.pkl`
- **Environment:** Defined in `python_env.yaml` for reproducibility

---

## 🚀 Future Enhancements

- Add hyperparameter optimization for K values
- Deploy trained models with FastAPI and Docker

---

## 👤 Author

**Kameron Fournillier**  
Machine Learning Developer  