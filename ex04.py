# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Handling Missing Data

import pandas as pd
import seaborn as sns
import numpy as np

df = pd.DataFrame(
    [
        [np.nan, 2, np.nan, 0],
        [3, 4, np.nan, 1],
        [np.nan, np.nan, np.nan, 5]
    ],
    columns=list('ABCD')
)

df

# ## Dropna

# +
# df.dropna?
# -

df.dropna(axis=1, how='all')    # axis=1 (column 기준), how='all' (전부 NaN일 때) 예외

df.dropna(axis=1, how='any')    # axis=1 (column 기준), how='any' (하나라도 NaN이 있으면) 예외

df.dropna(axis=0, how='all')    # axis=0 (row 기준), how='all' (전부 NaN일 때) 예외

df.dropna(axis=0, how='any')    # axis=0 (row 기준), how='any' (하나라도 NaN이 있으면) 예외

# ## Fillna

# +
# df.fillna?
# -

df.fillna(0)

values = {'A' : 0, 'B' : 1, 'C' : 'C', 'D' : 3}
df.fillna(value=values)

fill_na = df['B'].mean()
fill_na

df.fillna(fill_na)

df.isnull()

df.isnull().sum()

df.notnull().sum()


