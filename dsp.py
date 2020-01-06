# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:26:57 2020

@author: sbrow
"""

import numpy as np
from scipy import signal

def low_pass_filter(data, fc, fs):
    w = fc/fs*2
    
    b, a = signal.butter(order, w, 'low')
    out = signal.filtfilt(b,a, data)
    
    return out

def resampling_no_lpf(data, fs1, fs2):
    gcd = np.gcd(fs1, fs2)
    p = fs2/gcd
    q = fs1/gcd
    
    data2 = np.zeros()
    
    
    
def resampling_with_lpf(data, fs1, fs2):
    
    
    
    