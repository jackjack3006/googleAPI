from googleapiclient.discovery import build
from google.oauth2 import service_account


def read(hi):
    SERVICE_ACCOUNT_FILE = 'new.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '17rOLJBYmeWYGO6uGNj0KMqqhpQ9Wq-5-_ixvzCqkwYU'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=hi).execute()
    values = result.get('values', [1])
    return values


def write(aa, bb):
    SERVICE_ACCOUNT_FILE = 'new.json'
    SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
    creds = None
    creds = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)

    # The ID sample spreadsheet.
    SAMPLE_SPREADSHEET_ID = '17rOLJBYmeWYGO6uGNj0KMqqhpQ9Wq-5-_ixvzCqkwYU'

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    a = [[aa]]
    request = sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=bb, valueInputOption="USER_ENTERED",
                                    body={"values": a}).execute()
