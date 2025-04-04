# Fraud-Detection-with-Streaming-Data


A real-time fraud detection pipeline using Apache Kafka, a Random Forest model, and Snowflake for data storage. This project demonstrates streaming data processing, machine learning, and cloud integration—ideal for fintech and cybersecurity applications.

## Project Overview
- **Goal**: Detect fraudulent credit card transactions in real-time.
- **Tools Used**: Python (Scikit-learn, Kafka-Python), Apache Kafka, Snowflake.


## Setup Instructions

### Prerequisites
- Python 
- Apache Kafka (Docker)
- Snowflake 
- Dataset: [Kaggle Credit Card Fraud Detection](https://www.kaggle.com/mlg-ulb/creditcardfraud)

### Installation
1. **Install dependencies**:
   ```bash
   pip install kafka-python scikit-learn pandas snowflake-connector-python imblearn joblib
