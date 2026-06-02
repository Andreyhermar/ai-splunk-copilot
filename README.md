# 🧠 AI Splunk Copilot

An AI-powered log troubleshooting assistant that analyzes system logs using a local LLM (Ollama) and provides structured root cause analysis, severity classification, and remediation steps through a Streamlit interface.

---

## 🚀 Overview

AI Splunk Copilot simulates an SRE-style incident analysis tool. It allows users to paste raw system or application logs and receive AI-generated insights such as:

- 🔍 Root cause analysis
- 🛠️ Suggested fixes
- ⚠️ Severity classification (P1 / P2 / P3)
- 📊 Confidence estimation

This project is designed for learning AI engineering, prompt design, and DevOps-style system architecture using local inference.

---

## 🧱 Architecture


User Input (Logs)
↓
Streamlit UI
↓
Python Backend
↓
Ollama (Local LLM)
↓
AI-generated troubleshooting response


---

## ⚙️ Tech Stack

- Python
- Streamlit (UI)
- Ollama (Local LLM inference)
- Llama 3 (default model)
- Requests (API communication)

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/Andreyhermar/ai-splunk-copilot.git
cd ai-splunk-copilot