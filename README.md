# Reproducible AI Pipeline for Medical Image Classification

This project demonstrates an end-to-end, **research-ready MLOps pipeline** for deep learning-based medical image classification. It’s designed for reproducibility, scalability, and real-world academic use cases — ideal for Research Cyberinfrastructure, AI Engineering, and MLOps roles.

## Project Goals

- Automate data ingestion, preprocessing, model training, and deployment
- Build reproducible infrastructure using tools like MLflow, Hydra, Docker
- Enable version-controlled, research-friendly workflows with CI/CD support
- Deploy a REST API inference endpoint (FastAPI) in a containerized setup

## Pipeline Components

1. **Data Ingestion & Preprocessing**
   - Source: CAMELYON16, PatchCamelyon, or public Kaggle histopathology datasets
   - Preprocessing with `albumentations`: resizing, normalization, augmentation

2. **Model Training**
   - Architecture: ResNet/EfficientNet in PyTorch
   - Logging: `TensorBoard` or `wandb`
   - Config management with `Hydra`

3. **Pipeline Automation**
   - Orchestrated using `MLflow` or `DVC`
   - Configurable experiments tracked via `Hydra`

4. **Deployment**
   - Export model with ONNX or TorchScript
   - Serve via `FastAPI`
   - Containerized with `Docker`
   - CI/CD using `GitHub Actions`

5. **Reproducibility**
   - Docker image for full environment replication
   - `.env` and YAML configs for setup
   - `Jupyter` + `RMarkdown` documentation

---

## Getting Started

### Requirements
- Python 3.10+
- PyTorch, FastAPI, albumentations, MLflow
- Docker (for deployment)
- Optional: wandb, Hydra, GitHub Actions

### Setup

```bash
# Clone the repo
git clone https://github.com/your-username/medical-ai-pipeline.git
cd medical-ai-pipeline

# Install dependencies
pip install -r requirements.txt

# Or create a conda environment
conda env create -f environment.yml
conda activate medical-ai-pipeline
