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

# # 01-02 BAR TIMESERIES

# This notebook creates a timeseries (ID, TIME-VALUE) from a triplet DataFrame (ID, TIME, VALUE)
# and saves it.

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

from importlib import reload

# ### Personal Libraries

import src.Data.DFExplorer as DFE
import src.Data.SaverAndLoader as TSL
import src.Transformation.DFToMultiTSTransformator as TST

reload(DFE)
reload(TSL)
reload(TST)

# ### Notebook Settings

# Display settings:

pd.options.display.max_rows = 500
pd.options.display.max_columns = 50

# Constants:

from src.GlobalConstants import ATTR_ID, ATTR_TIME, ATTR_VALUE, ATTR_TIMESERIES

TRIPLET_NAME = "TripletDataFrame"
TIMESERIES_NAME = "TimeseriesDataFrame"
WHERE_TO_STORE = "raw"

ATTRS_TRIPLET = [ATTR_ID, ATTR_TIME, ATTR_VALUE]
ATTRS_TIMESERIES = [ATTR_ID, ATTR_TIMESERIES]

# # ANALYSIS ---------------------------------------------------------

# In this section, the goal is to load a triplet DataFrame, apply the timeseries transformator and
# save the newly transformed DataFrame.

# ## Data Generation

# In 01-01 BAR TRIPLET the DataFrame was generated and thus, in this notebook we will use that
# Data:

tsl = TSL.SaverAndLoader(None)
df_triplet = tsl.load_triplet(TRIPLET_NAME, ATTRS_TRIPLET, WHERE_TO_STORE)

# ## Timeseries Transformator

tst = TST.DFToMultiTSTransformator()
df_timeseries = tst.fit(df_triplet, ATTRS_TRIPLET[0], ATTRS_TRIPLET[1], ATTRS_TRIPLET[2])

# ## Data Basic Exploration

# Both DataFrames (Triplet, Timeseries) are explored:

dfe = DFE.DFExplorer()
dfs = {"TRPLT": df_triplet, "TMSRS": df_timeseries}
for name in dfs.keys():
    df = dfs[name]
    print(f"========== Data frame for {name} DataFrame. ==========")
    dfe.print_info_about_data_frame(df)
    print("\n\n")  # TODO - Maybe modify Visualizer to plot tuples as ints?

# ## Saving Timeseries

tsl.save_timeseries(df_timeseries, TIMESERIES_NAME, ATTRS_TIMESERIES, WHERE_TO_STORE)

# ### Loading Timeseries

df_loaded = tsl.load_timeseries(TIMESERIES_NAME, ATTRS_TIMESERIES, WHERE_TO_STORE)

# ### Checking Saver and Loader

print(df_timeseries.equals(df_loaded))

# ## Final Timestamp

tr.set_final_timestamp()
