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

# ### Concat

import pandas as pd


# +
# pd.concat?

# +
s1 = pd.Series(['a', 'b'])
s2 = pd.Series(['c', 'd'])

s1
# -

pd.concat([s1, s2])

pd.concat([s1, s2], ignore_index=True)

pd.concat([s1, s2], keys=['s1', 's2'], names=['Series name', 'Row ID'])

df1 = pd.DataFrame([['a', 1], ['b', 2]], columns=['letter', 'number'])
df1

df2 = pd.DataFrame([['c', 3], ['d', 4]], columns=['letter', 'number'])
df2

pd.concat([df1, df2])

df3 = pd.DataFrame([['c', 3, 'cat'], ['d', 4, 'dog']], columns=['letter', 'number', 'animal'])
df3

pd.concat([df1, df3], sort=False)

pd.concat([df1, df3], sort=False, join='inner')

pd.concat([df1, df3], sort=False, join='outer')

df4 = pd.DataFrame([['bird', 'polly'], ['monkey', 'george']], columns=['animal', 'name'])
df4

pd.concat([df1, df4], sort=False)

pd.concat([df1, df4], sort=False, axis=1)

df5 = pd.DataFrame([1], index=['a'])
df5

df6 = pd.DataFrame([2], index=['a'])
df6

pd.concat([df5, df6], verify_integrity=True)    # verify_integrity 옵션 사용 시, 중복 값 등 유효성 검사를 함


