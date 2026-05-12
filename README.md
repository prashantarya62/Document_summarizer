# AI Document Summarizer

An AI-powered document summarization system built using FastAPI, Google Drive API, and Gemini AI.

---
    
# Features

- Google Drive Integration
- PDF/DOCX/TXT Parsing
- Gemini AI Summarization
- FastAPI Backend
- Styled HTML Dashboard
- CSV Report Download
- PDF Report Download
- Google Drive File Links

---

# Tech Stack

- Python
- FastAPI
- Google Drive API
- Gemini AI
- Jinja2
- Bootstrap
- ReportLab

---

# Project Structure

```bash
Gen_AI_Assignment/
│
├── app.py
├── requirements.txt
├── .env
├── credentials.json
├── token.json
│
├── downloads/
├── reports/
│
├── services/
│   ├── drive_service.py
│   ├── parser_service.py
│   ├── summarizer_service.py
│   └── export_service.py
│
├── templates/
│   └── index.html
│
└── README.md