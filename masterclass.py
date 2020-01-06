# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:18:09 2019

@author: sbrow
"""
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import interactive
import scipy

def plot_signal(data, fs):
    plt.plot(np.arange(data.shape[0])/fs, data)
    plt.xlabel("Time (s)")
    plt.ylabel("Amplitude")

def plot_fft_magnitude(data, fs):
    # this allows experimentation of length of FFT, and number of bins etc.
    fft_data = scipy.fft(data)
    plt.plot(np.arange(data.shape[0])/data.shape[0]*fs, np.abs(fft_data))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Magnitude")
    
def plot_fft_angle(data, fs):
    fft_data = scipy.fft(data)
    plt.plot(np.arange(data.shape[0])/data.shape[0]*fs, np.angle(fft_data))
    plt.xlabel("Frequency (Hz)")
    plt.ylabel("Angle (radians)")

def plot_specgram(data, fs):
    NFFT = 1024
    plt.specgram(x=data, NFFT=NFFT, Fs=fs)

def plot_all(data, fs):
    plt.subplot(311)
    plot_signal(data, fs)
    plt.subplot(312)
    plot_fft_magnitude(data, fs)
    #plt.subplot(413)
    #plot_fft_angle(data, fs)
    plt.subplot(313)
    plot_specgram(data, fs)



