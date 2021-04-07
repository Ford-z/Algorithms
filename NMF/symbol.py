# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import wave
import os
import re
from numpy import *

count=0
color = ['#00BFFF','#7FFFD4','#A52A2A','#ADFF2F','#FFE4C4','#8A2BE2','#DEB887','#5F9EA0','#7FFF00','#FF7F50',
         '#8B008B','#FF8C00','#8B0000','#8FBC8F','#9400D3','#FFD700','#DCDCDC','#F0E68C','#E6E6FA','#9ACD32',
         '#90EE90','#0000CD','#E0FFFF','#FF1493','#90EE90','#1E90FF','#FFA07A','#20B2AA','#87CEFA','#800080',
         '#008000','#6495ED','#66CDAA','#9370DB','#3CB371','#FFE4E1','#7CFC00','#006400','#000080','#87CEEB',
         '#EEE8AA','#FF8C00','#8B0003','#DB7093','#FFC0CB','#DDA0DD','#B0E0E6','#800080','#FF69B4','#FFFF00',]
#设置颜色

def printdistance(file):
    global count
    df=pd.read_csv(file)
    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.plot(df.index,df)
    plt.rcParams['savefig.dpi'] = 600
    plt.rcParams['figure.dpi'] = 600
    # plt.rcParams['font.sans-serif']=['SimHei']
    # plt.rcParams['font.family'] = 'sans-serif'
    # plt.rcParams['axes.unicode_minus'] = False
    plt.title('Convergence curve')
    plt.xlabel('generation')
    plt.ylabel('loss')
    plt.xlim(0,)#确保从原点开始
    plt.ylim(0,)

    count=count+1
    plt.savefig("/home/ford/PycharmProjects/test1/image/lossfunction/sample"+str(count)+".png")
    plt.clf()  #清除画板
    print("损失函数曲线已经画好")

def printwave(file):
   df=pd.read_csv(file)
   plt.figure(figsize=(13, 7.5))#
   for i in range(len(df.columns)):
       col = df.iloc[:, i]
       plt.subplot(4,3,i+1)#确保每一幅图都出现
       plt.plot(col,color[i])
       plt.xlim(0, )
       plt.ylim(0, )

   left = None  # the left side of the subplots of the figure
   right = None  # the right side of the subplots of the figure
   bottom = None  # the bottom of the subplots of the figure
   top = None  # the top of the subplots of the figure
   wspace = 0.7  # the amount of width reserved for blank space between subplots, expressed as a fraction of the average axis width
   hspace = 0.7  # the amount of height reserved for white space between subplots, expressed as a fraction of the average axis height
   #控制间距
   plt.subplots_adjust(left, bottom, right, top, wspace, hspace)

   plt.savefig("/home/ford/PycharmProjects/test1/image/wave/wave.png")
   plt.clf() #清除画板
   print("特征频率图存储已结束")

def themebox(file):
    x=['Symbol1','Symbol2','Symbol3','Symbol4','Symbol5','Symbol6','Symbol7','Symbol8','Symbol9','Symbol10']
    df = pd.read_csv(file)
    fig, axes = plt.subplots(figsize=(23, 11))
    length = len(df.index)
    plt.bar(np.array([x * 4 for x in range(length)]), np.array(df.ix[:, 0]+df.ix[:,1]+df.ix[:,2]+df.ix[:,3]+df.ix[:,4]+df.ix[:,5]+df.ix[:,6]+df.ix[:,7]+df.ix[:,8]+df.ix[:,9]), np.array([3] * length), label='Speaker1',color=color[0])
    ax = plt.gca()
    ax.set_xticks(np.array([x * 4 for x in range(length)]))
    ax.set_xticklabels(list(x))
    c=0
    for i in range(10):
        a = df.ix[:, 0] + df.ix[:, 1] + df.ix[:, 2] + df.ix[:, 3] + df.ix[:, 4] + df.ix[:, 5] + df.ix[:, 6] + df.ix[:,7] + df.ix[:,8] + df.ix[:,9]
        if(i>=1):
            b=df.ix[:,i*10]+df.ix[:,i*10+1]+df.ix[:,i*10+2]+df.ix[:,i*10+3]+df.ix[:,i*10+4]+df.ix[:,i*10+5]+df.ix[:,i*10+6]+df.ix[:,i*10+7]+df.ix[:,i*10+8]+df.ix[:,i*10+9]#获得这一段的数据
            if(i==1):
                c=a
            plt.bar(np.array([x * 4 for x in range(length)]), np.array(b), np.array([3] * length),
                    bottom=np.array(c), label='Speaker' + str(i+1), color=color[i])#使得下一段的值是在上一段的基础上
            c=c+b

    ax.legend(loc=1)
    ax.set_xlabel("Sample_name", fontsize=15, color='b')
    ax.set_ylabel("Number Of Mutations", fontsize=15, color='b')
    plt.savefig("/home/ford/PycharmProjects/test1/image/theme/theme.png", dpi=400)
    plt.clf()  #清除画板
    print("主题堆积直方图已处理好")


if __name__ == "__main__":
    file1="/home/ford/PycharmProjects/test1/NMFresult/distance/distance_sample.csv"
    file2="/home/ford/PycharmProjects/test1/NMFresult/W/W_sample.csv"
    file3="/home/ford/PycharmProjects/test1/NMFresult/H/H_sample.csv"
    file4="/home/ford/PycharmProjects/test1/NMFresult/distance/distance_better.csv"
    printdistance(file1)
    printwave(file2)
    themebox(file3)
    printdistance(file4)







