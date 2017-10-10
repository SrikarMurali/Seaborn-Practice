# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 17:35:09 2017

@author: Nathan
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

df = pd.read_csv('vgsales.csv', index_col=0, encoding = "ISO-8859-1")

#print(df.head())


smallerData = df[:500]
#sns.swarmplot(x='Genre', 
#              y='Global_Sales',
#              data=smallerData,
#              hue='Genre',
#              split=True)
#plt.figure(figsize=(20,10))
#sns.violinplot(x='Publisher',
#               y='Global_Sales',
#               data=smallerData,
#               hue='Publisher',
#               inner=None)
#plt.ylim(0, 30)
#plt.xlim(0, None)
#plt.legend(bbox_to_anchor=(1,1), loc=2)
#plt.xticks(rotation=45)

#g = sns.factorplot(x='Year',
#                   y='Global_Sales',
#                   data=smallerData,
#                   hue='Publisher',
#                   col='Publisher',
#                   kind='swarm')
#
#g.set_xticklabels(rotation=45)

#corr = smallerData.corr()
#
#sns.heatmap(corr)

sns.swarmplot(x='Publisher', 
              y='Year',
              data=smallerData,
              hue='Genre',
              split=True)

plt.legend(bbox_to_anchor=(1,1), loc=2)
plt.xticks(rotation=45)
