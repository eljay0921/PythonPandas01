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

# ## Merge

# +
import pandas as pd

adf = pd.DataFrame({'x1': ['A', 'B', 'C'],'x2': [1 , 2, 3] })
adf
# -

bdf = pd.DataFrame({'x1': ['A', 'B', 'D'],'x2': ['T', 'F', 'T'] })
bdf

pd.merge(adf, bdf, how='left', on='x1')    # sql의 join과 유사한것 같다

pd.merge(adf, bdf, how='right', on='x1')

pd.merge(adf, bdf, how='inner', on='x1')

pd.merge(adf, bdf, how='outer', on='x1')

bdf.x1    # bdf['x1'] 동일함

adf.x1.isin(bdf.x1)

adf[adf.x1.isin(bdf.x1)]

adf[~adf.x1.isin(bdf.x1)]    # 반대의 경우로 가져옴 (제외)

# --------------

# +
ydf = pd.DataFrame({
    "x1" : [ "A", "B", "C" ],
    "x2" : [ 1, 2, 3 ]
})

ydf

# +
zdf = pd.DataFrame({
    "x1" : [ "B", "C", "D" ],
    "x2" : [ 2, 3, 4 ]
})

zdf
# -

pd.merge(ydf, zdf)    # 기본 merge는 inner 다.

pd.merge(ydf, zdf, how='outer')

pd.merge(ydf, zdf, how='outer', indicator=True)

pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"')

pd.merge(ydf, zdf, how='outer', indicator=True).query('_merge == "left_only"').drop(columns=['_merge'])
