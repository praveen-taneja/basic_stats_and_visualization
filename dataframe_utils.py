# -*- coding: utf-8 -*-
# By Praveen Taneja praveen.taneja@gmail.com

import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import matplotlib.ticker as ticker
import itertools
import math
import sys
from scipy.stats import pearsonr
#from matplotlib.ticker import ScalarFormatter

from matplotlib.backends.backend_pdf import PdfPages

def numeric_cols(df):
    '''
    given a data frame, return list of column names that have numeric data
    '''

    col_names = df.columns.values.tolist() # extract column names
    col_names_numeric = []
    
    # make a dataframe with numeric columns only
    for col_name in col_names:
        #print col_name, df[col_name].dtype.kind
        if np.issubdtype(df[col_name].dtype, np.integer) or np.issubdtype(df[col_name].dtype, np.floating):
            col_names_numeric.append(col_name)
    return col_names_numeric

def pair_plots(df, delimiter, outdatafile, graphs_per_plot = 8):
    '''given a dataframe, read the file into a data frame and plot scatter plots
    of all numeric columns.
    
    '''
    
    #df = pd.read_table(filename, delimiter = delimiter)
    
    
    col_names_numeric = numeric_cols(df)
    
    col_name_pairs = list(itertools.combinations(col_names_numeric, 2))
    print 'number of pairs = ', len(col_name_pairs)
    # arrange col_name_pairs in order of decreasing absolute corr coeffs.
    corr_list = []
    pval_list = []
    for x, y in col_name_pairs:
        # also calculate p-value
        df_clean = df.ix[:, [x, y]].dropna()
        corr_val, p_val = pearsonr(df_clean[x], df_clean[y]) #pearsonr from scipystats also returns p-value
        corr_list.append(abs(corr_val))
        pval_list.append(p_val)     
    col_name_pairs_sorted = [y for (x, y) in sorted(zip(corr_list, col_name_pairs), reverse = True)] 
    
    # plot all plots in same graph
    #subplot_rows = math.ceil(math.sqrt(len(col_name_pairs_sorted)))
    #subplot_cols = math.ceil(math.sqrt(len(col_name_pairs_sorted)))
    
    # plot maximum graphs_per_plot in a single plot
    #print 'graphs_per_plot', graphs_per_plot
    num_plots = int(math.ceil(float(len(col_name_pairs_sorted))/graphs_per_plot))
    #print 'num_plots', num_plots
    
    subplot_rows = math.ceil(math.sqrt(graphs_per_plot))
    subplot_cols = math.ceil(math.sqrt(graphs_per_plot))

    #print col_name_pairs_sorted
    fig = pl.figure(figsize=(14, 9.5))
    graph_num = 0
    pp = PdfPages(outdatafile)
    plot_num = 1
    print 'saving plot number', plot_num, 'of', num_plots
    for x, y in col_name_pairs_sorted:
        #print x, y
        if graph_num >= graphs_per_plot:
            #pl.show()
            pp.savefig()
            pl.close()
            fig = pl.figure(figsize=(14, 9.5))
            graph_num = 0
            plot_num = plot_num + 1
            print 'saving plot number', plot_num, 'of', num_plots
            
        #print graph_num, x, y
        #print subplot_rows, subplot_cols, graph_num
        fig.add_subplot(subplot_rows, subplot_cols, graph_num + 1)
        pl.subplots_adjust(left=.07, right=.93, bottom=.07, top=.93, wspace=.15,
                   hspace=.15)
        df_clean = df.ix[:, [x, y]].dropna()
        corr_val, p_val = pearsonr(df_clean[x], df_clean[y]) #pearsonr from scipystats also returns p-value
        corr_val_str = format(corr_val, '0.2f')
        p_val_str = format(p_val, '0.3f')    
        pl.scatter(df_clean[x], df_clean[y], label = 'r, p =' + corr_val_str +', '+p_val_str)#label = x+y)#, color=colors[y_pred].tolist(), s=10)
        #pl.axis([0.8*min(df[x]), 1.2*max(df[x]), 0.8*min(df[y]), 1.2*max(df[y])])
        
        
        if len(df_clean[x]) > 0 and len(df_clean[y]):
            np_x = df_clean[x].values 
            np_y = df_clean[y].values
            zfit = np.polyfit(np_x, np_y, 1)# add trend line
            p1d = np.poly1d(zfit)
            pl.plot(np_x, p1d(np_x), "r--")
            x_min = min(df_clean[x])
            x_max = max(df_clean[x])
            y_min = min(df_clean[y])
            y_max = max(df_clean[y])
            
            x_range_min = x_min - 0.1*abs(x_min)
            x_range_max = x_max + 0.1*abs(x_max)
            
            y_range_min = y_min - 0.1*abs(y_min)
            y_range_max = y_max + 0.1*abs(y_max)
                
            pl.xlim(x_range_min, x_range_max)
            pl.ylim(y_range_min, y_range_max)
        pl.legend(loc = 0, fontsize = 11)
        pl.xlabel(x)
        pl.ylabel(y)
        pl.ticklabel_format(style = 'sci',scilimits=(0,0),axis='both', useOffset=False)
        graph_num = graph_num + 1
        
    #pl.show()
    pp.savefig()
    pl.close()    
    pp.close()
    print 'plots saved to', outdatafile
    #pl.show()  # uncomment to see scatter plots


