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


path = "/home/" + user + "/VLC_Project/Project/XML/fist.xml"

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


def check_pos(y):
	if y<(120):			
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.up_key)
		kebd.release_key(kebd.control_l_key)
	elif y>(120):	
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.down_key)
		kebd.release_key(kebd.control_l_key)


def fistdetect():
	img = cam.getImage().adaptiveScale((320,240)).grayscale()

	fists = img.findHaarFeatures(path)
	
	if fists is not None:
		fists = fists.sortArea()
	
	size = len(fists)

	if(size == 1):
		#fists[0].draw(Color.YELLOW,10)
		check_pos(fists[0].y)
		#print str(fists[0].coordinates())
		
	elif(size>1):
		
		check_pos(fists[-1].y)
	

if "Linux" in os_detect():

	state = 0
	while True:
		title = check_win()
		
		if "VLC media player" in title:
			fistdetect()
else:
	print "Oops, you don't have Ubuntu installed and this project works on that only"
	