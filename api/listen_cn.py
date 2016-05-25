#-*- coding:utf-8 -*-
import speech_recognition as sr

# this is called from the background thread
def callback(recognizer, audio):
    BING_KEY = "6c81bbd3cd1248d7bb32b99af134de7a" # Microsoft Bing Voice Recognition API keys 32-character lowercase hexadecimal strings
    try:
        content=r.recognize_bing(audio, key=BING_KEY, language = "zh-CN", show_all = False)
        print("Microsoft Bing Voice Recognition thinks you said "+content)
    except sr.UnknownValueError:
        print("你说什么？".decode('utf-8').encode('cp936'))#Mac删去.decode('utf-8').encode('cp936')
    except sr.RequestError as e:
        print("Sorry, but I can not connect to my server sir; {0}".format(e))

#Microphone(device_index = None, sample_rate = 16000, chunk_size = 1024)

r = sr.Recognizer()
m = sr.Microphone(device_index = None, sample_rate = 6000)
with m as source:
    r.adjust_for_ambient_noise(source) # we only need to calibrate once, before we start listening

r.energy_threshold = 8000
r.pause_threshold = 0.8

# start listening in the background (note that we don't have to do this inside a `with` statement)
stop_listening = r.listen_in_background(m, callback)
# `stop_listening` is now a function that, when called, stops background listening

# do some other computation for 5 seconds, then stop listening and keep doing other computations
import time
#for _ in range(50): time.sleep(0.1) # we're still listening even though the main thread is doing other things
#stop_listening() # calling this function requests that the background listener stop listening
while True: time.sleep(1)