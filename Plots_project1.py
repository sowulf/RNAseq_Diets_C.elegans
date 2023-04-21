#!/usr/bin/env python3
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df_data = pd.read_csv('/Users/sophie.wulf/Desktop/Python_course/ project_1/analyzed_data.csv', sep = ',')

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
plt.text(-4.5, -4.5, 'low', fontdict=None, color = 'blue')

plt.savefig('figure_project1.pdf')
plt.show()
