import gspread
from gspread_dataframe import get_as_dataframe
import streamlit as st
from oauth2client.service_account import ServiceAccountCredentials

credentials = ServiceAccountCredentials.from_json_keyfile_dict(st.secrets["GOOGLE_APPLICATION_CREDENTIALS"])
gc = gspread.authorize(credentials)

DOC_ID = "1_HgTNFTli6Te9kHuceVZkNHOP6I82RX0NQY9VAesMBI"
doc = gc.open_by_key(DOC_ID)

def load_spreadsheet():
    doc = gc.open_by_key(DOC_ID)
    return doc

def get_dataframe_from_sheet(sheet_name, skiprows=None):
    sheet = doc.worksheet(sheet_name)
    df = get_as_dataframe(sheet, evaluate_formulas=True, skiprows=skiprows).dropna(how='all').dropna(how='all', axis='columns')
    return df

def load_simulation_parameters():
    global gc

    # Parameters: from sheets to dict
    doc = load_spreadsheet()
    df_levels = get_dataframe_from_sheet("Levels", doc)
    df_products = get_dataframe_from_sheet("Products", doc)

    recipes_dict = {}

    df_recipes = df_products.query("Type != 'Crop'")

    for product in df_recipes["Name"]:
        df_product = df_recipes.query(f"Name == '{product}'")
        
        # Initialize a dictionary for the product
        product_ingredients = {}

        for i in range(3):
            ingredient = df_product[f"Ingredient {i+1}"].values[0] if not df_product[f"Ingredient {i+1}"].isnull().values[0] else None
            quantity = df_product[f"Quantity {i+1}"].values[0] if not df_product[f"Quantity {i+1}"].isnull().values[0] else None

            if ingredient and quantity:
                product_ingredients[ingredient] = quantity
        
        print(product)
        recipes_dict[product] = product_ingredients

        # SC needed for a recipe
        


    return {
        "player_progression" : dict(zip(df_levels["Level"], df_levels["Cumulative XP"])),
        "df_products" : df_products,
        "products_list" : df_products["Name"],
        "df_levels" : df_levels,
        "recipes_dict" : recipes_dict,
        "df_recipes" : df_recipes
    }

