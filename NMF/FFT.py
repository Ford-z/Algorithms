# -*- coding: utf-8 -*-
from numpy import *
import numpy as np
from scipy.fftpack import fft,ifft
import matplotlib.pyplot as plt
import seaborn
import wave
import os
import filetype
import ffmpeg
from pydub import AudioSegment
import re
import pandas as pd


filepath = "/home/ford/PycharmProjects/test1/voice"#添加路径
filename= os.listdir(filepath) #得到文件夹下的所有文件名称
sample=list()
df = pd.DataFrame(sample)
count=0
for file in filename:
    source=os.path.join(filepath +"/"+ file)
    name=re.findall(r'(.+?)\.',file)#用正则表达式获得文件前缀名
    f = wave.open(source, 'rb')
    params = f.getparams()
    print(params)
    nchannels, sampwidth, framerate, nframes = params[:4]#声道数 量化位数 采样频率 采样点数
    strData = f.readframes(200)#读取音频，字符串格式
    print(strData)
    y = np.fromstring(strData, dtype=np.short)#将字符串转化为short
    print(y)
    #y = np.reshape(y, [nframes, nchannels])
    x = np.linspace(0, 1, 200)#采样定理
    f.close()#关闭文件

    yy = fft(y)#快速傅里叶变换
    yreal = yy.real#获取实数部分
    yimag = yy.imag#获取虚数部分

    yf = abs(fft(y))#取绝对值
    yf1 = abs(fft(y)) / len(x)#归一化处理
    yf2 = yf1[range(int(len(x) / 2))]#由于对称性，只取一半区间
    #np.savetxt("./voicenumpy"+"/single/"+name[0], yf2)#储存目标数组
    if(count==0):
        sample=yf2
        df = pd.DataFrame(sample)
    else:
        df[count]=yf2#

    xf = np.arange(len(y))#频率
    xf1 = xf
    xf2 = xf[range(int(len(x) / 2))]#取一半区间

    plt.subplot(221)
    plt.plot(x, y)
    plt.title('Original wave')

    plt.subplot(222)
    plt.plot(xf, yf, 'r')
    plt.title('FFT of Mixed wave(two sides frequency range)', fontsize=7, color='#7A378B')

    plt.subplot(223)
    plt.plot(xf1, yf1, 'g')
    plt.title('FFT of Mixed wave(normalization)', fontsize=9, color='r')

    plt.subplot(224)
    plt.plot(xf2, yf2, 'b')
    plt.title('FFT of Mixed wave)', fontsize=10, color='#F08080')

    plt.savefig("/home/ford/PycharmProjects/test1/image/wave/"+name[0]+".png")
    plt.clf()#清除画板，不然画图痕迹会相互影响
    count+=1

print(df)
print("波形图存储已结束")
df.to_csv('/home/ford/PycharmProjects/test1/voicenumpy/sample.csv', index=False, header=False )


