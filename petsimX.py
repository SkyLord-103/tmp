#!/usr/bin/python3
import time
import threading
import sys

import keyboard as kb
from pynput import mouse
from pynput.mouse import Button

print(sys.platform)
# Variables
startStopKey = 'r'
exitKey = 'ctrl+e'


class Application(threading.Thread):
    def __init__(self):
        super(Application, self).__init__()
        self.running = False
        self.programRunning = True

    def start_clicking(self):
        self.running = True

    def stop_clicking(self):
        self.running = False

    def run(self):
        while self.programRunning:
            while self.running:
                usr_mouse.down()
                time.sleep(1)
                usr_mouse.up()
            time.sleep(1)

# python -m PyInstaller your_program.py --onefile --hidden-import=pynput.keyboard._xorg --hidden-import=pynput.mouse._xorg --hidden-import=pynput.keyboard._win32 --hidden-import=pynput.mouse._win32


class Mouse(threading.Thread):
    def __init__(self):
        super(Mouse, self).__init__()

    def down(self):
        mouse.down()

    def up(self):
        mouse.up()


usr_mouse = Mouse()
usr_mouse.start()

App = Application()
App.start()


def on_pressed(key):
    if key == 1:
        if App.programRunning:
            if App.running:
                App.stop_clicking()
            else:
                App.start_clicking()
            print("RUNNING: ", App.running)
    elif key == 0:
        App.exit()
        print("EXITING")


kb.add_hotkey(startStopKey, on_pressed, args=[1],
              suppress=False, timeout=0.1, trigger_on_release=False)
kb.add_hotkey(exitKey, on_pressed, args=[0],
              suppress=False, timeout=0.1, trigger_on_release=False)
