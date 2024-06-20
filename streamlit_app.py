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
# Farm Resource Manager Game
## Economy Simulation 

### Products
"""



selection = st.selectbox("Select product to check recipe", params["df_recipes"]["Name"])

recipe = params["recipes_dict"][selection]

st.dataframe(recipe)

"""
### Player Inventory
"""

st.write(f"Player has: ")
df = pd.DataFrame.from_dict(player.inventory, orient="index", columns=["Amount"])
st.dataframe(df[df.index.isin(recipe.keys())])