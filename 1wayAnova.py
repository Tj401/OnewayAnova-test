# -*- coding: utf-8 -*-
"""
Created on Fri Feb 22 21:22:12 2019

@author: kdandebo
"""

import pandas as pd
#import statsmodels.api as sm
#import pylab
import scipy.stats as stats
#from scipy import stats
from matplotlib import pyplot
#import matplotlib.pyplot as plt
import numpy as np
from statsmodels.graphics.gofplots import qqplot
#from tkinter.filedialog import askopenfilename
#twosample = pd.ExcelFile(askopenfilename())
OneWayAnova = pd.ExcelFile('C:/Users/kdandebo/Desktop/Models/DS training/Yogesh data sets/ContractRenewal_Data(unstacked).xlsx')
OneWayAnova = OneWayAnova.parse("Sheet1")
print(OneWayAnova.columns)
OneWayAnova = OneWayAnova.rename(columns={'Supplier A': 'E1', 'Supplier B': 'E2','Supplier C': 'E3'})

conv_arr= OneWayAnova.values

#split matrix into 3 columns each into 1d array
arr1 = np.delete(conv_arr,[1,2],axis=1) 
arr2 = np.delete(conv_arr,[0,2],axis=1) 
arr3 = np.delete(conv_arr,[0,1],axis=1)

#converting into 1D array
E1 = arr1.ravel()
E2 = arr2.ravel()
E3 = arr3.ravel()

#Variance test by plotting the graph, seems like all of them follow ND
qqplot(OneWayAnova['E1'], line='s')
qqplot(OneWayAnova['E2'], line='s')
qqplot(OneWayAnova['E3'], line='s')
pyplot.show()

#we need to verify the p values by the shapiro test
print(stats.shapiro(E1))
print(stats.shapiro(E2))
print(stats.shapiro(E3))

#chekcing the p-value by comparing the means of all the employees
output = stats.f_oneway(OneWayAnova['E1'], OneWayAnova['E2'], OneWayAnova['E3'])
print(output)
