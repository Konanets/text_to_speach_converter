#Йомайо шо не так пішло в житті
#Пряцяє тільки один раз
#QT5 Набагато кращий це я зрозумів уж точно
import tkinter
from tkinter import *
from gtts import gTTS
from playsound import playsound

root = Tk()
root.geometry("350x300")
root.configure(bg = 'ghost white')
root.title("TEXT TO SPEECH")

Label(root, text = "TEXT_TO_SPEECH", font = "arial 20 bold", bg = "white smoke").pack()
Label( font = "arial 15 bold", bg = "white smoke", width = '20').pack(side = 'bottom')

Msg = StringVar()
Label(root, text = "Enter Text", font = 'arial 15 bold', bg = 'white smoke').place(x= 20, y=60)
entry_field = Entry(root, textvariable = Msg , width = '50')
entry_field.place(x = 20, y = 100)


def Text_to_Speech():
    Message = entry_field.get()
    speech = gTTS(text = Message)
    speech.save('music.mp3')
    playsound('music.mp3')


def Exit():
    root.destroy()


def Reset():
    Msg.set("")


Button(root, text = "PLAY", font = 'arial 15 bold' , command = Text_to_Speech, width = '5',fg = 'white', bg = 'Lightgreen').place(x = 25, y = 140)
Button(root , font = 'arial 15 bold', text = 'EXIT', width = '5', command = Exit ,fg = 'white', bg = 'Red').place(x = 100, y = 140)
Button(root, font = 'arial 15 bold', text = 'RESET', width = '5', command = Reset,fg = 'white', bg = 'Orange').place(x = 175, y = 140)

root.mainloop()