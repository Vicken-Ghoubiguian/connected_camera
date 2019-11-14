import cv2
import numpy as np

def frontal_facial_detection_application_function(desired_frame, scale_factor = 0.5, scaleFactor = 1.3, minNeighbors = 1):

	face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_alt.xml')

	if face_cascade.empty():

		raise IOError('Unable to load the face cascade classifier xml file')

	face = face_cascade.detectMultiScale(desired_frame, scaleFactor = scaleFactor, minNeighbors = minNeighbors)

	for (face_x, face_y, face_w, face_h) in face:

		cv2.rectangle(desired_frame, (face_x, face_y), (face_x + face_w, face_y + face_h), (0,255,0), 3)

	return desired_frame

def smile_detection_application_function(desired_frame):

	face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_alt.xml')

	smile_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_smile.xml')

	if face_cascade.empty():

                raise IOError('Unable to load the face cascade classifier xml file')

	if smile_cascade.empty():

                raise IOError('Unable to load the smile cascade classifier xml file')

	face = face_cascade.detectMultiScale(desired_frame, scaleFactor=1.05, minNeighbors=5, minSize=(45, 45))

	for (x,y,w,h) in face:

		#cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

		#face_gray = gray[y:y+h, x:x+w]

		face_color = desired_frame[y:y+h, x:x+w]

		smile = smile_cascade.detectMultiScale(face_color, scaleFactor=1.7, minNeighbors=3, minSize=(15, 15))

		for (ex,ey,ew,eh) in smile:

			cv2.rectangle(face_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),1)

	return desired_frame

def eye_detection_application_function(desired_frame):

	eye_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_eye.xml')

	face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_default.xml')

	if face_cascade.empty():

                raise IOError('Unable to load the face cascade classifier xml file')

	if eye_cascade.empty():

		raise IOError('Unable to load the eye cascade classifier xml file')

	face = face_cascade.detectMultiScale(desired_frame, 1.3, 5)

	for (face_x, face_y, face_w, face_h) in face:

		roi_color = desired_frame[face_y : face_y + face_h, face_x : face_x + face_w]

		eyes = eye_cascade.detectMultiScale(roi_color)

		for (eyes_x, eyes_y, eyes_w, eyes_h) in eyes:

			cv2.rectangle(roi_color,(eyes_x, eyes_y),(eyes_x + eyes_w, eyes_y + eyes_h), (250,0,0), 2)

	return desired_frame
