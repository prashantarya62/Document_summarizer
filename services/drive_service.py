import io
import os

from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

from googleapiclient.discovery import build
from googleapiclient.http import MediaIoBaseDownload

SCOPES = ['https://www.googleapis.com/auth/drive']

DOWNLOAD_FOLDER = "downloads"


def get_drive_service():

    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file(
            'token.json',
            SCOPES
        )

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())

        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                SCOPES
            )

            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('drive', 'v3', credentials=creds)

    return service


def list_files(folder_id):

    service = get_drive_service()

    query = f"'{folder_id}' in parents"

    results = service.files().list(
        q=query,
        fields="files(id, name, mimeType)"
    ).execute()

    return results.get("files", [])


def download_file(file_id, file_name):

    service = get_drive_service()

    request = service.files().get_media(fileId=file_id)

    os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

    file_path = os.path.join(DOWNLOAD_FOLDER, file_name)

    fh = io.FileIO(file_path, 'wb')

    downloader = MediaIoBaseDownload(fh, request)

    done = False

    while not done:
        status, done = downloader.next_chunk()

    return file_path