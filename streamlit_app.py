import altair as alt
import numpy as np
from model import * 

# Loading parameters

if 'simulation_parameters' not in st.session_state:
    st.session_state['simulation_parameters'] = params

if st.sidebar.button("Reload Data"):
    st.session_state['simulation_parameters'] = load_simulation_parameters()
    params = st.session_state['simulation_parameters']


"""
# Welcome to Streamlit! ! 

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:.
If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""

st.dataframe(params["df_products"])
st.write(params["recipes_dict"]["cookie"])
cookie = params["recipes_dict"]["cookie"]

st.write(params["products_lists"])


# for ingredient, quantity in cookie.items():
#     st.write(ingredient, quantity)

