# -*- coding: utf-8 -*-
"""
plot long form data is in the long form (example what is used by stats progs)

example:

0	100	Cell_0001	07_22_14 Folder:FI	NTG	LG86	112	350	m
0	150	Cell_0001	07_22_14 Folder:FI	NTG	LG86	112	350	m
11.1905	200	Cell_0001	07_22_14 Folder:FI	NTG	LG86	112	350	m
21.4692	250	Cell_0001	07_22_14 Folder:FI	NTG	LG86	112	350	m

    
by Praveen Taneja praveen.taneja@gmail.com
"""
#print(__doc__)

import pandas as pd
import matplotlib.pylab as pl
import numpy as np
import sys
#sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
import dataframe_utils
import pt_PyUtils
import imp
import os
imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)
#import plot_dataframe_means


#indatafile = 'H:\\Core Labs\\Electrophysiology\\PraveenT\\GanLab\\ProGran_FullKO_NucAccumbens_Grietje\\Analysis_05_08_15\\Export05_08_15Unblinded_NoRsRInOutliers_vs_currents\\Export05_08_15Unblinded_NoRsRInOutliers_InstFreq_long'

#indatafile = 'C:/Users/praveen.taneja/Copy/ProGran_FullKO_NucAccumbens_Grietje/05_08_15/mixed_effects_analysis/Export05_08_15Unblinded_NoRsRInOutliers_InstFreq_long_w_cohort_noc3'

#Input file suffix
#suffix = ".csv"


data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

groupby_list = pt_PyUtils.ask(message = 'Enter grouping factors (eg. GT Gender)')
groupby_list = groupby_list.split(' ')
print 'Group by:', groupby_list

df = pd.read_table(data_file, delimiter = ',')
print '$$$$$$$'
print df.head()
grouped = df.groupby(groupby_list)
print grouped

# average
for name, group in grouped:
    print name
    df_pivot = group.pivot(index = 'Currents', columns = 'CellName', values = 'InstFreq')
    #print df_pivot.head()    
    avg = df_pivot.mean(axis = 1)#.aggregate(np.mean)
    std = df_pivot.std(axis = 1)#.aggregate(np.std)
    size = df_pivot.count(axis = 1)#.aggregate(np.size)
    sem = std/np.sqrt(size)
    #print len(avg), len(sem)
    avg.plot(yerr = sem, label = name)
    pl.legend(loc = 'lower right', fontsize = 9)
    #pl.ylim()

# raw data
for name, group in grouped:
    print name
    df_pivot = group.pivot(index = 'Currents', columns = 'CellName', values = 'InstFreq')
    #print df_pivot.head()    
    #avg = df_pivot.mean(axis = 1)#.aggregate(np.mean)
    #std = df_pivot.std(axis = 1)#.aggregate(np.std)
    #size = df_pivot.count(axis = 1)#.aggregate(np.size)
    #sem = std/np.sqrt(size)
    #print len(avg), len(sem)
    df_pivot.plot(yerr = sem, label = name)
    pl.legend(loc = 'lower right', fontsize = 9)
    #pl.ylim()
pl.show()
#print df.head()
#df_pivot = df.pivot(index = 'Currents', columns = 'CellName')#, values = 'InstFreqAll')
#print df_pivot#.head()
#df_pivot.to_csv('C:\Users\praveen.taneja\OneDrive\ProGran_FullKO_NucAccumbens_Grietje\Analysis11_16_14\InstFreqWPars_pivot.csv')