# -*- coding: utf-8 -*-
"""
by Praveen Taneja praveen.taneja@gmail.com

Documentation from statsmodels
http://statsmodels.sourceforge.net/devel/stats.html

solve_power(self, effect_size=None, nobs1=None, alpha=None, power=None, ratio=1.0, alternative='two-sided') method of statsmodels.stats.power.TTestIndPower instance
    solve for any one parameter of the power of a two sample t-test
    
    for t-test the keywords are:
        effect_size, nobs1, alpha, power, ratio
    
    exactly one needs to be ``None``, all others need numeric values
    
    Parameters
    ----------
    effect_size : float
        standardized effect size, difference between the two means divided
        by the standard deviation. `effect_size` has to be positive.
    nobs1 : int or float
        number of observations of sample 1. The number of observations of
        sample two is ratio times the size of sample 1,
        i.e. ``nobs2 = nobs1 * ratio``
    alpha : float in interval (0,1)
        significance level, e.g. 0.05, is the probability of a type I
        error, that is wrong rejections if the Null Hypothesis is true.
    power : float in interval (0,1)
        power of the test, e.g. 0.8, is one minus the probability of a
        type II error. Power is the probability that the test correctly
        rejects the Null Hypothesis if the Alternative Hypothesis is true.
    ratio : float
        ratio of the number of observations in sample 2 relative to
        sample 1. see description of nobs1
        The default for ratio is 1; to solve for ratio given the other
        arguments it has to be explicitly set to None.
    alternative : string, 'two-sided' (default), 'larger', 'smaller'
        extra argument to choose whether the power is calculated for a
        two-sided (default) or one sided test. The one-sided test can be
        either 'larger', 'smaller'.
    
    Returns
    -------
    value : float
        The value of the parameter that was set to None in the call. The
        value solves the power equation given the remaining parameters.
    
    
    Notes
    -----
    The function uses scipy.optimize for finding the value that satisfies
    the power equation. It first uses ``brentq`` with a prior search for
    bounds. If this fails to find a root, ``fsolve`` is used. If ``fsolve``
    also fails, then, for ``alpha``, ``power`` and ``effect_size``,
    ``brentq`` with fixed bounds is used. However, there can still be cases
    where this fails.

"""
#print(__doc__)

import datetime
import statsmodels.stats.power as smp


###################################################

#######Start - Variables to be edited by user #####


diff_means = 5 # desired difference in means
stddev = 25    # standard deviation
alpha = 0.05 #significance level (probability of getting false positive)
#power = 1 - beta where beta = (probability of getting false negative). Typical
# beta = 0.2 to 0.4. So power = 0.8 to 0.6
power = 0.6

#######End - Variables to be edited by user #######
###################################################

# effect_size = difference between means divided by standard dev. Should be >0
# eg. 10% change in freq on an initial value of 50Hz = 5Hz. Say, std dev. = 10Hz
# then effect size = 5/10 = 0.5
effect_size = float(abs(diff_means))/float(stddev)

print "====================================================="
now = datetime.datetime.now()
print "Starting analysis at:", now.strftime("%m-%d-%Y %H:%M")
print "====================================================="
print " "
print "diff_means =", diff_means
print "stddev = ",stddev
print "effect_size =", effect_size
print "alpha =", alpha
print "power =", power
print " "
print "Observations needed =", round(smp.tt_ind_solve_power(effect_size = effect_size, nobs1 =None , alpha =alpha , power = power))
print "Observations needed =", round(smp.zt_ind_solve_power(effect_size = effect_size, nobs1 =None , alpha =alpha , power = power))