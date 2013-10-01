#!/usr/bin/env python
#! coding: utf-8

#########################################################################
# File Name: tts.py
# Author: Sandtears
# mail: me@sandtears.com
# Created Time: 2013年10月01日 星期二 17时41分17秒
#########################################################################

def tts(str):
    try:
        import requests
    except:
        print "请下载python-requests模块后使用..."
        exit(-1)
    import urllib
    
    s = requests.Session()
    s.get("http://translate.google.com/#zh-CN/en/" + urllib.quote(str))
    res = s.get("http://translate.google.com/translate_tts?ie=UTF-8&q=" + urllib.quote(str) + "&tl=zh-CN&total=1&idx=0&textlen=8&prev=input").content
    f = open("tts-" + str + ".mpeg", "w")
    f.write(res)
    f.close()

def say(str):
    tts(str)
    import os
    os.system("mplayer tts-" + str + ".mpeg")
    os.system("rm -f tts-" + str + ".mpeg")

if __name__ == "__main__":
    import sys
    say(sys.argv[1])
