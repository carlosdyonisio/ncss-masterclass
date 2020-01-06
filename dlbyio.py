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
vfont_URL = "https://api.dolby.com/alpha/vfont"
virtu_URL = "https://api.dolby.com/beta/media/process/virtualize"

def file_upload(dlb_url, fname):
    print("DLBY.IO: Uploading " + fname + " to " + dlb_url)
    r = requests.post(url=file_ul_URL, headers=HDR, data=json.dumps({"url" : dlb_url}))
    if r.status_code != 200:
        print("Failed to get dlb url for file upload.")
        return r
    # get file upload url from response
    upload_url = r.json()['url']  
    with open(fname, 'rb') as file:
        r = requests.put(url=upload_url, headers=HDR, data=file)
    if r.status_code != 200:
        print("File failed to upload.")
    return r
        

def file_download(dlb_url, fname):
    print("DLBY.IO: Downloading " + fname + " from " + dlb_url)
    r = requests.get(url=file_dl_URL, headers=HDR, params={"url" : dlb_url})
    if r.status_code != 200:
        print("File failed to upload.")
        return r
    open(fname, "wb").write(r.content)
    return r


def noise_process(dlb_in, dlb_out, intensity):
    # process it with noise
    print("DLBY.IO: Calling Noise")
    r = requests.post(url=noise_URL, headers=HDR, data=json.dumps({"input" : dlb_in, "output" : dlb_out, "intensity" : intensity}))
    if r.status_code != 200:
        print("Noise request failed.")
        print(r.content)
        exit()
        
    r = wait_to_finish("Noise", r.json()["job_id"])

    return r
        
def vfont_process(dlb_in, dlb_out, preset):
    # combine lists dlb_in, dlb_out, params
    print("DLBY.IO: Calling Voice Fonts")
    data = {"input" : dlb_in, "output" : dlb_out, "preset" : preset}
    r = requests.post(url=vfont_URL, headers=HDR, data=json.dumps(data))

    if r.status_code != 200:
        print("Voice Fonts POST request failed.")
        print(r.content)
        exit()
        
    r = wait_to_finish("Voice Fonts", r.json()["job_id"])

    return r


def virtualize_process(dlb_in, dlb_out, position, room_level):
    # combine lists dlb_in, dlb_out, params
    print("DLBY.IO: Calling Virtualize")
    data = {"inputs" : [{"input" : dlb_in, "position" : position}], "output" : dlb_out, "room_level" : room_level}

    r = requests.post(url=virtu_URL, headers=HDR, data=json.dumps(data))
    if r.status_code != 200:
        print("Virtualize request failed.")
        print(r.content)
        exit()
       
    r = wait_to_finish("Virtualize", r.json()["job_id"])

    return r

def wait_to_finish(name, JOB_ID):
    print("Job ID: " + JOB_ID)
    while(True):
        r = requests.get(url=virtu_URL, params={"job_id" : JOB_ID}, headers=HDR)
        if r.status_code != 200:
            print(name + " GET request failed.")
            print(r.content)
            quit()
        print("Status: " + str(r.json()["status"]) + "       Progress: " + str(r.json()["progress"]))
        if r.json()["status"] == "Success":
            break
        elif r.json()["status"] == "Failed":
            print(r.json())
            exit()  
        elif r.json()["status"] == "InternalError":
            print(r.json())
            break
        time.sleep(5)
    return r


#print(r.text)