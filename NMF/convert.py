import filetype
import ffmpeg
from pydub import AudioSegment
import os
import re

def converttowav():
    filepath = "/home/ford/PycharmProjects/test1/cutfile"#添加路径
    filename= os.listdir(filepath) #得到文件夹下的所有文件名称
    for file in filename:
        source=os.path.join(filepath +"/"+ file)
        name = re.findall(r'(.+?)\.', file)
        type = filetype.guess(source)
        print(type)
        if (type.extension!="wav"):
            if(type.extension=='mp3'):
                song = AudioSegment.from_mp3(source)
                song.export(filepath+"/"+name[0]+".wav",format='wav')#转变类型
            if(type.extension=='flac'):
                song = AudioSegment.from_file(source)
                song.export(filepath + "/" + name[0] + ".wav", format='wav')  #转变类型
            os.remove(source)#删除源文件

if __name__ == "__main__":
    converttowav()
