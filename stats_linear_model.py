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
import sys
#sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/python_data_analysis/cluster_analysis/cluster_analysis_git')

#import dataframe_utils
import pt_PyUtils
import imp
import os
#imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)
#import plot_dataframe_means

###################################################

#######Start - Variables to be edited by user #####

# Path for input data file without file suffix
#indatafile = "/Users/taneja/Work/Dravet/pt_Dravet_FI_L5A_SubsetFI_AnalysisNPooled_AddAnalysis_Subset"
#indatafile = "C:\\Users\\praveen.taneja\\OneDrive\\ProGran_FullKO_NucAccumbens_Grietje\\Analysis01_14_15\\pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled01_14_15_NoOL_less_cols"
#indatafile = "C:\Users\praveen.taneja.GLADSTONE\Dropbox\Analysis\python_progs\python_data_analysis\pt_Dravet_FI_L5A_SubsetFI_AnalysisNPooled_AddAnalysis_out"
#indatafile = "/Users/taneja/Dropbox/Analysis/python_progs/python_data_analysis/stats/Reducing variability by including other explanatory variables"
#indatafile = "C:\Users\praveen.taneja\Dropbox\Analysis\stats\Reducing variability by including other explanatory variables"
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\Users\praveen.taneja\Dropbox\Analysis\stats\Reducing variability by including other explanatory variables"
#Input file suffix
#indatafile  = "H:\\Core Labs\\Electrophysiology\\PraveenT\\MuckeLab\\CaPermAmpa\\AmpaDecayTauCoef_long_no_outliers_means_with_gt"
#indatafile  = "C:/Users/taneja/Work/sumihiro/150213_hTau_20mo_RawData_Slopes"
#suffix = ".csv"

#######End - Variables to be edited by user #######
###################################################

data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="

#outdatafile = indatafile + "_means"

# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')
#print df.head()
#vars = ["AvgFreq400pA", "GT", "RInAvg"]
#df = df[vars]
#print df.head(3)
#sys.exit()
#pl.plot(df["CmAvg"], df["AvgFreq700pA"], marker = "o", linestyle = "")
#Weight gender   Height  Weight_wH
# GT  Age Gender  AvgFreq400pA  InstFreq400pA  SpkTrainAhp400pA
# AdaptR400pA  InstFreq_0Spk400pA  Ahp_0Spk400pA  PeakAmp_0Spk400pA
# Fwhm_0Spk400pA  VThresh_0Spk400pA  MaxDvDt_0Spk400pA  T2FracPeak_0Spk400pA
# RsAvg     RInAvg         CmAvg     FI_CurrTh      FI_Slope

#df["RInAvg"] *=1e-6

df1 = df.copy()
#df1 = df1[df1['Gender'] == 'm']
#print df1.head(40)


#y, X = dmatrices('Ahp_0Spk250pA ~ GT', data=df1, return_type='dataframe')
y, X = dmatrices('IFrqNormCm_MaxFreq ~ GT', data=df1, return_type='dataframe')
#print y[:3]
#print X[:3]
mod = sm.OLS(y, X)    # Describe model
res = mod.fit()       # Fit model
print res.summary()   # Summarize model
#pl.show()
