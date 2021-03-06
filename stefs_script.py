# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:51:58 2020

@author: sbrow
"""

#Scratch file
import dlbyio
import masterclass as mc
# import wavio 
import audiolib
import scipy.io.wavfile as wavfile
from matplotlib import interactive
interactive(True)

your_name = "stef"
dlb_in = "dlb://" + your_name + "/inwav.wav"
dlb_out = "dlb://" + your_name + "/outwav.wav"

input_wav = "Voice_challenge_32KHz_L2.wav"

clean_wav = "clean.wav"
virtu_wav = "virtu.wav"
vfont_wav = "vfont.wav"

dlbyio.file_upload(dlb_in, input_wav)
# use audiolib readw
fs, indata = audiolib.read_wave(input_wav)
mc.plot_all(indata, fs)

noise = np.random.rand(indata.shape[0], indata.shape[1] )-0.5

dlb_out = "dlb://" + your_name + "/clean.wav"

dlbyio.noise_process(dlb_in, dlb_out, "auto")
dlbyio.file_download(dlb_out, clean_wav)
fs, indata = audiolib.read_wave(clean_wav)
mc.plot_all(indata, fs)

#dlb_in = dlb_out
dlb_out = "dlb://" + your_name + "/virtu.wav"
dlbyio.virtualize_process(dlb_in, dlb_out, "stereo_front", 3)
dlbyio.file_download(dlb_out, virtu_wav)
fs, indata = = audiolib.read_wave(virtu_wav)
mc.plot_all(indata, fs)

# process it with vfont
#dlb_in = dlb_in
dlb_out = "dlb://" + your_name + "/vfont.wav"
#plot.interactive(True)
dlbyio.vfont_process(dlb_in, dlb_out, "dalek")
dlbyio.file_download(dlb_out, vfont_wav)
fs, indata = = audiolib.read_wave(vfont_wav)
mc.plot_all(indata, fs)