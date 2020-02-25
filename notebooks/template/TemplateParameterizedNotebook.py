# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
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

# # Template Parameterized Notebook

# [papermill](https://github.com/nteract/papermill)

# ## Imports

import matplotlib.pyplot as plt
# %matplotlib inline

# ## Parameters
#
# To create a parametrized notebook, add tag parameters to the cell with variables you want to modify (jupyter notebook environment View/Cell Toolbar/Tags, does not work with jupyter lab now). Values in this cell will be considered default values. If a notebook will be run without the tagged cell, specified parameters will be added as a separate cell at the top of the notebook.

# + {"tags": ["parameters"]}
n = 10
a = 1
b = 0
# -

# ## Data

X = list(range(1, n+1))
Y = [a*x + b for x in X]

# ## Plotting

plt.plot(X, Y, "r.")
