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
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/python_data_analysis/cluster_analysis/cluster_analysis_git')
#sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
import dataframe_utils
import pt_PyUtils
import imp
import os
imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)
#import plot_dataframe_means

###################################################

#######Start - Variables to be edited by user #####

# Path for input data file without file suffix
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "H:\Core Labs\Electrophysiology\PraveenT\GanLab\ProGran_FullKO_NucAccumbens_Grietje/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\Users\praveen.taneja.GLADSTONE\Dropbox\Analysis\python_progs\python_data_analysis\pt_Dravet_FI_L5A_SubsetFI_AnalysisNPooled_AddAnalysis_out"
#indatafile = "/Users/taneja/Work/GanLab/pt_ProGran_FullKO_NucAccumbens_FIAnalysisAndPooled_400pA_LessCols"
#indatafile = "C:\\Users\\praveen.taneja\\OneDrive\\ProGran_FullKO_NucAccumbens_Grietje\\Analysis01_14_15\\pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled01_14_15_NoOL"
#indatafile = "C:\\Users\\praveen.taneja\\OneDrive\\TauTG_Sumihiro\\Spk0AHP170pA"
#indatafile = "/Users/taneja/OneDrive/ProGran_FullKO_NucAccumbens_Grietje/Analysis11_16_14/pt_ProGran_FullKO_NucAccumbens_11_16_14_no_outliers"
#indatafile = "C:\Users\praveen.taneja\OneDrive\python_data_analysis\ExcitNInhibPairs\corr_peak_locs_AND_vals_in_5ms_long"
#indatafile = "/Users/taneja/OneDrive/ProGran_FullKO_NucAccumbens_Grietje/ProGran_cKO_Striatum_Grietje/sEPSC/pt_PGRNcKOStriatum_mEPSCAnalysisNPooledwExclude12_11_14_Amp2SD_Deriv2SD_Cutoff4pA"
#indatafile = "/Users/taneja/OneDrive/ProGran_FullKO_NucAccumbens_Grietje/sEPSC/pt_ProGran_FullKO_NucAccumbens_sEPSC_3SDAmp_3SDderiv_AnalysisNPooled09_29_14"
#indatafile = "H:\\Core Labs\\Electrophysiology\\PraveenT\\MuckeLab\\CaPermAmpa\\AmpaDecayTauSigma_longno_OL"
#indatafile  = "H:\\Core Labs\\Electrophysiology\\PraveenT\\MuckeLab\\CaPermAmpa\\AmpaDecayTauCoef_long_no_outliers_means_with_gt"
#indatafile  = "/Users/taneja/Copy/Elsa_BRCA1_shRNA/pt_elsa_brca1_shrna_FI_Analysis1"
#indatafile  = "C:/Users/praveen.taneja/Copy/ProGran_FullKO_NucAccumbens_Grietje/Analysis01_14_15/pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled01_14_15"
#indatafile  = "C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/python_data_analysis/mouse_place_attraction/20140304OF2441trial0/corner_preference_across_genotypes"
#indatafile  = "C:/Users/taneja/Work/sumihiro/150213_hTau_20mo_RawData_Slopes"
#indatafile  = "/Users/taneja/Copy/Elsa_BRCA1_shRNA/pt_elsa_brca1_shrna_FI_AnalysisNPooled2_lesscols"
#indatafile  = "H:/Core Labs/Electrophysiology/PraveenT/GanLab/ProGran_FullKO_NucAccumbens_Grietje/Analysis04_27_15/pt_ProGran_FullKO_NucAccumbens_FIAnalysisNPooled04_27_15_UnBlinded_LessCols_NoOL"

#Input file suffix"
#suffix = ".csv"

#groupby_list = ['GT', 'Gender']
#groupby_list = ['GT']
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


# read actual user dataset 
df = pd.read_table(data_file, delimiter = ',')
print df.head()

dataframe_utils.group_means(df, groupby_list, out_data_file, display_raw = True, autoscale = False)