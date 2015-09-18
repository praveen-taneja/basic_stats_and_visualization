# -*- coding: utf-8 -*-
"""
by Praveen Taneja praveen.taneja@gmail.com
"""
#print(__doc__)

import datetime
import matplotlib.pyplot as pl
import pandas as pd
#import itertools
#import math
import sys
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
#sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
import dataframe_utils
import pt_PyUtils
import os
import imp
imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)
#import plot_dataframe_means

###################################################

#######Start - Variables to be edited by user #####

# Path for input data file without file suffix
#indatafile  = "C:/Users/praveen.taneja/Copy/BD_DravetData/FI data/05_01_15/150120_AnalysisAllParam_for Praveen_p17to30_DOnly"
subtract_group_mean = False
#Input file suffix
#suffix = ".csv"

graphs_per_plot = 4

#groupby_list = []


#######End - Variables to be edited by user #######
###################################################

data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

groupby_list = pt_PyUtils.ask(message = 'Enter grouping factors (eg. GT Gender)')
groupby_list = groupby_list.split(' ')
print 'Group by:', groupby_list

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="

out_data_file = data_file_no_ext + "_means"
out_data_file_singles = data_file + "_column_plots.pdf"
out_data_file_pairs = data_file + "_pair_plots.pdf"
#outdatafile = data_file + "_out"+suffix

# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')

dataframe_utils.column_plots(df, ",", out_data_file_singles, graphs_per_plot = 4)

df1 = df.copy()
if subtract_group_mean:
    df1 = df1.groupby(groupby_list).transform(lambda x: x - x.mean())
    print 'length df', len(df1)
    
dataframe_utils.pair_plots(df1, ",", out_data_file_pairs, graphs_per_plot = 4)

if subtract_group_mean:
    
    print 'Subtracted means for scatter plots...'

