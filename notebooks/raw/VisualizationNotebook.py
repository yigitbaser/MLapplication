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

# # Visualization Notebook

# # ---- GENERAL SETTINGS ----

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

import src.Utils.Timerer as T

tr = T.Timerer()
tr.set_initial_timestamp()

# ### General Libraries

import pandas as pd
from importlib import reload

# ### Personal Libraries

import src.Data.TimeSeriesGenerator as G
import src.Visualization.Visualization as V

reload(G)
reload(V)

visu = V.Visualizer()
tsg = G.TimeSeriesGenerator()

# ### Notebook Settings

pd.options.display.max_rows = 500
pd.options.display.max_columns = 50

# ### Constants

from src.GlobalConstants import ATTR_ID, ATTR_VALUE

NUMBER_BINS = 5
BASE_LOG = 10


# # ---- ANALYSIS ----

# By making use of the already existing Data generators, we generate a Data Frame for testing.

def _get_df():
    df = tsg.generate_sample_triplet_df(None, True)
    return df


df_in = _get_df()

# The shape of the DataFrame is:

df_in.shape

# and an initial display of it:

df_in.head()

# ## Chart Plotting

# We are going to create three plots using the same DataFrame. But first a brief explanation of Visualization.py:
# - Histogram: Takes a column of a DataFrame and groups by name_category_column
# - Bar Chart: Takes two columns of a DataFrame and plots them by adding the name_value_column per name_category_column
#   - if only one column is provided (name_category_column) it will
#   create a count histogram with bin = unique name_category_column

# ### Histogram

# #### No log applied

visu.create_plotly_histogram_chart(
    df=df_in,
    name_category_attr=ATTR_VALUE,
    bins=NUMBER_BINS,
    log_x_data=False,
    log_y_axis=False,
    log_base=BASE_LOG
)

# #### log applied

visu.create_plotly_histogram_chart(
    df=df_in,
    name_category_attr=ATTR_VALUE,
    bins=NUMBER_BINS,
    log_x_data=True,
    log_y_axis=False,
    log_base=BASE_LOG
)

# ### Bar Chart with two columns as input


df_in = _get_df()

# #### No log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    name_value_attr=ATTR_VALUE,
    log_y_data=False,
    log_y_axis=False,
    log_base=BASE_LOG
)

# #### log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    name_value_attr=ATTR_VALUE,
    log_y_data=True,
    log_y_axis=True,
    log_base=BASE_LOG
)

# ### Bar chart with one column as input

df_in = _get_df()

# In this case, the class Visualizer creates a new count column which plots in the y axis. By not
# setting the value of name_value_column, it will take the predefined value of None and perform
# the count. Please see Visualization.py for more details.

# #### No log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    log_y_data=False,
    log_y_axis=False,
    log_base=BASE_LOG
)

# #### log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    log_y_data=True,
    log_y_axis=True,
    log_base=BASE_LOG
)

# ## Final Timestamp

tr.set_final_timestamp()
