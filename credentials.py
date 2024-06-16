import gspread
from gspread_dataframe import get_as_dataframe
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"])
gc = gspread.authorize(credentials)

DOC_ID = "1kUY8Suw4jS2MhtNRQcHhogf04WdV7ubMpHwnaCPlir0"
doc = gc.open_by_key(DOC_ID)

def get_dataframe_from_sheet(sheet_name, skiprows=None):
    sheet = doc.worksheet(sheet_name)
    df = get_as_dataframe(sheet, evaluate_formulas=True, skiprows=skiprows).dropna(how='all').dropna(how='all', axis='columns')
    return df

df = get_dataframe_from_sheet("Data")
