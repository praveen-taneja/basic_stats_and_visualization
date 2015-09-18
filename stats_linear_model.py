# -*- coding: utf-8 -*-
"""
by Praveen Taneja praveen.taneja@gmail.com
"""
#print(__doc__)

import datetime
import matplotlib.pyplot as pl
import pandas as pd
import statsmodels.api as sm
from patsy import dmatrices
import statsmodels.sandbox.stats.multicomp as multicomp
import sys
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/'
                'python_data_analysis/cluster_analysis/cluster_analysis_git')
import pt_PyUtils
import dataframe_utils
import imp
import os

imp.reload(pt_PyUtils)
imp.reload(dataframe_utils)

###################################################

#######Start - Variables to be edited by user #####

factor_name = 'GT'

# for now the following has to be altered in the code below
# 1. data filtering based on any conditon(s)
# 2. Model formula to fit
#######End - Variables to be edited by user #######
###################################################

data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="


# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')

col_names_numeric = dataframe_utils.numeric_cols(df)

df1 = df.copy()
# filter data set if needed
#df1 = df1[df1['Gender'] == 'm']
#df1 = df1[df1['start_time_sec'] <= 240] # 240, 360, 540

#print df1['start_time_sec'].head(40)

par_vals = []

for col in col_names_numeric:
    formula = ' '.join([col, '~', 
                    'C(',factor_name, ',Treatment(reference = \'I5A+\'))'])
    #print formula
    y, X = dmatrices(formula, data=df1, return_type='dataframe')
    mod = sm.OLS(y, X)    # Describe model
    res = mod.fit()       # Fit model
    print res.summary()  # Summarize model
    # use dir(res) to see all results that are available
    # correct for multiple comparisons
    # 1st p-value is for reference level and is removed
    p_corr = multicomp.multipletests(res.pvalues.values[1:], method = 'holm')
    print 'Uncorrected p-values:', res.pvalues
    print 'Corrected p-values:', p_corr[1]
    par_vals.append([col, res.df_resid, res.rsquared_adj, res.f_pvalue] +
                    list(res.pvalues.values[1:])+ list(p_corr[1]))


df_out = pd.DataFrame(par_vals, columns = ['par_name', 'deg_free', 'r_sq_adj',
                    'p_val', 'p_J20A_I5A', 'p_NTG_I5A', 'p_adj_J20A_I5A', 'p_adj_NTG_I5A'])
df_out = df_out.sort(columns = ['p_val']) # sort by p-values
data_file_no_ext = os.path.splitext(data_file)[0]
df_out.to_csv(data_file_no_ext + '_5minRefI5A_stats.csv',index = False)
            


