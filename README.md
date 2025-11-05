# AIoT_HW3_spam_email_classification

This repository contains a homework project for spam (SMS/email) classification. See `openspec/project.md` for the project context, conventions, and quickstart.

Quick steps:

1. Create a virtual environment and install dependencies:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

2. Run a quick training (example):

```powershell
python -m src.train --data "https://raw.githubusercontent.com/PacktPublishing/Hands-On-Artificial-Intelligence-for-Cybersecurity/refs/heads/master/Chapter03/datasets/sms_spam_no_header.csv" --out models/baseline.joblib
```

3. Run inference (example):

```powershell
python -m src.infer --model models/baseline.joblib --text "Free money"
```

4. Run the Streamlit demo

```powershell
pip install -r requirements.txt
streamlit run streamlit_app.py
```
