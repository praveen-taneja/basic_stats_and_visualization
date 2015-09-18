setwd("/Users/taneja/Copy/ProGran_FullKO_NucAccumbens_Grietje/05_30_15")
fileName <- 'pt_ProGran_FullKO_NucAccumbens_FIInstFreq05_30_15Unblinded_NoRsRInOutliers_fit_thresh_plus_150pA_noCohort3'
data <- read.table(paste(fileName, '.csv', sep=''), header=T, sep=',') # header = True
head(data)
y = data$IFrq_CurrTh # IFrq_MaxFreq# IFrq_Slope
x = data$GT

fit <- lm(y ~ x, data=data)
summary(fit)

# post hoc test

pairwise.t.test(y, x, p.adj = "holm") # or "none", "bonf"
