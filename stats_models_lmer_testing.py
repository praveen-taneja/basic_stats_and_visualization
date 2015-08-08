import numpy as np
import pandas as pd
import statsmodels.api as sm

indatafile  = "C:/Users/taneja/Work/sumihiro/150213_hTau_20mo_RawData_Slopes"
suffix = ".csv"
#data = pd.read_csv("C:\Users\praveen.taneja\OneDrive\ProGran_FullKO_NucAccumbens_Grietje\Analysis11_16_14\InstFreqWPars.csv")
data = pd.read_csv(indatafile + suffix)
print data.head()
#data = data[data['Gender'] == 'm']
#print data.head()
model = sm.MixedLM.from_formula("slope ~ gt", data, groups=data["GT"])
result = model.fit()
print result.summary()