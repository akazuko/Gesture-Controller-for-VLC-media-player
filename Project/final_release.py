import cv2
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
	img = cam.getImage().grayscale().adaptiveScale((320,320))
	
	faces = img.findHaarFeatures("/home/ayush/SimpleCV/SimpleCV/Features/HaarCascades/face2.xml")
	noses = img.findHaarFeatures("/home/ayush/SimpleCV/SimpleCV/Features/HaarCascades/nose.xml")
	right_eyes = img.findHaarFeatures("/home/ayush/SimpleCV/SimpleCV/Features/HaarCascades/right_eye.xml")
	left_eyes = img.findHaarFeatures("/home/ayush/SimpleCV/SimpleCV/Features/HaarCascades/lefteye.xml")

	l1 = len(faces)
	l2 = len(noses)
	l4 = len(right_eyes)
	l5 = len(left_eyes)

	nose_x=0
	nose_y=0
	r_eye_x=0
	r_eye_y=0
	l_eye_x=0
	l_eye_y=0
	dim_x=0
	dim_y=0

	if l1 == 1:
		
		limit_x = faces[0].width()
		limit_y = faces[0].height()
		face = faces[0]
		(face_oX,face_oY) = (face.points[0][0],face.points[0][1])
		(dim_x,dim_y) = (face_oX + limit_x,face_oY + limit_y)
	
	elif l1>1:
		faces = faces.sortArea()
		
		limit_x = faces[-1].width()
		limit_y = faces[-1].height()
		face = faces[-1]
		(face_oX,face_oY) = (face.points[0][0],face.points[0][1])
		(dim_x,dim_y) = (face_oX + limit_x,face_oY + limit_y)
	

	if l2 == 1:
		
		(nose_x,nose_y) = noses[0].coordinates()
	
	elif l2>1:
		
		noses = noses.sortArea()	
		(nose_x,nose_y) = noses[-1].coordinates()
	

	if l4 == 1:

		(r_eye_x,r_eye_y) = right_eyes[0].coordinates()
	
	elif l4>1:

		right_eyes = right_eyes.sortArea()
		(r_eye_x,r_eye_y) = right_eyes[-1].coordinates()

	if l5 == 1:

		(l_eye_x,l_eye_y) = left_eyes[0].coordinates()
	
	elif l5>1:
		
		left_eyes = left_eyes.sortArea()
		(l_eye_x,l_eye_y) = left_eyes[-1].coordinates()


	if faces is not None:
		if ((l_eye_x < dim_x and l_eye_y < dim_y) or (r_eye_x < dim_x and r_eye_y < dim_y) or (nose_x < dim_x and nose_y < dim_y)):
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
		time.sleep(0.5)
		
		
	elif(size>1):
		
		check_pos(fists[-1].y)
		time.sleep(0.5)
	




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
		k = cv2.waitKey(33)	
		if k == 27:
			break



#TO ALTER THE VOLUME BASED UPON FIST MOVEMENTS
def Volpy(state):
	print "Volpy" + state
	while True:
		title = check_win()
		
		if "VLC media player" in title:
			fistdetect()
		k = cv2.waitKey(33)	
		if k == 27:
			break


def main():
	print "FEATURE BASED RECOGNITION INITIATED"
	if __name__ == "__main__":
		thread1 = Thread(target = facepy, args = ("active",))
		thread2 = Thread(target = Volpy, args = ("active",))
		thread1.start()
		thread2.start()
		

main()
