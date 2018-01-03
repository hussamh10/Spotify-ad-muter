import win32gui
import win32api
import win32con
import os

def getwindow(Title="SpotifyMainWindow"):
	return win32gui.FindWindow(Title, None)
	
def getSongInfo():
	try:
            return win32gui.GetWindowText(getwindow())
	except:
            return 'None'

def toggle_mute():
    win32api.keybd_event(0xAD, 0, 0, 0)

while(True):
    mute = False
    if not mute:
        if ('spotify' in getSongInfo().lower()):
            toggle_mute()
            mute = True
    if mute:
        if ('spotify' not in getSongInfo().lower()):
            toggle_mute()
            mute = False
        
