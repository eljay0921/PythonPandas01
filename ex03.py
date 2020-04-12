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

# ## Summarize Data

import pandas as pd
import seaborn as sns
import numpy as np

df = sns.load_dataset('iris')
df.shape

df.shape[0]    # == len(df)

df.head()

df['species'].value_counts()

df['species'].nunique()

df['sepal_length'].sum()

df['sepal_length'].max()

df['petal_length'].median()    # 중간 값

df.median()    # 중간 값

df['petal_length'].mean()    # 평균 값

df.mean()    # 평균 값

df.var()    # 분산

df.std()    # 표준편차

df.quantile([0.25, 0.30, 0.50, 1.00])    # 각 퍼센트? 의 값 => 50% 중간 값, 100% 최대 값

df.loc[:, ['sepal_length', 'petal_length']].quantile([0.25, 0.30, 0.50, 1.00])

df.loc[50:100, ['sepal_length', 'petal_length']].quantile([0.25, 0.30, 0.50, 1.00])

# ## Describe

# +
# df.describe?
# -

df.describe()

df.describe(include='all')

df.describe(exclude=[np.object])

df['sepal_width'].describe()

df['species'].describe()

# ## Apply (function)

# +
# df.apply?
# -

df.head()

df.apply(lambda x : x[0])

df['species'].apply(lambda x: x[0]).head()


def sample_last_3(x) : 
    x = x[-3:]
    return x


df['species_first_3'] = df['species'].apply(lambda x: x[:3])

df['species_last_3'] = df['species'].apply(sample_last_3)

df


