import time
from datetime import datetime
from pynput.keyboard import Controller,Key
from data import lst
import webbrowser

isStarted= False
keyboard= Controller()

for i in lst:
    while True:
        if isStarted== False:
            if datetime.now().hour== int(i[1].split(':')[0]) and datetime.now().minute== int(i[1].split(':')[1]):
                webbrowser.open(i[0])
                isStarted=True
        elif isStarted==True:
             if datetime.now().hour== int(i[2].split(':')[0]) and datetime.now().minute== int(i[2].split(':')[1]):
                 keyboard.press('x')
                 time.sleep(1)
                 keyboard.press(key.enter)
                 isStarted=False
                 break







