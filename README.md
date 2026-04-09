# 🚀 Fraud Detection OpenEnv

## 📌 Overview
This project implements a **Fraud Detection AI Environment** using OpenEnv standards, where an AI agent classifies whether a call is fraudulent or not based on given features.

---

## 🧠 Problem Statement
Detect fraudulent calls using AI by analyzing simple behavioral patterns like:
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
The environment supports multiple difficulty levels:

- 🟢 Easy  
- 🟡 Medium  
- 🔴 Hard  

---

## 🤖 Inference
The model uses an LLM via OpenAI-compatible API (LiteLLM proxy in evaluation).

Structured outputs are generated using:
