import pandas as pd
import numpy as np
import matplotlib.pylab as plt
import sys
sys.path.append('C:/Users/praveen.taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
#sys.path.append('/Users/taneja/Dropbox/Analysis/python_progs/EclipseIDEWorkSpace/pt_PyUtilsDir')
import dataframe_utils
import pt_PyUtils
import os
import imp
imp.reload(dataframe_utils)
imp.reload(pt_PyUtils)

data_file = pt_PyUtils.get_path('*.*')
print 'loading data file', data_file
data_file_no_ext = os.path.splitext(data_file)[0]

df = pd.read_table(data_file, delimiter = ',')

print df.RInAvg.describe() # also prints median and quartiles
RIn = df.RInAvg.values
q1 = np.percentile(RIn, 25.0)
q2 = np.percentile(RIn, 50.0)
q3 = np.percentile(RIn, 75.0)

print q1, q2, q3
print 'iqr = ', q3-q1

#RIn.plot(kind = 'hist')
#plt.show()
