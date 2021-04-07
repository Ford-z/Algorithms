import os
import wave
import numpy as np
import pylab as plt
from pydub import AudioSegment


path = "/home/ford/PycharmProjects/test1/cutfile"
files = os.listdir(path)
files = [path + "/" + f for f in files if f.endswith('.wav')]

def setname(WavFileName,i):
    FileName = "/home/ford/PycharmProjects/test1/voice/" + WavFileName[-8:-4] + "-" + str(i + 1) + ".wav"

    return FileName

def cutfile():
    for i in range(len(files)):
        FileName = files[i]
        print("CutFile File Name is ", FileName)
        f = wave.open(r"" + FileName, "rb")
        params = f.getparams()
        print(params)
        nchannels, sampwidth, framerate, nframes = params[:4]

        print("nchannels=%d" % (nchannels))
        print("sampwidth=%d" % (sampwidth))
        print("framerate=%d" % (framerate))
        print("nframes=%d" % (nframes))

        a = nframes  #帧总数
        b = framerate  #采样频率
        total=int(a/b)+1
        for i in range(total):
            start_time = i*1000#以毫秒计算,所以要乘1000
            end_time = (i+1)*1000#以毫秒计算,所以要乘1000

            if(i>=10):
                break#确保一共十段

            sound = AudioSegment.from_wav(FileName)
            sound = sound[start_time:end_time]

            part_wav_path=setname(FileName,i)
            sound.export(part_wav_path, format="wav")

        f.close()

    print("分割已结束")

if __name__ == "__main__":
    cutfile()



