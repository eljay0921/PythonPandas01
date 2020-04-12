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

# ## Subset Variables (Columns)

import pandas as pd
import seaborn as sns

df = sns.load_dataset("iris")

df.head()

cols = ['sepal_width', 'sepal_length', 'species']
df[cols].head()

# ## Regex

df.filter(regex='^sepal').head(5)

df.filter(regex='length$').head()

df.filter(regex='^(?!species$).*').head()

# ## Location

df.loc[:,'sepal_length':'petal_length'].head()

df.loc[4:10,'petal_length':'petal_width']

df.iloc[4:10,[1,2,4]]

df.loc[df['sepal_width'] > 3.8, ['sepal_width', 'sepal_length']]
