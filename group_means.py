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
'''
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'python_data_analysis/cluster_analysis/cluster_analysis_git')
'''                
sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/'
                'EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/'
                'python_data_analysis/cluster_analysis/cluster_analysis_git')                
import dataframe_utils
import pt_PyUtils
import imp
import os
imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)
#import plot_dataframe_means

###################################################

#######Start - Variables to be edited by user #####
# number of levels in enclosing group or final group(if there is only one group)
colors = ['magenta', 'blue', 'green', 'red']
#colors = ['green', 'blue', 'orange', 'red'] 
#######End - Variables to be edited by user #######
###################################################


data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]


groupby_list = pt_PyUtils.ask(message ='Enter grouping factors (eg. GT Gender)')
groupby_list = groupby_list.split(' ')
print 'Group by:', groupby_list

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="

out_data_file = data_file_no_ext + "_means"


# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')
print df.head(2)

dataframe_utils.group_means(df, groupby_list, out_data_file, display_raw = False
                            , autoscale = False, colors = colors)