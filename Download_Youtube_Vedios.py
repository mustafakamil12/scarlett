#This Script to download Vedios from Youtube...!

import os
from pytube import YouTube


def Download_Vedios ():
 user = os.getlogin()
 url = input("Sweety Could you please Enter Youtube Vedio url Link: ")
 #ext = input("Please Enter the Extension of the vedio: ")
 #quality = input("Please Enter The quality of the vedio: ")
 #vedio_path = input ("Enter Path to save the vedio please: ")
 yt = YouTube(url).streams.first().download("C:\\Users\\malogaidi\\Desktop\\F5-Dhari\\")
 #yt = yt.get('mp4', '720p')
 #video.download('C:\Youtube_Vedios\')