def column_plots(df, delimiter, outdatafile, graphs_per_plot = 8):
    '''given a dataframe, read the file into a data frame and plot scatter plots
    of all numeric columns.
    
    '''
    
    #df = pd.read_table(filename, delimiter = delimiter)
    
    
    col_names_numeric = numeric_cols(df)
    
    
    print 'number of numeric columns = ', len(col_names_numeric)
    
    # plot maximum graphs_per_plot in a single plot
    #print 'graphs_per_plot', graphs_per_plot
    num_plots = int(math.ceil(float(len(col_names_numeric))/graphs_per_plot))
    #print 'num_plots', num_plots
    
    subplot_rows = math.ceil(math.sqrt(graphs_per_plot))
    subplot_cols = math.ceil(math.sqrt(graphs_per_plot))

    #print col_name_pairs
    fig = pl.figure(figsize=(14, 9.5))
    graph_num = 0
    pp = PdfPages(outdatafile)
    plot_num = 1
    print 'saving plot number', plot_num, 'of', num_plots
    for y in col_names_numeric:
        if graph_num >= graphs_per_plot:
            #pl.show()
            pp.savefig()
            pl.close()
            fig = pl.figure(figsize=(14, 9.5))
            graph_num = 0
            plot_num = plot_num + 1
            print 'saving plot number', plot_num, 'of', num_plots
            
        #print graph_num, x, y
        #print subplot_rows, subplot_cols, graph_num
        fig.add_subplot(subplot_rows, subplot_cols, graph_num + 1)   
        pl.subplots_adjust(left=.07, right=.93, bottom=.07, top=.93, wspace=.15,
                   hspace=.15) 
        pl.plot(df[y], 'ro', label = y)#, color=colors[y_pred].tolist(), s=10)
        #pl.axis([0.8*min(df[x]), 1.2*max(df[x]), 0.8*min(df[y]), 1.2*max(df[y])])
        pl.ylim(0.8*min(df[y]), 1.2*max(df[y]))
        #pl.legend(loc = 0)
        pl.xlabel("#")
        pl.ylabel(y)
        pl.ticklabel_format(style = 'sci',scilimits=(0,0),axis='both', useOffset=False)
        graph_num = graph_num + 1
        
    #pl.show()
    pp.savefig()
    pl.close()    
    pp.close()
    print 'plots saved to', outdatafile
    #pl.show()  # uncomment to see scatter plots



