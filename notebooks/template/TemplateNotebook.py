# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # NotebookTemplate

# *PLACE FOR COMMENTS*

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
sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(), os.pardir))) # one up
sys.path.insert(0,os.path.abspath(os.path.join(os.getcwd(),"../..")))    # two up

# ### Initial Timestamp

import src.Utils.Timerer as T

tr = T.Timerer()
tr.set_initial_timestamp()

# ### General Libraries

# +
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from importlib import reload

# %matplotlib notebook
# -

# ### Personal Libraries

# Personal libraries, classes, functions from repo itself



# ### Notebook Settings

# Notebook settings.

pd.options.display.max_rows = 500
pd.options.display.max_columns = 50

# Constants (please use all letter upper), ...

from src.GlobalConstants import *  # Remember to import only the constants in use

# # ANALYSIS ---------------------------------------------------------

# ## Chapter



# ### Sub-Chapter



# ## Final Timestamp

tr.set_final_timestamp()
