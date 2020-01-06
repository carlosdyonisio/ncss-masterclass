import pyaudio
import numpy as np
import wave

def print_pyaudio_devices(pa):
    for i in range(0, pa.get_device_count()):
        print('{}'.format(pa.get_device_info_by_index(i)['name']))
        
def get_pyaudio_device_by_name(pa, name):
    for i in range(0, pa.get_device_count()):
        if pa.get_device_info_by_index(i)['name'].startswith(name):
            return i
    return None

def record_audio(dev_name, sample_rate, no_channels, seconds_to_record):
    pa = pyaudio.PyAudio()
    
    devindex = get_pyaudio_device_by_name(pa, dev_name)
    if devindex is None:
        print('No device starts with {}'.format(dev_name))
        print_pyaudio_devices(pa)
        pa.terminate()
        return


    stream = pa.open(input_device_index=devindex,
                     rate=sample_rate,
                     channels=no_channels,
                     input=True,
                     output=False,
                     format=pyaudio.paFloat32)
    pcm = stream.read(seconds_to_record * sample_rate)
    stream.stop_stream()
    stream.close()
    pa.terminate()

    pcm = np.fromstring(pcm, dtype=np.float32)
    pcm = np.reshape(pcm, (int(len(pcm)/no_channels), no_channels))
    return pcm

def play_audio(dev_name, sample_rate, pcm):
    pa = pyaudio.PyAudio()
    
    devindex = get_pyaudio_device_by_name(pa, dev_name)
    if devindex is None:
        print('No device starts with {}'.format(dev_name))
        print_pyaudio_devices(pa)
        pa.terminate()
        return

    if len(pcm.shape) == 1:
        no_channels = 1
    else:
        no_channels = pcm.shape[1]
    pcm.flatten()
    rawdata = pcm.astype(np.float32).tostring()

    stream = pa.open(output_device_index=devindex,
                     rate=sample_rate,
                     channels=no_channels,
                     input=False,
                     output=True,
                     format=pyaudio.paFloat32)
    pcm = stream.write(rawdata)
    stream.stop_stream()
    stream.close()
    pa.terminate()                 

def read_wave(file_name):
    w = wave.open(file_name, "rb")
    no_channels = w.getnchannels()
    fs = w.getframerate()
    sw = w.getsampwidth()
    frames = w.getnframes()
    if sw < 4:
        print("Only supports float32, 4 bytes sample width!")
        w.close()
        return None
    pcm = w.readframes(frames)
    w.close()
    pcm = np.fromstring(pcm, dtype=np.float32)
    pcm = np.reshape(pcm, (int(len(pcm)/no_channels), no_channels))
    return (fs, pcm)

def write_wave(file_name, fs, pcm):
    w = wave.open(file_name, "wb")
    if len(pcm.shape) == 1:
        no_channels = 1
    else:
        no_channels = pcm.shape[1]
    w.setnchannels(no_channels)
    w.setframerate(fs)
    w.setsampwidth(4)
    pcm.flatten()
    rawdata = pcm.astype(np.float32).tostring()
    w.writeframesraw(rawdata)
    w.close()





    
