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

# ## Reshaping Data (1)

import pandas as pd
import seaborn as sns

df = sns.load_dataset('mpg')
df.shape

df.head()

# +
# df.sort_values?
# -

df.sort_values('mpg', ascending=False).head()

df.rename(columns={'model_year' : 'years'}).sort_values('years', ascending=False).head()

# +
# df.reset_index?
# -

df.reset_index().head()

df.drop(columns=['mpg', 'weight']).head()

# ## Reshaping Data (2)

# ### Melt

# +
# pd.melt?

# +
df2 = pd.DataFrame({'A': {0: 'a', 1: 'b', 2: 'c'},
                   'B': {0: 1, 1: 3, 2: 5},
                   'C': {0: 2, 1: 4, 2: 6}})

df2
# -

pd.melt(df2, id_vars=['A'], value_vars=['B'])

pd.melt(df2, id_vars=['A'], value_vars=['B','C'])

pd.melt(df2, value_vars=['A','B','C'])

pd.melt(df2, value_vars=['A','B','C']).rename(columns={'variable' : 'var', 'value' : 'val'})

# ### Pivot

# +
# df2.pivot?
# -

df3 = pd.DataFrame({'foo': ['one', 'one', 'one', 'two', 'two', 'two'],
                   'bar': ['A', 'B', 'C', 'A', 'B', 'C'],
                   'baz': [1, 2, 3, 4, 5, 6],
                   'zoo': ['x', 'y', 'z', 'q', 'w', 't']})
df3

df3.pivot(index='foo', columns='bar', values='baz')

df3.pivot(index='foo', columns='bar')['baz']

df4 = df3.pivot(index='foo', columns='bar', values='baz').reset_index()
df4

# +
# pd.melt?
# -

pd.melt(df4, id_vars=['foo'], value_vars=['A','B','C'])

pd.melt(df4, id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo', 'bar'])

pd.melt(df4, id_vars=['foo'], value_vars=['A','B','C']).sort_values(['foo', 'bar']).rename(columns={'value':'baz'})


