# -*- coding: utf-8 -*-
"""
Remove rows from data table based on values being outside the specified range
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
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "/Users/taneja/OneDrive/ProGran_FullKO_NucAccumbens_Grietje/pt_ProGran_FullKO_NucAccumbens_10_28_14"
#indatafile = "C:\Users\praveen.taneja.GLADSTONE\Dropbox\Analysis\python_progs\python_data_analysis\pt_Dravet_FI_L5A_SubsetFI_AnalysisNPooled_AddAnalysis_out"
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\\Users\\praveen.taneja\\OneDrive\\ProGran_FullKO_NucAccumbens_Grietje\\Analysis01_14_15\\pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled01_14_15_NoOL"
#indatafile = "H:\\Core Labs\\Electrophysiology\\PraveenT\\MuckeLab\\CaPermAmpa\\AmpaDecayTauCoef_long"
#indatafile  = "C:/Users/praveen.taneja/Copy/ProGran_FullKO_NucAccumbens_Grietje/Analysis03_30_15/pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled03_30_15"
#indatafile  = "/Users/taneja/Work/ProGran_FullKO_NucAccumbens_Grietje/Analysis_05_08_15/pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled05_08_15Unblinded_NoRsOL"
#indatafile  = '\\gdsl.gladstone.internal\\gdsl\\Core Labs\\Electrophysiology\\PraveenT\\GanLab\\ProGran_FullKO_NucAccumbens_Grietje\\Analysis_05_08_15\\pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled05_08_15Unblinded_NoRsOL'
#Input file suffix
#suffix = ".csv"

outlier_minmax = []
# syntax outlier_minmax.append(['RsAvg', 0, 20e6])
#outlier_minmax.append(['AvgFreq250pA', 0.0, 70.0])
#outlier_minmax.append(['InstFreq250pA', 0, 100.0])
#outlier_minmax.append(['AdaptR400pA', 0, 1.0])
#outlier_minmax.append(['PeakAmp_1Spk400pA', 30.0e-3, 1.0e3])
#outlier_minmax.append(['Fwhm_1Spk400pA', 0, 2.0e-3])
#outlier_minmax.append(['RsAvg', 0, 30.0e6])
outlier_minmax.append(['RInAvg', 0, 430.0e6])
#outlier_minmax.append(['InstFreq400pA', 0, 120.0])
#outlier_minmax.append(['FI_Slope', 0.2e11, 3.0e11])
#outlier_minmax.append(['FI_MaxFreq', 10, 1000.0])
#outlier_minmax.append(['Ahp_1Spk250pA', -20e-3, 0])
#outlier_minmax.append(['data', 0.0, 20.e-3])



# output values for rows from following column if there is an outlier
#col_with_row_id = 'names'
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
    # create a column par_name + '_OL' which is one if par_name is OL, else zero
    # use bitwise '|' because we are comparing a sequence of booleans with 
    # another sequence of booleans.
    #x = 1*( (df[par_name] < min_val) | (df[par_name] > max_val) )
    #df_out[''.join([par_name, '_OL'])] = x
    n = len(df[par_name].index)
    for idx, val in zip(df.index, df[par_name]):
        if val < min_val or val > max_val:
            print 'outlier...',df[col_with_row_id][idx],val
            
       

#df_out.to_csv(outdatafile)
#print 'values saved to', outdatafile+".csv"