from services.drive_service import list_files, download_file
from services.parser_service import parse_document
from services.summarizer_service import summarize_text

FOLDER_ID = "18eC6XmBjZWYvLclvL99Y5sVfhiBKbJc_"

files = list_files(FOLDER_ID)

for file in files:

    print("\n====================")
    print("FILE:", file["name"])

    file_path = download_file(
        file["id"],
        file["name"]
    )

    extracted_text = parse_document(file_path)
    print("\nEXTRACTED TEXT:\n")
    print(extracted_text[:1000])  # Print only the first 1000 characters for brevity
    summary = summarize_text(extracted_text)

    print("\nSUMMARY:\n")

    print(summary)