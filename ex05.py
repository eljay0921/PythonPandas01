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

# ## Make New Columns

import pandas as pd
import numpy as np

df = pd.DataFrame()

# ## Assign

# +
# df.assign?
# -

df = pd.DataFrame({'A': range(1, 11), 'B': np.random.randn(10)})
df

df.assign(ln_A = lambda x: np.log(x.A))

df.assign(AxB = lambda x: x.A * x.B)

df['AxB'] = df['A'] * df['B']
df

# ## QCut

# +
# pd.qcut?
# -

pd.qcut(range(5), 4)    # 4개의 구간(bucket)으로 나눈다

pd.qcut(range(5), 3, labels=["good", "medium", "bad"])    # 3개의 bucket으로 만든다 (label을 지정)

pd.qcut(df.A, 3, labels=['good', 'medium', 'bad'])

pd.qcut(df['AxB'], 3, labels=['good', 'medium', 'bad'])

# ## Max, Clip, Abs

df.max(axis=1)

df.max(axis=0)

df['B'].clip(lower=-1, upper=1)

df['B'].abs()

df.loc[:,:].abs()


