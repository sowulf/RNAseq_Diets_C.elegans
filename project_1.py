#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#https://www.ebi.ac.uk/gxa/experiments/E-MTAB-8164/Downloads
df_data = pd.read_csv('/Users/sophie.wulf/Desktop/Python_course/ project_1/E-MTAB-8164-raw-counts.tsv', sep = '\t')

#OP50: ERR3452815/16/17(E.coli); OP50 & PXN21: ERR3452818/19/20; PXN21: ERR3452821/22/23
#OP50 & PXN21 represents control group
#calculate mean for each group
df_data.loc[:,'OP50'] = df_data.loc[:,['ERR3452815', 'ERR3452816', 'ERR3452817']].mean(axis = 1)
df_data.loc[:,'OP50_PXN21'] = df_data.loc[:,['ERR3452818', 'ERR3452819', 'ERR3452820']].mean(axis = 1)
df_data.loc[:,'PXN21'] = df_data.loc[:,['ERR3452821', 'ERR3452822', 'ERR3452823']].mean(axis = 1)

#calculate log2 fold changes between treatments and control group
df_data.loc[:,'OP50_vs_OP50&PXN21'] = np.log2(df_data.loc[:,'OP50'])/((df_data.loc[:,'OP50_PXN21']))
df_data.loc[:,'PXN21_vs_OP50&PXN21'] = np.log2(df_data.loc[:,'PXN21'])/(df_data.loc[:,'OP50_PXN21'])
df_data.replace([np.inf, -np.inf], np.nan , inplace=True)

#setting threshold for Log2 scale: Log2>2 up, Log2<-2 down, Log2 between 2 and -2 none and safe it in new column
for row, col in df_data.iterrows():
    if col["OP50_vs_OP50&PXN21"]  > 2:
        df_data.loc[row, "change_0P50"] = "up"
    elif col["OP50_vs_OP50&PXN21"]  < -2:
        df_data.loc[row, "change_0P50"] = "down"
    else:
        df_data.loc[row, "change_0P50"] = "none"

for row, col in df_data.iterrows():
    if col["PXN21_vs_OP50&PXN21"]  > 2:
        df_data.loc[row, "change_PXN21"] = "up"
    elif col["PXN21_vs_OP50&PXN21"]  < -2:
        df_data.loc[row, "change_PXN21"] = "down"
    else:
        df_data.loc[row, "change_PXN21"] = "none"

#safe analyzed data in new file
df_data.to_csv('/Users/sophie.wulf/Desktop/Python_course/ project_1/analyzed_data.csv')

#plot results in scatter plot
plt.scatter(df_data.loc[:,'OP50_vs_OP50&PXN21'], df_data.loc[:,'PXN21_vs_OP50&PXN21'], s = 1)
plt.ylabel('PXN21_vs_OP50&PXN21')
plt.xlabel('OP50_vs_OP50&PXN21')
plt.title('RNAseq of C. elegans fed on different bacterial diets')

#add lines in plot to see which
plt.axvline(x = 2, color = 'green', linewidth = 0.8)
plt.axhline(y = 2, color = 'green', linewidth = 0.8)
plt.axvline(x = -2, color = 'blue', linewidth = 0.8)
plt.axhline(y = -2, color = 'blue', linewidth = 0.8)

#add labels for high and low counts
plt.text(9, 12.5, 'high', fontdict=None, color = 'green')
plt.text(-4.5, -4.5, 'down', fontdict=None, color = 'blue')

plt.savefig('figure_project1.pdf')
plt.show()
