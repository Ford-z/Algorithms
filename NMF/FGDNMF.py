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

np.set_printoptions(suppress=True)#不使用科学计数法

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

def BetterNMF(V, r, k, error):
    m,n=shape(V) #得到目地矩阵的行和列#
    W = mat(random.random(size=(m, r)))#设定权重矩阵中随机数值#
    H = mat(random.random(size=(r, n)))#设定特征矩阵中随机数值#

    b=[]
    delta=0.0
    deltaW=0.0
    beta=0.5
    alpha=0.5
    yura=0.5
    l=0.0
    theta=0.0
    theta1=0.0
    theta2=0.00002

    I = mat(random.random(size=(m, n)))  #建立对角矩阵
    for i in range(m):
        for j in range(n):
            if(i==j):
                I[i, j] = 1
            else:
                I[i,j]=0

    E = mat(random.random(size=(m, n)))  #建立矩形的单位矩阵
    for i in range(m):
        for j in range(n):
            E[i, j] = 1

    e=E-I
    S=mat(np.random.randint(0,2,(m,n)))
    D=mat(np.random.randint(0,2,(m,n)))

    for x in range(k):
        V_new = W * H  # V=W*H#
        D1 = V_new - V
        distance = 0.0  # 初始化#
        for i in range(m):
            for j in range(n):
                distance = D1[i, j] * D1[i, j]  # 欧式距离#
        b.append(distance)
        #print(distance)

        if distance < error:
            print(distance)
            break

        a_num = transpose(W) * V
        a_den = transpose(W) * W * H
        a_extra = transpose(W) * E
        HS=H*S
        HD=H*D

        V_new = W * H
        for i in range(r):
            for j in range(n):
                if  (a_extra[i, j] + beta * H[i, j] + yura *HD[i,j])!=0:
                    delta = H[i, j] * ((a_num[i, j] / V_new[i, j]) + yura*HS[i,j]) / (a_extra[i, j] + beta * H[i, j] + yura *HD[i,j])-H[i,j]
                    if(H[i,j]-delta)>=0:
                        l=H[i,j]
                    else:
                        l=delta
                    theta1=0.00001+0.00001*l#方便与0.00002比较
                    if (theta1 - theta2) >= 0:
                        theta=theta2
                    else:
                        theta = theta1#选择更好的步长
                    H[i,j]=H[i,j]-theta*delta

        b_num = V * transpose(H)  # 不能同时设定两个更新方则，不然会相互影响#
        b_den = W * H * transpose(H)
        b_extra = E * transpose(H)

        V_new = W * H
        for i in range(m):
            for j in range(r):
                if (b_extra[i, j] + alpha * W[i,j]*e[i,j])!=0:
                    deltaW = W[i, j] * (b_num[i, j] / V_new[i, j] / (b_extra[i, j] + alpha * W[i,j]*e[i,j]))-W[i,j]
                    if (W[i, j] - deltaW) >= 0:
                        l = W[i, j]
                    else:
                        l = deltaW
                    theta1 = 0.00001 + 0.00001 * l
                    if (theta1 - theta2) >= 0:
                        theta = theta2
                    else:
                        theta = theta1#选择更好的步长
                    W[i,j]=W[i,j]-theta*deltaW
    print("优化算法运行已结束")
    return b

def save2(G):
    df = pd.DataFrame(G)
    df.to_csv('./NMFresult/distance/distance_better.csv', index=False, header=False)
    print("存储已结束")

if __name__ == "__main__":
    filepath = "./voicenumpy"  # 添加路径
    filename = os.listdir(filepath)  # 得到文件夹下的所有文件名称
    for file in filename:
        V = Loaddata(filepath+"/"+file)
        r = Setr()
        G=BetterNMF(V,r,5000,1e-10)
        save(G)