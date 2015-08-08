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
import dataframe_utils
import imp
imp.reload(dataframe_utils)
#import plot_dataframe_means

###################################################

#######Start - Variables to be edited by user #####

# Path for input data file without file suffix
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "H:\Core Labs\Electrophysiology\PraveenT\GanLab\ProGran_FullKO_NucAccumbens_Grietje/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\Users\praveen.taneja.GLADSTONE\Dropbox\Analysis\python_progs\python_data_analysis\pt_Dravet_FI_L5A_SubsetFI_AnalysisNPooled_AddAnalysis_out"
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\\Users\\praveen.taneja\\OneDrive\\ProGran_FullKO_NucAccumbens_Grietje\\pt_ProGran_FullKO_NucAccumbens_11_16_14_no_outliers"
#indatafile = "C:\Users\praveen.taneja\OneDrive\python_data_analysis\ExcitNInhibPairs\corr_peak_vals_in_5ms"
indatafile = "H:\\Core Labs\\Electrophysiology\\PraveenT\\MuckeLab\\CaPermAmpa\\AmpaDecayTauSigma"

#Input file suffix
suffix = ".csv"

#######End - Variables to be edited by user #######
###################################################

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="

outdatafile = indatafile + "_long.csv"


# read actual user dataset 
df = pd.read_table(indatafile+suffix, delimiter = ',')
df_out = dataframe_utils.cols_to_long(df)
df_out.to_csv(outdatafile)