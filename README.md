Google_TTS_Python
=================

Google TTS.

## 简介
谷歌翻译中文TTS的接口提取。

## 依赖
- python-requests模块
- mplayer程序（仅say函数）
- *nix操作系统

## 功能
- say(str), 念出str的内容，不产生文件
- tts(str), 在当前目录下生成一个名为tts-str.mpeg的文件
- python tts.py "要读的内容"  念出要读的内容 
- python tts.py -f filename  逐行念出要读的文件 

## 备注
请随意使用。
