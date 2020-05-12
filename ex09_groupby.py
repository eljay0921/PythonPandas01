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

# +
import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')
df.head(10)
# -

# ## Groupby

# +
# df.groupby?
# -

df.groupby(by='origin').size()

df.origin.value_counts()    # df.groupby(by='origin').size() 동일함

df['origin'].value_counts()    # df.groupby(by='origin').size() 동일함

# ### min, max, mean

df.groupby(by='origin').min()

df.groupby(by='origin').max()

df.groupby(by='origin').mean()

df.groupby(by='origin')['horsepower', 'weight'].mean()

# ## Groupby multiple column

df.groupby(['model_year', 'origin'])['horsepower', 'weight'].max()

# ## Group Data - shift, rank, cum(~)

# +
df2 = pd.DataFrame( [[4, 9, 10], 
                     [5, 8, 20],
                     [6, 7, 12]],
                   index=[1, 2, 3], 
                   columns=['a', 'b', 'c'])

df2
# -

df2.shift(-1)

df2.shift(2)

df2['b'].shift(1)

df2.rank(method='dense')

df['model_year'].rank(method='max').value_counts()

df['model_year'].rank(method='first', pct=True).head(10)

df2

df2.cumsum()    # Cumulative Sum.

df2.cummax()    # Cumulative Max.

df2.cummin()

df2.cumprod()


