# -*- coding: utf-8 -*-
"""
Created on Mon Jan  6 10:51:58 2020

@author: sbrow
"""

#Scratch file
import dlbyio

dlb_in = "dlb://stef/inwav.wav"
dlb_out = "dlb://stef/outwav.wav"

dlbyio.file_upload(dlb_in, "Voice_challenge_32KHz_L.wav")
dlbyio.noise_process(dlb_in, dlb_out, "auto")
dlbyio.file_download(dlb_out, "denoised.wav")


# process it with vfont
dlb_in = dlb_out
dlb_out = "dlb://stef/vfont.wav"

dlbyio.vfont_process(dlb_in, dlb_out, "elf")

dlbyio.file_download(dlb_out, "download.wav")
