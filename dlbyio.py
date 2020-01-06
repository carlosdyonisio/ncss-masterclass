# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:31:04 2019

@author: sbrow
"""

import requests
import json
import time
import numpy as np
from sys import exit

KEY = "KGgU4s9dXtB0gc6FKNSgEKgOd4FlQ6Sm"
HDR = {"x-apikey" : KEY}
file_ul_URL = "https://api.dolby.com/file/upload"
file_dl_URL = "https://api.dolby.com/file/download"
noise_URL = "https://api.dolby.com/beta/media/process/noise"
vfont_URL = "https://dolby-dev.apigee.net/alpha/vfont"

def file_upload(dlb_url, fname):
    print("DLBY.IO: Uploading " + fname + " to " + dlb_url)
    r = requests.post(url=file_ul_URL, headers=HDR, data=json.dumps({"url" : dlb_url}))
    # get file upload url from response
    upload_url = r.json()['url']  
    with open(fname, 'rb') as file:
        r = requests.put(url=upload_url, headers=HDR, data=file)

def file_download(dlb_url, fname):
    print("DLBY.IO: Downloading " + fname + " from " + dlb_url)
    r = requests.get(url=file_dl_URL, headers=HDR, params=json.dumps({"url" : dlb_url}))
    open(fname, "wb").write(r.content)

def noise_process(dlb_in, dlb_out, intensity):
    # process it with noise
    print("DLBY.IO: Calling Noise")
    r = requests.post(url=noise_URL, headers=HDR, data=json.dumps({"input" : dlb_in, "output" : dlb_out, "intensity" : intensity}))
    if r.status_code != 200:
        print("Voice Fonts request failed.")
        print(r.content)
        exit()
        
    JOB_ID = r.json()["job_id"]
    print("Job ID: " + JOB_ID)
    while(True):
        r = requests.get(url=noise_URL+"?job_id="+JOB_ID, headers=HDR)
        print("Status: " + r.json()["status"])
        print("Progress: " + str(r.json()["progress"]))
    
        if r.json()["status"] == "Success":
            break
        if r.json()["status"] == "Failed":
            print(r.json())
            exit()
        time.sleep(5)
    return r
        
def vfont_process(dlb_in, dlb_out, preset):
    # combine lists dlb_in, dlb_out, params
    print("DLBY.IO: Calling Voice Fonts")
    data = {"input" : dlb_in, "output" : dlb_out, "preset" : preset}
#    settings = files.update(settings)
    r = requests.post(url=vfont_URL, headers=HDR, data=json.dumps(data))
    if r.status_code != 200:
        print("Voice Fonts request failed.")
        print(r.content)
        exit()
    
    JOB_ID = r.json()["job_id"]
    print("Job ID: " + JOB_ID)
    
    while(True):
        r = requests.get(url=vfont_URL,params=json.dump({"job_id" : JOB_ID}), headers=HDR)
        print("Status: " + r.json()["status"])
        print("Progress: " + str(r.json()["progress"]))
        if r.json()["status"] == "Success":
            break
        if r.json()["status"] == "Failed":
            print(r.json())
            exit()    
        time.sleep(5)
    return r







#print(r.text)