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
# Farm Resource Manager Toy Model
## Economy Simulation 
"""

st.dataframe(params["df_products"])
st.write(params["recipes_dict"]["cookie"])
cookie = params["recipes_dict"]["cookie"]


for ingredient, quantity in cookie.items():
    st.write(ingredient, quantity)

