# 🚀 Fraud Detection OpenEnv

## 📌 Overview
This project implements a **Fraud Detection AI Environment** using OpenEnv standards, where an AI agent classifies whether a call is fraudulent or not based on simple behavioral features.

---

## 🧠 Problem Statement
Detect fraudulent calls using AI by analyzing patterns such as:
- Call duration  
- Call frequency  

---

## ⚙️ Environment Design

### 🔍 Observation Space
- `duration` → Length of call  
- `frequency` → Number of calls  

---

### 🎯 Action Space
- `0` → Not Fraud  
- `1` → Fraud  

---

### 🏆 Reward Function
- Correct prediction → **1.0**  
- Wrong prediction → **0.0**

---

## 🧪 Tasks

The environment includes multiple difficulty levels:

- 🟢 **Easy** → Basic fraud patterns (low frequency, short duration)  
- 🟡 **Medium** → Suspicious behavior (moderate anomalies)  
- 🔴 **Hard** → Complex fraud patterns (high frequency + unusual duration)  

---

## 🤖 AI Component
This project uses an **LLM (Large Language Model)** via an OpenAI-compatible API (LiteLLM proxy during evaluation) to simulate intelligent decision-making in fraud detection scenarios.

---

## 💡 Real-world Impact
This system can help telecom companies and service providers:
- Detect fraudulent call patterns  
- Reduce financial losses  
- Improve automated fraud monitoring systems  

---

This project follows a clean and modular structure for easy deployment and evaluation.

---

## 📁 Project Structure

```
fraud-openenv/
├── server/
│   └── app.py          # FastAPI + Gradio app (OpenEnv API)
├── inference.py        # LLM inference script (Phase 2)
├── app.py              # Hugging Face entry file
├── openenv.yaml        # OpenEnv configuration
├── Dockerfile          # Container setup
├── requirements.txt    # Dependencies
├── pyproject.toml      # Project configuration
├── uv.lock             # Dependency lock file
└── README.md           # Documentation
```

---

## 🚀 How to Run

```bash
python inference.py
```
