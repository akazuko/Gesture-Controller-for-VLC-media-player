import platform
import time
import getpass

from threading import Thread

import wnck
import gtk

from SimpleCV import Camera, Display, Color
from pykeyboard import PyKeyboard

kebd = PyKeyboard()
cam = Camera()
user = getpass.getuser()


path1 = "/home/" + user + "/VLC_Project/Project/XML/face2.xml"
path2 = "/home/" + user + "/VLC_Project/Project/XML/fist.xml"

#TO DETECT THE OPERATING SYSTEM
def os_detect():
	return platform.system()



#TO CHECK THE NAME OF THE ACTIVE WINDOW (ie. WHAT IS DISPLAYED IN THE TITLE BAR)
def check_win():
	if __name__ == '__main__':
		screen = wnck.screen_get_default()
		screen.force_update()
		while True:
			while gtk.events_pending():
				gtk.main_iteration()
			
			return screen.get_active_window().get_name()



#TO DETECT THE FACE 
def facedetect():
	img = cam.getImage().adaptiveScale((320,240)).grayscale()

	faces = img.findHaarFeatures(path1)
		
	if(faces):
		return 3
	else:
		return 5
				



#TO SIMULATE THE SPACE BAR KEY
def simulate():
	kebd.tap_key("space")



#TO SIMULATE THE VOLUME KEYS UPON FIST MOVEMENTS 
def check_pos(y):
	if y<(120):
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.up_key)
		kebd.release_key(kebd.control_l_key)
	elif y>(120):
		kebd.press_key(kebd.control_l_key)
		kebd.tap_key(kebd.down_key)
		kebd.release_key(kebd.control_l_key)



#TO DETECT THE FIST
def fistdetect():
	img = cam.getImage().adaptiveScale((320,240)).grayscale()

	fists = img.findHaarFeatures(path2)
	
	if fists is not None:
		fists = fists.sortArea()
	
	size = len(fists)

	if(size == 1):
		
		check_pos(fists[0].y)
		
		
	elif(size>1):
		
		check_pos(fists[-1].y)
		
	




#TO PLAY/PAUSE BASED ON THE FACE PRESENCE	
def facepy(stat):	
	print "facepy" + stat	
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



#TO ALTER THE VOLUME BASED UPON FIST MOVEMENTS
def Volpy(state):
	print "Volpy" + state
	while True:
		title = check_win()
		
		if "VLC media player" in title:
			fistdetect()



def main():
	print "FEATURE BASED RECOGNITION INITIATED"
	if __name__ == "__main__":
		thread1 = Thread(target = facepy, args = ("active",))
		thread2 = Thread(target = Volpy, args = ("active",))
		thread1.start()
		thread2.start()

main()
