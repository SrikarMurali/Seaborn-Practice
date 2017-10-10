# -*- coding: utf-8 -*-
"""
Created on Wed Aug  9 15:42:33 2017

@author: Nathan
"""

import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sns

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
df = pd.read_csv('Pokemon.csv', index_col=0, encoding = "ISO-8859-1")
#print(df.head())

#sns.lmplot(x='Attack', y='Defense', data=df, 
#           fit_reg=False, 
#           hue='Stage')

#plt.ylim(0, None)
#plt.xlim(0, None)

stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
#sns.boxplot(data=stats_df)

sns.set_style('whitegrid')

#sns.violinplot(x='Type 1', y='Attack', data=df,
#               palette=pkmn_type_colors)

#sns.swarmplot(x='Type 1', y='Attack', data=stats_df,
#              palette=pkmn_type_colors)

#plt.figure(figsize=(10,6))
#
sns.violinplot(x='Type 1',
               y='Attack',
               data=df,
               inner=None,
               palette=pkmn_type_colors)

sns.swarmplot(x='Type 1',
              y='Attack',
              data=df,
              color='k',
              alpha=0.7)

plt.title('Attack by Type')
s = 'cat'
print(s[-1])
#print(stats_df.head())
#
#melted_df = pd.melt(stats_df,
#                    id_vars = ["Name", "Type 1", "Type 2"],
#                    var_name="Stat")
#
#print(melted_df.head())
#
#print(stats_df.shape)
#print(melted_df.shape)
#
#sns.swarmplot(x='Stat', 
#              y='value', 
#              data=melted_df,
#              hue = 'Type 1',
#              split=True,
#              palette=pkmn_type_colors)
#
#plt.ylim(0,260)
#plt.legend(bbox_to_anchor=(1,1), loc=2)
#
#corr = stats_df.corr()
#
##sns.heatmap(corr)
#
##sns.distplot(df.Attack)
#
##sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
##
##plt.xticks(rotation=45)
#
##g = sns.factorplot(x='Type 1',
##                   y='Attack',
##                   data=df,
##                   hue='Stage',
##                   col='Stage',
##                   kind='swarm')
##
##g.set_xticklabels(rotation=45)
#
##sns.kdeplot(df.Attack, df.Defense)
#
##sns.jointplot(x='Attack', y='Defense', data=df)