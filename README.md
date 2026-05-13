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

# Setup Instructions

## 1. Clone Repository

```bash
git clone https://github.com/prashantarya62/Document_summarizer.git
```

---

## 2. Move Into Project Folder

```bash
cd Document_summarizer
```

---

## 3. Create Virtual Environment

```bash
python -m venv .venv
```

---

## 4. Activate Virtual Environment

### Windows

```bash
.venv\Scripts\activate
```

### Mac/Linux

```bash
source .venv/bin/activate
```

---

## 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---
# Google Drive API Setup

## 6. Open Google Cloud Console

Visit:

https://console.cloud.google.com/

---

## 7. Create a Google Cloud Project

### Top Navigation Bar

At the top of the page:

* Click the project dropdown
* Click **NEW PROJECT**

### Create Project

* Enter Project Name
* Click **CREATE**

Wait a few seconds for project creation.

---

## 8. Enable Google Drive API

Open:

https://console.cloud.google.com/apis/library

Search:

```text
Google Drive API
```

Click:

```text
ENABLE
```

---

## 9. Configure OAuth Consent Screen

Open:

https://console.cloud.google.com/apis/credentials/consent



### Fill Required Fields

* App Name
* User Support Email
* Developer Contact Email

Click:

```text
SAVE AND CONTINUE
```

Skip optional sections until completion.

---


## 10. Create OAuth Credentials

Open:

https://console.cloud.google.com/apis/credentials

Click:

```text
+ CREATE CREDENTIALS
```

Select:

```text
OAuth Client ID
```

### Application Type

Choose:

```text
Desktop App
```

Click:

```text
CREATE
```

---

## 11. Download OAuth Credentials

Click:

```text
DOWNLOAD JSON
```

Rename downloaded file to:

```text
credentials.json
```

Place it in project root folder.

---
## 12. Add Test Users

Open:

https://console.cloud.google.com/apis/credentials/consent

click on Audience:

Publish app

Save changes.

---

## 13. Authenticate Google Drive Access

Open terminal inside the project folder.

### Windows (PowerShell)

```bash
cd path/to/Document_summarizer
```

Run:

```bash
gcloud auth application-default login --scopes="https://www.googleapis.com/auth/cloud-platform https://www.googleapis.com/auth/drive"
```

---

### What Happens Next

* Browser window opens automatically
* Login with your Google account
* Click:

  * Continue
  * Allow permissions

After successful login, Google creates Application Default Credentials (ADC) locally.

This allows the application to securely access Google Drive files.

---

### Verify Authentication

Run:

```bash
gcloud auth application-default print-access-token
```

If authentication works, you will see a long access token printed in terminal.
"

---

# Gemini API Setup

## 14. Create `.env` File

Create a `.env` file in the project root.

Add:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get API key from:

https://aistudio.google.com/app/apikey

---


## 15. Configure Google Drive Folder ID

Open `app.py`

Find:

```python
FOLDER_ID = "YOUR_FOLDER_ID"
```

Replace with your Google Drive folder ID.

Example:

```python
FOLDER_ID = "18eC6XmBjZWYvLclvL99Y5sVfhiBKbJc_"
```

---

### How To Get Folder ID

If your Google Drive folder URL is:

```text
https://drive.google.com/drive/folders/18eC6XmBjZWYvLclvL99Y5sVfhiBKbJc_
```

Then your Folder ID is:

```text
18eC6XmBjZWYvLclvL99Y5sVfhiBKbJc_
```


# Run Application

## 16. Start FastAPI Server

```bash
uvicorn app:app --reload
```

---

## 17. Open Browser

Visit:

```for Swagger UI
http://127.0.0.1:8000/docs
```

```for summaries UI and download links 
http://127.0.0.1:8000/
```
---

# Features

* Google Drive Integration
* PDF/DOCX/TXT Parsing
* Gemini AI Summarization
* Styled HTML Table
* CSV Export
* PDF Export
* Google Drive File Links
