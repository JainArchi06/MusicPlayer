import os
from tkinter.filedialog import askdirectory
import pygame
from mutagen.id3 import ID3
from tkinter import *

root = Tk()
root.minsize(300,300)


listofsongs = []

v = StringVar()
songlabel = Label(root,textvariable=v,width=35)

index = 0

def play(event):#play function
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()

def nextsong(event):#next song  function
    global index
    index += 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def prevsong(event):#previous song function
    global index
    index -= 1
    pygame.mixer.music.load(listofsongs[index])
    pygame.mixer.music.play()
    updatelabel()

def stopsong(event):#stop function
    pygame.mixer.music.stop()
    v.set("")

def updatelabel():
    global index
    global songname
    v.set(listofsongs[index])
    #return songname

def directorychooser():#library calling function

    directory = askdirectory()
    os.chdir(directory)

    for files in os.listdir(directory):
        if files.endswith(".mp3"):

            listofsongs.append(files)


    pygame.mixer.init()
    pygame.mixer.music.load(listofsongs[0])
    pygame.mixer.music.play()
    pygame.mixer.music.pause()


directorychooser()


listbox = Listbox(root,width=50,height=25)
listbox.pack(fill='x',expand=True)

listofsongs.reverse()


for items in listofsongs:
    listbox.insert(0,items)


listofsongs.reverse()



Button1=Button(root,width=5,height=3,text="PLAY", bg='blue')
Button1.pack(fill="x",side='bottom')
Button2=Button(root,width=5,height=3,text="STOP",bg='red')
Button2.pack(fill="x",side='bottom')
Button3=Button(root,width=5,height=3,text="NEXT",bg='yellow')
Button3.pack(fill="y",side='right')
Button4=Button(root,width=5,height=3,text="PREVIOUS",bg='green')
Button4.pack(fill="y",side='left')
label1=LabelFrame(root,text="song name")
label1.pack(fill="both",expand="yes")
Button1.bind("<Button-1>",play)
Button3.bind("<Button-1>",nextsong)
Button4.bind("<Button-1>",prevsong)
Button2.bind("<Button-1>",stopsong)
contents1=Label(label1)
contents1.pack()
root.mainloop()