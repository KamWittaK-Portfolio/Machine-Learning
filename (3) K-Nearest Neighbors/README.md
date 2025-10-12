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

| Category | Technology |
|-----------|-------------|
| **Language** | Python 3.12 |
| **Compute Environment** | Azure Virtual Machine |
| **Pipeline Orchestration** | ZenML |
| **Experiment Tracking** | MLflow |
| **Artifact Storage** | Supabase |
| **Machine Learning** | scikit-learn (KNN algorithm) | 
| **Data Handling** | pandas, numpy | 
| **Testing** | pytest |
| **Environment Management** | .env file (dotenv) |
| **Logging** | Python logging + ZenML/MLflow |
| **Serialization** | Pickle for saving models |
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

## 🧪 Testing

Test coverage includes:
- `test_ingest.py` — Verifies dataset loading.
- `test_preprocess.py` — Ensures preprocessing works correctly.
- `test_evaluate.py` — Checks evaluation logic and metric calculation.

---

## ⚙️ Continuous Integration & Deployment (CI/CD)

This project uses **GitHub Actions** to automate testing and deployment through a structured CI/CD pipeline.

- **Development Branch Workflow** (`Dev`)

   After a pull request from a feature branch, GitHub Actions automatically:

   1. Installs dependencies

   2. Runs unit tests inside the project directory

   3. Validates that the pipeline components execute correctly before merging

- **Production Deployment (`Prod`)**
   
   After a pull request merges into the Prod branch, the workflow:

   1. Connects to the remote production server via SSH

   2. Pulls the latest production code

   3. Activates the virtual environment and ZenML stack

   4. Executes the full **production pipeline** (`run.py`) end to end

This ensures a fully automated transition from **development** → **testing** → **production**, improving consistency, reproducibility, and deployment reliability.

---

## 🌐 Cloud + MLOps Integration

The project seamlessly combines:

- Azure Compute — executes pipelines and heavy ML workloads.
- MLflow — tracks runs, metrics, and models.
- Supabase — stores model artifacts and experiment data.
- ZenML — orchestrates all steps and manages pipeline logic.
- You can deploy MLflow with Docker for local or cloud tracking:

---

## 🧠 Model Details

- **Algorithm:** K-Nearest Neighbors (KNN)
- **Framework:** scikit-learn
- **Metrics:** Accuracy (and optionally precision/recall)
- **Model Output:** Serialized as `model.pkl`
- **Environment:** Defined in `python_env.yaml` for reproducibility

---