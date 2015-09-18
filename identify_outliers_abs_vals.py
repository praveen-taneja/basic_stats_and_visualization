# -*- coding: utf-8 -*-
"""
Remove rows from data table based on values being outside the specified range
by Praveen Taneja praveen.taneja@gmail.com
"""
#print(__doc__)

import datetime
import pandas as pd
import sys
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'EclipseIDEWorkSpace/pt_PyUtilsDir')
#import dataframe_utils
import pt_PyUtils
import os
import imp
#imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)

###################################################

#######Start - Variables to be edited by user #####

outlier_minmax = []
outlier_minmax.append(['RInAvg', 0, 400.0e6])
remove_outliers = True
# output values for rows from following column if there is an outlier
col_with_row_id = 'CellName'

#######End - Variables to be edited by user #######
###################################################

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="


data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

#outdatafile = indatafile + "_outlier_id.csv"


# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')

print df.info()

df_out = pd.DataFrame()
for outlier in outlier_minmax:
    par_name = outlier[0]
    min_val = outlier[1]
    max_val = outlier[2]
    
    num_outliers = 0
    for idx, val in zip(df.index, df[par_name]):
        if val < min_val or val > max_val:
            num_outliers = num_outliers + 1
            print num_outliers, 'outlier...', df[col_with_row_id][idx],val
            
    if remove_outliers:
        print ' ' 
        print 'removing outliers for', par_name     
        df = df[(df[par_name] >= min_val) & (df[par_name] <= max_val)]   

if remove_outliers:
    df.to_csv(data_file, index = False)