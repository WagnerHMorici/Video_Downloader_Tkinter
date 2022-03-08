from tkinter import *
from download_funcs import Download


root = Tk()
root.geometry("400x200")
root.title("Video Downloader")


def videodown():
    Download.download_video(link.get())


Label(root, text="Digite o Link:").place(x=10, y=10, width=100, height=20)

link = Entry(root)
link.place(x=110, y=10, width=250, height=20)


btnvideo = Button(root, text="Download Video", command=videodown)
btnvideo.place(x=240, y=35, width=100, height=20)


root.mainloop()
