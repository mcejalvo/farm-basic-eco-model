import os
import gspread
from gspread_dataframe import get_as_dataframe, set_with_dataframe

GOOGLE_APP_CREDENTIALS = os.getenv('GOOGLE_APPLICATION_CREDENTIALS')
DOC_ID = "1kUY8Suw4jS2MhtNRQcHhogf04WdV7ubMpHwnaCPlir0"
gc = gspread.service_account(filename=GOOGLE_APP_CREDENTIALS)

def load_spreadsheet():
    doc = gc.open_by_key(DOC_ID)
    return doc

def get_dataframe_from_sheet(sheet_name, skiprows=None):
    df = get_as_dataframe(doc.worksheet(sheet_name), evaluate_formulas=True, skiprows=skiprows).dropna(how='all').dropna(how='all', axis='columns')
    return df

doc = gc.open_by_key(DOC_ID)
df = get_dataframe_from_sheet("Data")