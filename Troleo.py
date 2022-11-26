import sys

from pynput.keyboard import Key, Controller
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