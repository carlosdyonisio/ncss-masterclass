# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 15:26:57 2020

@author: sbrow
"""

import numpy as np
from scipy import signal

def low_pass_filter(data, fc, fs):
    # data: signal to be filtered
    # fc: cut-off frequency of the filter (Hz)
    # fs: sampling rate (Hz)
    w = fc/fs*2
    
    b, a = signal.butter(order, w, 'low')
    out = signal.filtfilt(b,a, data)
    
    return out

def resampling_no_lpf(data, fs1, fs2):
    # data: data to be resampled:
    # fs1: the input sampling rate
    # fs2: desired output sampling rate
    # I was too lazy to implement this properly, ask one of us if you're interested
    # if you want to break some of my assumptions, go ahead and implement this more fully
    assert(fs1 == 48000 and fs1 >= fs2)
#    gcd = np.gcd(fs1, fs2)
#    p = fs2/gcd
#    q = fs1/gcd
#    assert(p == 1)
    q = fs2/fs1;
    #assert(isint(q))
    
    rng = np.arange(0, data.shape[0], int(q))
    
    out = data[rng]
    return out
    
    
def resampling_with_lpf(data, fs1, fs2):
    # data: data to be resampled:
    # fs1: the input sampling rate
    # fs2: desired output sampling rate

    # upsample first, unimplemented
    # fix the lpf to account for both upsampling and downsampling
    data = low_pass_filter(data, fs2/2, fs2)
    
    data = resampling_no_lpf(data, fs1, fs2)
    
    
    
    