def group_means(df, groupby_list, outdatafile, display_raw = True, autoscale = False):
    '''
given a data-frame, and some groupby factors, plot 

1. raw data values.
2. means and sems
3. medians and quartiles (not yet implemented).
4. statistical tests (not yet implemented).

eg. if there are 5 numeric columns and one grouby factor with 3 possible values,
plot 3 means per column and do it for 5 columns.

for 2 groupby factors, with 3 and 4 possible values respectively, for each
column there will be 12 means.

code - for each column, make 1 plot. In each plot, plot m*n means
    '''

    #print 'groupbylist',groupbylist
    grouped = df.groupby(groupby_list)
    #print grouped.groups
    col_names_numeric = numeric_cols(df)
    
    # exclude calculating means for columns in groupby_list
    exclude_cols = [col for col in col_names_numeric if col in groupby_list]
    #print 'exclude_cols', exclude_cols
    print " "
    num_plots = len(col_names_numeric)
    print 'number of plots =', num_plots
    print 'Names of numeric columns =', col_names_numeric
    #for name, group in grouped:
    #    print name, type(group)
    pp = PdfPages(outdatafile+".pdf")
    stats_list = []
    
    for col_num, col_name in enumerate(col_names_numeric):
        #print "***group[col_name].describe***", grouped[col_name]#.describe()
        avg = grouped[col_name].mean()#.aggregate(np.mean)
        std = grouped[col_name].std()#.aggregate(np.std)
        size = grouped[col_name].count()#.aggregate(np.size)
        size_withnan = grouped[col_name].aggregate(np.size) # for plotting raw data later
        max_val = max(grouped[col_name].max())
        min_val = min(grouped[col_name].min())
        
        #print 'type(avg)', type(avg)
        #print 'size', type(size)
        #print 'len', len(grouped)
        
        #if (size > 0):
        sem = std/np.sqrt(size)
        #with open(outdatafile+".csv", 'a') as f:
        #    avg.to_csv(f, header = True)
        #    size.to_csv(f, header = True)
        #    sem.to_csv(f, header = True)
        #avg.to_csv(outdatafile+".csv")
        
        # aggregation function returns a multi-level index object.
        # reset_index() converts these indices to regular column.
        
        
        # can't convert ward_five labels to ward_five column if such column aleady
        #exists. Basically, if groupby list has a numeric column we can't reset 
        #index for that.
        if col_name not in exclude_cols:
            #print 'avg.reset_index()',avg.reset_index()
            
            df_temp = avg.reset_index() # convert multilvel index object to data-frame
            df_temp = df_temp.rename(columns = {col_name : col_name + '_Avg'})
            stats_list.append(df_temp)
            
            df_temp = size.reset_index().drop(groupby_list, axis = 1)
            df_temp = df_temp.rename(columns = {col_name : col_name + '_N'})
            stats_list.append(df_temp)
            
            df_temp = sem.reset_index().drop(groupby_list, axis = 1)
            df_temp = df_temp.rename(columns = {col_name : col_name + '_Sem'})
            stats_list.append(df_temp)
            
            
            #stats_list.append(avg.reset_index())
            #stats_list.append(size.reset_index().drop(['GT', 'ward_five'], axis = 1))
            #stats_list.append(sem.reset_index().drop(['GT', 'ward_five'], axis = 1))
            
        #print 'standard deviation', std
        #print 'number of observations', size
        #print 'standard error of mean', sem
        pl.figure(figsize=(10, 10))
        pl.title(col_name, size=24)
        p = avg.plot(kind = 'bar', yerr = sem, grid = None, fill = None)
        x_locs = np.array(p.xaxis.get_majorticklocs())
        pl.grid(None)
        if display_raw:
            # plot raw points with some scatter so that they don't overlap
            #for bar_num, num_pnts in enumerate(size):
            for bar_num, (num_pnts, group) in enumerate(zip(size_withnan, grouped[col_name])):
            # group is a tuple with 1st arguement as genotype and other factor levels
            #and 2nd arguement as data values
                #print 'size', bar_num, num_pnts#, group[1]
                #print 'p.xaxis.get_majorticklocs()',p.xaxis.get_majorticklocs()
                #print '****num_pnts****', num_pnts
                x = np.random.normal(x_locs[bar_num], 0.05, size = int(num_pnts))
                pl.plot(x, group[1], linestyle='',marker = 'o', color ='magenta', alpha=0.3, markersize = 4.0)
                if autoscale:
                    pl.ylim(min_val, max_val)
        
          
        pl.ylabel(col_name, fontsize=24)
        #pl.tick_params(axis='both', which='major', labelsize=24)
        #pl.tick_params(axis='both', which='minor', labelsize=24)
        #y_formatter = ticker.ScalarFormatter(useOffset=False)
        #ax = pl.gca()
        #pl.ticklabel_format(style = 'sci',scilimits=(0,0),axis='both', useOffset=False)
        print 'saving plot number', col_num + 1, 'of', num_plots
        pl.show()
        pp.savefig()
        #pl.close()
    pp.close()
    
    print 'plots saved to', outdatafile+".pdf"
    df_stats = pd.DataFrame()
    df_stats = pd.concat(stats_list, axis = 1)
    df_stats.to_csv(outdatafile+".csv")
    print 'values saved to', outdatafile+".csv"
    #print stats_list
    #print len(stats_list)
    #print df_stats

def cols_to_long(df):
    '''given a set of columns convert to long format with column names as keys
    eg. 
    input - 
    col1    col2    col3
    1       2       3
    4       5       6
    output - 
    1   col1
    4   col1
    2   col2
    5   col2
    3   col3
    6   col3
    '''
    col_names = df.columns
    df_out = pd.DataFrame()
    for col_name in col_names:
        #print col_name
        names_col = pd.TimeSeries([col_name]*len(df[col_name]))
        #print names_col.head()
        df_temp = pd.DataFrame({'data':df[col_name], 'names': names_col})
        df_out = pd.concat([df_out, df_temp], axis = 0)
    return df_out
    
    
        
        