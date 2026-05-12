import os

from fastapi import FastAPI, Request
from fastapi.responses import FileResponse
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse

from services.drive_service import (
    list_files,
    download_file
)

from services.parser_service import (
    parse_document
)

from services.summarizer_service import (
    summarize_text
)

from services.export_service import (
    create_csv,
    create_pdf
)

app = FastAPI(title="Document Summarization Service",
                description="A service that summarizes documents from Google Drive using Gemini API",
                )
templates = Jinja2Templates(
    directory="templates"
)

FOLDER_ID = "18eC6XmBjZWYvLclvL99Y5sVfhiBKbJc_"

REPORT_FOLDER = "reports"

os.makedirs(REPORT_FOLDER, exist_ok=True)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    files = list_files(FOLDER_ID)
    print("FOLDER ID:", FOLDER_ID)
    print("files:", files)

    results = []

    for file in files:

        try:

            file_path = download_file(
                file["id"],
                file["name"]
            )

            extracted_text = parse_document(
                file_path
            )
            summary = summarize_text(
                extracted_text  
            )

        except Exception as e:

            summary = f"Error: {str(e)}"

        results.append({
            "file_name": file["name"],
            "summary": summary,
            "link": f"https://drive.google.com/file/d/{file['id']}/view"
        })

    csv_path = os.path.join(
        REPORT_FOLDER,
        "summaries.csv"
    )

    pdf_path = os.path.join(
        REPORT_FOLDER,
        "summaries.pdf"
    )

    create_csv(results, csv_path)

    create_pdf(results, pdf_path)

    return templates.TemplateResponse(
        request=request, name="index.html", context={"results": results}
    )

@app.get("/download/csv")
def download_csv():

    return FileResponse(
        "reports/summaries.csv",
        media_type="text/csv",
        filename="summaries.csv"
    )


@app.get("/download/pdf")
def download_pdf():

    return FileResponse(
        "reports/summaries.pdf",
        media_type="application/pdf",
        filename="summaries.pdf"
    )