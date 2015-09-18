# -*- coding: utf-8 -*-
"""
Identify rows from data table based on values being outside outlier cut-offs
by Praveen Taneja praveen.taneja@gmail.com
"""
#print(__doc__)

import datetime
import pandas as pd
#import itertools
#import math
import sys
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'EclipseIDEWorkSpace/pt_PyUtilsDir')
import pt_PyUtils
import os
import imp
imp.reload(pt_PyUtils)

###################################################

#######Start - Variables to be edited by user #####

# Path for input data file without file suffix

times_IQR = 2.0 

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

med =  df.median()
lower_q = df.quantile(q = 0.25)
upper_q = df.quantile(q = 0.75)

iqr = upper_q - lower_q

upper_cutoff = upper_q + times_IQR*iqr
lower_cutoff = lower_q - times_IQR*iqr

#print lower_q
#print upper_q
#print iqr

all_cols = lower_q.index.values # get col names

for col in all_cols:
    # print cellname and outlier value
    print col, lower_cutoff[col], upper_cutoff[col]
    for idx, val in zip(df.index, df[col]):
        if val < lower_cutoff[col] or val > upper_cutoff[col]:
            print 'outlier...',df[col_with_row_id][idx],val
    print ' '
