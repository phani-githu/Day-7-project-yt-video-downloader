from pytube import YouTube
from tkinter import *
root = Tk()
root.geometry("250x320")
root.title("YouTube Video Downloader")
def youtube():
    a= var.get() #https://www.youtube.com/watch?v=C81nqlBD3wg
    video = YouTube(a).streams.filter(progressive = True,file_extension = "mp4").order_by('resolution').desc().first()
    video.download(r"C:\Users\USER\OneDrive\Desktop\12-10-2020")

l1 = Label(text = "YouTube video Downloader", fg = "black", font = ("bold",33))
l1.place(x=420,y=25)
var = StringVar()
entry_1 = Entry(root,textvariable=var,width=55)
entry_1.place(x=500,y=100)
button_1 = Button(root,text = "Click on the tab to Downloade the video" ,command = youtube,bg = "red",width = 35,fg = "white",font = 10)
button_1.place(x=505,y=150)



root.mainloop()