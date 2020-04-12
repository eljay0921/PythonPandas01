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

# ## 여러가지 선언 방법

# +
import pandas as pd

df = pd.DataFrame(
    {"a" : [4 ,5, 6],
    "b" : [7, 8, 9],
    "c" : [10, 11, 12]}, index = [1, 2, 3])

df
# -

df.loc[2]

df.loc[2, 'a']

df.loc[[1,3], ['a', 'c']]

# +
df = pd.DataFrame(
    [
        [4, 7, 10], 
         [5, 8, 11],
         [6, 9, 12]
    ],
    index=[1, 2, 3], 
    columns=['a', 'b', 'c'])

df

# +
df = pd.DataFrame(
    { 
        "a" : [4,5,6,6],
        "b" : [7,8,9,9],
        "c" : [10,11,12,12]
    },
    index=pd.MultiIndex.from_tuples(
        [
            ('d', 1),
            ('d', 2),
            ('e', 2),
            ('e', 3)
        ],
        names=['n', 'v']
    )
)

df
# -

# ## 조건으로 색인

df[df.b > 7]

df.b > 7

# ## 중복 제거

df.drop_duplicates()
df
# 이후 df를 다시 확인해보면 중복 제거 전 데이터가 그대로 있음.
# df.drop_duplicates(inplace=True) # 권장하지 않는 방법.
# => df = df.drop_duplicates 로 변수에 담자.

df = df.drop_duplicates(keep='first')  # 중복된 값 중, 첫번째 항목을 남긴다 (last : 마지막 항목을 남긴다)
df

# ## 논리 연산

df[df.b != 8]

df[df['a'].isin([5,6])]

# +
import numpy as np

df = pd.DataFrame(
    { 
        "a" : [4,5,6,6,np.nan],
        "b" : [7,np.nan,8,9,9],
        "c" : [10,11,12,np.nan,12]
    },
    index=pd.MultiIndex.from_tuples(
        [
            ('d', 1),
            ('d', 2),
            ('e', 2),
            ('e', 3),
            ('e', 4)
        ],
        names=['n', 'v']
    )
)

df
# -

pd.isnull(df)

df[df['b'].isnull()]

pd.notnull(df)

df[df['a'].notnull()]

df[df['a'].notnull()].sum()

df[df['a'] == 5] & df[df['b'] == 7]

# ## Head, Tail

df.tail(3)

# ## Sampling

df.sample(frac=0.5)    # 임의의 순서로 특정 비율로 샘플링하는 방법, frac=1 이면 전부 가져옴

df.sample(n=3)    # 임의의 순서로 특정 갯수(n)만큼 샘플링

df.iloc[:4]

df.iloc[2:4]

df.iloc[-1:]

# +
# df.iloc?

# +
# df.nlargest?
# -

# ## nlargest, nsmallest

df.nlargest(3, 'c', keep='last')

df.nsmallest(2, 'b')
