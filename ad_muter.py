import win32gui
import win32api
import win32con
import os
from time import sleep

def getwindow(Title="SpotifyMainWindow"):
	return win32gui.FindWindow(Title, None)
	
def getSongInfo():
	try:
            return win32gui.GetWindowText(getwindow())
	except:
            return 'None'

def toggle_mute():
    win32api.keybd_event(0xAD, 0, 0, 0)


def main():
    mute = False
    while(True):
        key = 'paint'
        sleep(.2)
        if not mute:
            if (key in getSongInfo().lower()):
                mute = True
                toggle_mute()

        if mute:
            if (key not in getSongInfo().lower()):
                toggle_mute()
                mute = False
main()            
