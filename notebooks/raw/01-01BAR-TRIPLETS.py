# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.0
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 01-01 BAR TRIPLETS

# This notebook creates a triplet DataFrame (ID, TIME, VALUE) and saves it.

# # GENERAL SETTINGS --------------------------------------

# ### Cells Hiding
#
# This part creates a button that can Show/Hide code.

# +
from IPython.display import HTML

HTML('''<script> 
code_show=true;  
function code_toggle() { 
if (code_show){ 
$('div.input').hide(); 
} else { 
$('div.input').show(); 

} 
code_show = !code_show 
}  
$( document ).ready(code_toggle); 
</script> 
<form action="javascript:code_toggle()"><input type="submit" value="Show/Hide code"></form>''')
# -

# ### Paths

import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), os.pardir)))  # one up
sys.path.insert(0, os.path.abspath(os.path.join(os.getcwd(), "../..")))  # two up

# ### Initial Timestamp

import src.Utils.Timerer as TMR

tr = TMR.Timerer()
tr.set_initial_timestamp()

# ### General Libraries

import pandas as pd
import numpy as np

from importlib import reload

# ### Personal Libraries

import src.Data.DFExplorer as DFE
import src.Data.TimeSeriesGenerator as TSG
import src.Data.SaverAndLoader as TSL

reload(DFE)
reload(TSG)
reload(TSL)

# ### Notebook Settings

# Display settings:

pd.options.display.max_rows = 500
pd.options.display.max_columns = 50

# Constants:

from src.GlobalConstants import ATTR_ID, ATTR_TIME, ATTR_VALUE

TRIPLET_NAME = "TripletDataFrame"
WHERE_TO_STORE = "raw"
SIZE = 10000

ATTRS_TRIPLET = [ATTR_ID, ATTR_TIME, ATTR_VALUE]


# # ANALYSIS ---------------------------------------------------------

# In this section, the goal is to create a triplet DataFrame, explore it and save the newly
# transformed DataFrame.

# ## Data Generation

# The Data is generated with the class generate_sample_triplet_df(). We will provide provide an
# ID list to specify the size of the sample (the variable SIZE modifies the size of the DataFrame).

def _gen_id_list(size):
    np.random.seed(123)
    id_list = [np.random.randint(1, 9) for i in range(size - 1)]
    id_list.append(10)
    return id_list


df_triplet = TSG.TimeSeriesGenerator().generate_sample_triplet_df(id_list=_gen_id_list(SIZE), int_data=True)

# ## Data Basic Exploration

dfe = DFE.DFExplorer()
dfs = {"TRPLT": df_triplet}
for name in dfs.keys():
    df = dfs[name]
    print(f"========== Data frame for {name} DataFrame. ==========")
    dfe.print_info_about_data_frame(df)
    dfe.print_attr_stats(df)
    print("\n\n")

# ## Saving Triplet

tsl = TSL.SaverAndLoader(None)
tsl.save_triplet(df_triplet, TRIPLET_NAME, ATTRS_TRIPLET, WHERE_TO_STORE)

# ### Loading Triplet

df_loaded = tsl.load_triplet(TRIPLET_NAME, ATTRS_TRIPLET, WHERE_TO_STORE)

# ### Checking Saver and Loader

print(df_triplet.equals(df_loaded))

# ## Final Timestamp

tr.set_final_timestamp()
