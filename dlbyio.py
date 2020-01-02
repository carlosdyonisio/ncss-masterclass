# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:31:04 2019

@author: sbrow
"""

import requests
import json
import time
import numpy as np


file_ul_URL = "https://api.dolby.com/file/upload"
file_dl_URL = "https://api.dolby.com/file/download"
noise_URL = "https://api.dolby.com/beta/media/process/noise"
vfont_URL = "https://dolby-dev.apigee.net/alpha/vfont"


KEY = "KGgU4s9dXtB0gc6FKNSgEKgOd4FlQ6Sm"

HDR = {"x-apikey" : KEY}
in_file = "dlb://stef/inwav.wav"
out_file = "dlb://stef/outwav.wav"


r = requests.post(url=file_ul_URL, headers=HDR, data=json.dumps({"url" : in_file}))
# get file url from response

FILE_URL = r.json()['url']
#print(FILE_URL)

with open('Voice_challenge_32KHz_L.wav', 'rb') as file:
    r = requests.put(url=FILE_URL, headers=HDR, data=file)
    
    
# process it with noise
r = requests.post(url=noise_URL, headers=HDR, data=json.dumps({"input" : in_file, "output" : out_file, "intensity" : "auto"}))

JOB_ID = r.json()["job_id"]
print(JOB_ID)
while(True):
    r = requests.get(url=noise_URL+"?job_id="+JOB_ID, headers=HDR)
    print("Status: " + r.json()["status"])
    print("Progress: " + str(r.json()["progress"]))

    if r.json()["status"] == "Success":
        break
    if r.json()["status"] == "Failed":
        print(r.json())
        exit
    time.sleep(5)
r = requests.get(url=file_dl_URL, headers=HDR, data=json.dumps({"url" : in_file}))
open("localfile.wav", "wb").write(r.content)

# process it with vfont
in_file = out_file
out_file = "dlb://stef/vfont.wav"


   
r = requests.post(url=vfont_URL, headers=HDR, data=json.dumps({"input" : in_file, "output" : out_file}))
JOB_ID = r.json()["job_id"]
print(JOB_ID)

while(True):
    r = requests.get(url=vfont_URL+"?job_id="+JOB_ID,params=json.dump({"job_id" : JOB_ID, "preset" : "elf"}), headers=HDR)
    print("Status: " + r.json()["status"])
    print("Progress: " + str(r.json()["progress"]))
    if r.json()["status"] == "Success":
        break
    if r.json()["status"] == "Failed":
        print(r.json())
        exit    
    time.sleep(5)


r = requests.get(url=file_dl_URL, headers=HDR, data=json.dumps({"url" : in_file}))
open("localfile.wav", "wb").write(r.content)

#print(r.text)