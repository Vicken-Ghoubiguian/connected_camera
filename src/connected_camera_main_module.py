import cv2
import time
import numpy as np
import src.terminal_color_codes as terminal_color_codes
from datetime import datetime

def print_howto():
	print("""
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 's'
		* Painting mode - press 'c'
		* Activating face detection - press 'f'
		* Activating eye detection - press 'e'

		multimedia features:
		* Shoot a photo regardless of the mode - press '1'
		* Start/Stop shooting video - press '2'
	""")

def cartoonizing_image_function(img, ksize = 5, sketch_mode = False):

	#Definition of variables with respectives values
	num_repetitions, sigma_color, sigma_space, ds_factor = 10, 5, 7, 4

	#Convert image to grayscale
	img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

	#Apply median filter to the grayscale image
	img_gray = cv2.medianBlur(img_gray, 7)

	#Detect edges in the image and threshold it
	edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = ksize)
	ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

	#'mask' is the sketch of the image
	if sketch_mode:

		return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)

	#Resize the image to a smaller size for faster computation
	img_small = cv2.resize(img, None, fx = 1.0/ds_factor, fy = 1.0/ds_factor, interpolation = cv2.INTER_AREA)

	#Apply bilateral filter the image multiple times
	for i in range(num_repetitions):
		img_small = cv2.bilateralFilter(img_small, ksize, sigma_color, sigma_space)

	img_output = cv2.resize(img_small, None, fx = ds_factor, fy = ds_factor, interpolation = cv2.INTER_LINEAR)

	dst = np.zeros(img_gray.shape)

	#Add the thick boundary lines to the image using 'AND' operator
	dst = cv2.bitwise_and(img_output, img_output, mask = mask)

	return dst

def shoot_a_photo_function(title, desired_frame):

	cv2.imwrite(title + '.jpg', desired_frame, [cv2.IMWRITE_JPEG_QUALITY, 90])

def initialisation_of_videoWriter_function(desired_title):

	fourcc = cv2.VideoWriter_fourcc(*'MP4V')

	return cv2.VideoWriter(desired_title + '.mp4', fourcc, 20.0, (640,480))

def writing_frame_function(desired_videoWriter, desired_frame):

	desired_videoWriter.write(desired_frame)

def releasing_videoWriter_function(desired_videoWriter):

	desired_videoWriter.release()

def frontal_facial_detection_application_function(desired_frame, scale_factor = 0.5, scaleFactor = 1.3, minNeighbors = 1):

	face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_alt.xml')

	if face_cascade.empty():

		raise IOError('Unable to load the face cascade classifier xml file')

	face = face_cascade.detectMultiScale(desired_frame, scaleFactor = scaleFactor, minNeighbors = minNeighbors)

	for (face_x, face_y, face_w, face_h) in face:

		cv2.rectangle(desired_frame, (face_x, face_y), (face_x + face_w, face_y + face_h), (0,255,0), 3)

	return desired_frame

def eye_detection_application_function(desired_frame):

	eye_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_eye.xml')

	face_cascade = cv2.CascadeClassifier('haarcascade_files/haarcascade_frontalface_alt.xml')

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

def exploits_function(title):

	print_howto()

	cap = cv2.VideoCapture(0)

	current_mode = None

	is_shoting_video = False

	is_activated_face_detection = False

	is_activated_eye_detection = False

	starting_stopwatch_time = 0

	stoping_stopwatch_time = 0

	output_video_file = initialisation_of_videoWriter_function(title)

	while True:

		ret, frame = cap.read()

		c = cv2.waitKey(1)

		today = datetime.today()

		today_as_string = today.strftime("%B %d, %Y at %I:%M%p")

		if c == 27:

			break

		if (c >= 97 and c <= 122) and c != current_mode:

			current_mode = c

		if current_mode == ord('s'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = True)

		elif current_mode == ord('c'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = False)

		if c == ord('1'):

			shoot_a_photo_function('output_media_files/monImg', frontal_facial_detection_application_function(frame))

		elif c == ord('2'):

			if is_shoting_video == False:

				is_shoting_video = True

				starting_stopwatch_time = int(time.time())

				stoping_stopwatch_time = int(time.time())

				print('Beginning of video shooting...' + str(stoping_stopwatch_time - starting_stopwatch_time))
			else:

				is_shoting_video = False

				stoping_stopwatch_time = int(time.time())

				print('End of video shooting...' + str(stoping_stopwatch_time - starting_stopwatch_time))

		elif c == ord('f'):

			if is_activated_face_detection == True:

				is_activated_face_detection = False

				print(terminal_color_codes.terminal_color_codes.LightYellow + "[" + today_as_string + "]: Disable facial detection" + terminal_color_codes.terminal_color_codes.ResetAll)

			else:

				is_activated_face_detection = True

				print("[" + today_as_string + "]: Enable facial detection")

		elif c == ord('e'):

			if is_activated_eye_detection == True:

				is_activated_eye_detection = False

				print("[" + today_as_string + "]: Disable eyes detection")

			else:

				is_activated_eye_detection = True

				print("[" + today_as_string + "]: Enable eyes detection")

		writing_frame_function(output_video_file, frame)

		if is_activated_face_detection == True:

			frame = frontal_facial_detection_application_function(frame)

		if is_activated_eye_detection == True:

			frame = eye_detection_application_function(frame)

		cv2.imshow('Cartoonization', frame)

	cap.release()

	releasing_videoWriter_function(output_video_file)

	cv2.destroyAllWindows()
