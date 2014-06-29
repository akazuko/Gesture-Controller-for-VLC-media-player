import platform
import time
import getpass

import wnck
import gtk

from SimpleCV import Camera, Display, Color
from pykeyboard import PyKeyboard

kebd = PyKeyboard()
cam = Camera()
user = getpass.getuser()
path = "/home/" + user + "/VLC_Project/Project/XML/face2.xml"
def os_detect():
	return platform.system()


def check_win():
	if __name__ == '__main__':
		screen = wnck.screen_get_default()
		screen.force_update()
		while True:
			while gtk.events_pending():
				gtk.main_iteration()
			
			return screen.get_active_window().get_name()


def facedetect():
	img = cam.getImage()

	faces = img.findHaarFeatures(path)
		
	if(faces):
		return 3
	else:
		return 5
				

def simulate():
	kebd.tap_key("space")

os = os_detect()	
if "Linux" in os:

	state = 0
	while True:
		title = check_win()
		
		if "VLC media player" in title:
			face = facedetect()
			if (state == 1 and face ==3):
				simulate()
				state = 0
			elif(state ==0 and face == 5):
				simulate()
				state = 1
else:
	print "Oops, you don't have Ubuntu installed and this project works on that only"
	