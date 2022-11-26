import sys
from tkinter import font, messagebox
from tkinter import *
from tkinter import filedialog
from pynput.keyboard import Key, Controller
import pywhatkit as rep
from time import sleep
def troll():
    keyb = Controller()
    delay = 1
    keyb.press(Key.cmd_l)
    sleep(delay)
    keyb.press('q')
    keyb.release('q')
    keyb.release(Key.cmd_l)
    sleep(1)
    keyb.type("Windows PowerShell")
    sleep(delay)
    keyb.press(Key.enter)
    keyb.release(Key.enter)
    sleep(1)
    keyb.type('$Audio = New-Object System.Media.SoundPlayer')
    keyb.press(Key.enter)
    keyb.release(Key.enter)

    keyb.type('$Audio.SoundLocation = \"C:\FelizCumLeandro\z.wav\"')

    keyb.press(Key.enter)
    keyb.release(Key.enter)
    keyb.type('$Audio.Play()')
    keyb.press(Key.enter)
    keyb.release(Key.enter)


    sys.exit()

def denada():
    messagebox.showinfo(message="De nada Crack 😎, ahora no me digas negro por este año", title="🎉🎉🎉🎉🎉")
    rep.playonyt('https://www.youtube.com/watch?v=ePSUMnkXyJM')


root = Tk()
root.geometry("800x420")
root.iconbitmap('C:\FelizCumLeandro\ico\LeandroGOD-icono.ico')
root.configure(background='#FFC7FA')
root.title("FELIZ CUM!🎂🎉🎉🎉")

label0 = Label(root, text="Felices vueltas al sol general B) 😎", bg='#FFC7FA',fg='black', width=0, font=("BubbleGum", 30))
label0.place(x= 70, y= 60)

button1 = Button(root, text='Gracias B)', width=10, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= denada)
button1.place(x=275, y=190)
button2 = Button(root, text='Salir', width=5, height=1, font=('BubbleGum', 30), bg='#FF4131', fg='white', command= troll)
button2.place(x=275, y=300)

root.mainloop()