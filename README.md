# CyberSentinel AI – Network Security & Threat Detection System  
_End-to-End MLOps & Cloud Deployment Project_

## 📌 Project Overview
CyberSentinel AI is an **AI-powered cyber threat detection system** designed to automatically detect and block malicious websites and suspicious IP addresses.  
The system leverages **machine learning, MLOps pipelines, and cloud deployment** to deliver scalable, automated, and enterprise-ready security monitoring.

---

## 🎯 Aim of the Project
- Detect **malicious websites & IPs** in real-time.
- Automate **monitoring, detection, and blocking** to reduce manual effort.
- Build a **robust MLOps framework** for reproducibility, versioning, and continuous deployment.

---
## 📂 Project Structure

├── data/                    # Raw and processed data
├── src/                     # Source code
│ ├── ingestion/             # Data ingestion components
│ ├── validation/            # Data validation logic
│ ├── transformation/        # Data transformation scripts
│ ├── trainer/               # Model training pipeline
│ ├── predictor/             # Batch prediction pipeline
│ ├── utils/                 # Logging & exception handling
├── artifacts/               # Stored ML artifacts
├── Dockerfile               # Docker image build
├── requirements.txt         # Python dependencies
├── setup.py                 # Package configuration
├── config.yaml              # Project configurations
└── README.md                # Project documentation

## 🏗️ Project Architecture
1. **Data Ingestion**
   - Extracted datasets from APIs and websites.
   - Stored in **MongoDB Atlas** and **PostgreSQL**.
   - Configured ingestion pipelines with schema validation.

2. **ETL Pipelines**
   - Automated Extract → Transform → Load workflows.
   - NASA API integration for external data sources.
   - Data cleaning, validation, and transformation.

3. **Data Processing**
   - Feature engineering, handling missing values, and schema validation.
   - Data transformation with encoding & scaling.

4. **Model Training**
   - Trained ML models (Logistic Regression, Random Forest, XGBoost).
   - Applied **hyperparameter tuning** for optimization.
   - Ensured reproducibility with **MLflow**.

5. **Experiment Tracking**
   - Used **MLflow + DagsHub** for tracking metrics, parameters, and artifacts.
   - Enabled collaborative, cloud-based experiment management.

6. **Deployment**
   - Containerized using **Docker**.
   - Automated CI/CD pipelines with **GitHub Actions**.
   - Deployed models to **AWS (S3, ECR, EC2)**.

7. **Batch Prediction Pipeline**
   - Implemented batch processing for real-time predictions.
   - Built a simple frontend for user-friendly output.

---

## ⚙️ Tech Stack
- **Programming**: Python  
- **ML & MLOps**: Scikit-learn, MLflow, DagsHub  
- **Databases**: MongoDB Atlas, PostgreSQL  
- **Cloud & DevOps**: AWS (S3, ECR, EC2), Docker, GitHub Actions  
- **Others**: Logging, Exception Handling, ETL Pipelines  

---

## 🚀 Business Impact
- **93% Accuracy** in detecting malicious websites & IPs.  
- Reduced **manual monitoring costs** through automation.  
- Improved **security response time** with real-time detection.
- Delivered **enterprise-grade scalability** using AWS cloud.  
- Enabled **continuous model retraining & versioning** with CI/CD.  

---




