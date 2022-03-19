from tkinter import *
from pytube import YouTube
import time

root = Tk()
root.geometry('500x300')
root.resizable(0,0)
root.title("Descargar video de Youtube")

Label(root,text = 'Descargar video de Youtube', font ='arial 20 bold').pack()

link = StringVar()

Label(root, text = 'Link de Youtube:', font = 'arial 15 bold').place(x= 160 , y = 60)
link_enter = Entry(root, width = 70,textvariable = link).place(x = 32, y = 90)

label = Label(root, text = " ", font = 'arial 15')

def Downloader():
    try:
        url = YouTube(str(link.get()))
        video = url.streams.get_highest_resolution()
        video.download()
        label.config(text = "Descargado")
        label.place(x= 180 , y = 210) 
    except:
        label.config(text = "Asegúrate de que el link sea correcto")
        label.place(x= 70 , y = 210) 

Button(root,text = 'Descargar', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = Downloader).place(x=180 ,y = 150)

root.mainloop()
