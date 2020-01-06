# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:51:58 2020

@author: sbrow
"""

#Scratch file
import dlbyio
import masterclass as mc
# import wavio 
import scipy.io.wavfile as wavfile

dlb_in = "dlb://stef/inwav.wav"
dlb_out = "dlb://stef/outwav.wav"

input_wav = "Voice_challenge_32KHz_L.wav"
clean_wav = "clean.wav"
virtu_wav = "virtu.wav"
vfont_wav = "vfont.wav"

dlbyio.file_upload(dlb_in, input_wav)
#fs, indata = wavio.read(input_wav)
#fs, indata = wavfile.read(open(input_wav, "rb"))
#mc.plot_all(indata, fs)

dlbyio.noise_process(dlb_in, dlb_out, "auto")
#dlbyio.file_download(dlb_out, clean_wav)
#fs, indata = wavio.read(clean_wav)
#fs, indata = wavfile.read(open(clean_wav, "rb"))
#mc.plot_all(indata, fs)
#dlb_in = dlb_out
#dlb_out = "dlb://stef/virtu.wav"

#dlbyio.virtualize_process(dlb_in, dlb_out, "stereo_front", 3)
#dlbyio.file_download(dlb_out, virtu_wav)

# process it with vfont
dlb_in = dlb_in
dlb_out = "dlb://stef/vfont.wav"

dlbyio.vfont_process(dlb_in, dlb_out, "dalek")
dlbyio.file_download(dlb_out, vfont_wav)
#fs, indata = wavfile.read(open(font_wav, "rb"))
#mc.plot_all(indata, fs)