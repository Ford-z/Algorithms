# -*- coding:utf-8 -*-
from pylab import *
from numpy import *
import cv2
import os
import pandas as pd
from tkinter import *
import numpy as np
import matplotlib.pyplot as plt
import re
import scipy.io as scio
from skimage import io
import seaborn as sns

np.set_printoptions(suppress=True)#

def LoadMovie(file_path):
    cap = cv2.VideoCapture(file_path)#read video#
    frame_count = 0
    success, frame = cap.read()#第一个参数success 为True 或者False,代表有没有读取到图片,第二个参数frame表示截取到一帧的图片
    while (success):
        frame_count = frame_count + 1#count
        params = []
        params.append(1)
        cv2.imwrite("video" + "_%d.jpg" % frame_count, frame, params)
        cv2.imshow('image',frame)

    cap.release()

def Loaddata(file_path):
    f=open(file_path)
    V=[]
    for line in f.readlines():
        lines = line.strip().split(",")#剥离空格#
        data = []
        for x in lines:
            if x != "-":
                data.append(float(x))
            else:
                data.append(float(0))
        V.append(data)
    f.close()
    return mat(V)

def Setr():
    m, n = shape(V)
    a=(m*n)/(n+m)#设定r相关的规则#
    r=int(a/5)#强制类型转换，确保r<nm/(n+m)#
    b=str(r)
    print("主题一共有"+b+"个")

    return r


def NMF(V, r, k, e):
    A=[]
    m,n=shape(V) #得到目地矩阵的行和列#
    W = mat(random.random(size=(m, r)))#设定权重矩阵中随机数值
    H = mat(random.random(size=(r, n)))#设定特征矩阵中随机数值

    for x in range(k):
        V_new = W * H  #V=W*H#
        D = V_new - V
        distance = 0.0  # 初始化#
        for i in range(m):
            for j in range(n):
                distance = D[i, j] * D[i, j]  # 欧式距离#

        A.append(distance)

        if distance < e:
            print(distance)
            break

        a_num = transpose(W)*V
        a_den = transpose(W)*W*H

        for i in range(r):
            for j in range(n):
                if a_den[i, j]!= 0:
                    H[i, j]= H[i, j]*a_num[i, j]/a_den[i, j]#更新规则1#

        b_num = V * transpose(H) #不能同时设定两个更新方则，不然会相互影响#
        b_den = W * H * transpose(H)

        for i in range(m):
            for j in range(r):
                if b_den[i, j]!= 0:
                    W[i, j] = W[i, j]*b_num[i, j]/b_den[i, j]#更新规则2#
    return W,H,A


def save(a,b,c,d,file):
    name = re.findall(r'(.+?)\.', file)
    df = pd.DataFrame(a)
    df.to_csv('/home/ford/PycharmProjects/test1/NMFresult/W/W_sample.csv', index=False, header=False)
    dd=pd.DataFrame(b)
    dd.to_csv('/home/ford/PycharmProjects/test1/NMFresult/H/H_sample.csv',index=False)#一定要有表头
    np.savetxt("/home/ford/PycharmProjects/test1/NMFresult" + "/" + "result" + "/" + "reslut_" + name[0], c)
    dt = pd.DataFrame(d)
    dt.to_csv('/home/ford/PycharmProjects/test1/NMFresult/distance/distance_sample.csv', index=False, header=False)
    print("存储已结束")

if __name__ == "__main__":
    filepath = "/home/ford/PycharmProjects/test1/voicenumpy"  # 添加路径
    filename = os.listdir(filepath)  # 得到文件夹下的所有文件名称
    for file in filename:
        V = Loaddata(filepath+"/"+file)
        r = Setr()
        W, H,A = NMF(V, r, 5000, 1e-10)
        print(W)
        print("\n")
        print(H)
        print("\n")
        print(W * H)

        save(W,H,W*H,A,file)



