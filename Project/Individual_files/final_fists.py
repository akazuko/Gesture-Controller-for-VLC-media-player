import platform
import time
import getpass

import wnck
import gtk

from SimpleCV import Camera, Display, Color
from pykeyboard import PyKeyboard
from pymouse import PyMouse

kebd = PyKeyboard()
cam = Camera()
m = PyMouse()
user = getpass.getuser()
(Sz_x,Sz_y) = m.screen_size()
d = Display()

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
	if y<(110):
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.up_key)
		kebd.release_key(kebd.control_l_key)
	elif y>(350):
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.down_key)
		kebd.release_key(kebd.control_l_key)


def fistdetect():
	img = cam.getImage()

	fists = img.findHaarFeatures(path)
	
	if fists is not None:
		fists = fists.sortArea()
	
	size = len(fists)

	if(size == 1):
		fists[0].draw(Color.YELLOW,10)
		check_pos(fists[0].y)
		#print str(fists[0].coordinates())
		
	elif(size>1):
		fists[-1].draw(Color.YELLOW,10)
		check_pos(fists[-1].y)
		#print str(fists[-1].coordinates())
	img.save(d)	


state = 0
while True:
	title = check_win()
	
	if "VLC media player" in title:
		fistdetect()

	