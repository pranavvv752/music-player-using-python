import tkinter as tk
import fnmatch
import os
from pygame import mixer


canvas=tk.Tk()
canvas.title("music player")
canvas.geometry("600x800")
canvas.config(bg="sky blue")

listBox=tk.Listbox(canvas,fg="cyan",bg="black",width="100")
listBox.pack(padx=15,pady=15)

root="C:\\Users\\Asus\\Desktop\\music"
pattern="*.mp3"
mixer.init()

for root,dirs,files in os.walk(root):
    for filename in fnmatch.filter(files,pattern):
        listBox.insert('end',filename)


    def select():
        button1.config(text=("play "))
        mixer.music.load(root + "\\" + listBox.get("anchor"))
        mixer.music.play()
    def stop():
        button2.config(text=("pause"))
        mixer.music.load(root + "\\" + listBox.get("anchor"))
        mixer.music.stop()


    def next():
        next_song=listBox.curselection()
        next_song=next_song[0]+1
        mixer.music.load(root + "\\" + listBox.get(next_song))
        mixer.music.play()
        listBox.select_clear(0,'end')
        listBox.activate(next_song)
        listBox.select_set(next_song)


    def prev():
        next_song = listBox.curselection()
        next_song = next_song[0] - 1
        mixer.music.load(root + "\\" + listBox.get(next_song))
        mixer.music.play()
        listBox.select_clear(0, 'end')
        listBox.activate(next_song)
        listBox.select_set(next_song)


button1=tk.Button(canvas,text="play",width=20,command=select)
button1.pack(pady=10)
button2=tk.Button(canvas,text="pause",width=20,command=stop)
button2.pack(pady=10)
button3=tk.Button(canvas,text="next",width=25,command=next)
button3.pack(pady=10)
button4=tk.Button(canvas,text="previous",width=25,command=prev)
button4.pack(pady=10)

canvas.mainloop()