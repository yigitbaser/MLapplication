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

# # Testing Histogram

# # ---- GENERAL SETTINGS ----

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

from importlib import reload

# ### Personal Libraries

import src.Data.TimeSeriesGenerator as G
import src.Visualization.Visualization as V
import src.Transformation.DFLogTransformator as L

reload(G)
reload(V)

visu = V.Visualizer()
tsg = G.TimeSeriesGenerator()
lgthm = L.DFLogTransformator()


# ### Constants

from src.GlobalConstants import ATTR_ID, ATTR_VALUE

NUMBER_BINS = 5
BASE_LOG = 10


# # ---- TESTING DATAFRAME ----

def _get_df():
    df = tsg.generate_sample_triplet_df(None, True)
    return df


df_in = _get_df()

# The shape of the DataFrame is:

df_in.shape

# and an initial display of it:

df_in.head()

# # ---- TRANSFORMATORS ----



# # ---- PLOTS ----

# ### Histogram

# No log applied

visu.create_plotly_histogram_chart(
    df=df_in,
    name_category_attr=ATTR_VALUE,
    bins=NUMBER_BINS,
    log_x_data=False,
    log_y_axis=False,
    log_base=BASE_LOG
)

# log applied

visu.create_plotly_histogram_chart(
    df=df_in,
    name_category_attr=ATTR_VALUE,
    bins=NUMBER_BINS,
    log_x_data=True,
    log_y_axis=False,
    log_base=BASE_LOG
)

# ### Bar Chart

df_in = _get_df()

# No log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    name_value_attr=ATTR_VALUE,
    log_y_data=False,
    log_y_axis=False,
    log_base=BASE_LOG
)

# log applied

visu.create_plotly_bar_chart(
    df=df_in,
    name_category_attr=ATTR_ID,
    name_value_attr=ATTR_VALUE,
    log_y_data=True,
    log_y_axis=True,
    log_base=BASE_LOG
)

# ## Final Timestamp

tr.set_final_timestamp()
