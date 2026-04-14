"""Functions used in Exercise 8 of Geol 197 GDAM"""

# Import any modules needed in your functions here
import math
import numpy as np


# Define your new functions below

def mean(data):
    return np.sum(data) / len(data)

def std(data):
    mu = mean(data)
    variance = np.sum((data - mu)**2) / (len(data) - 1)
    return np.sqrt(variance)

def sem(data):
    return std(data) / np.sqrt(len(data))

# Defines the new function "gaussian"
def gaussian(gauss_mean, gauss_stddev, gauss_x):
    # Gaussian equation/formula
    return [(1/(gauss_stddev * np.sqrt (2 *np.pi))) * np.exp(-((x - gauss_mean)**2)/(2*(gauss_stddev)**2))for x in gauss_x]     