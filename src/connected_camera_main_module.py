import cv2
import time
import numpy as np
import src.terminal_color_codes as terminal_color_codes
import src.detection_module as detection_module
import src.usefull_functions_module as usefull_functions_module
from datetime import datetime

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

def exploits_function(title):

	usefull_functions_module.print_howto()

	cap = cv2.VideoCapture(0)

	current_mode = None

	is_shoting_video = False

	is_activated_face_detection = False

	is_activated_eye_detection = False

	is_activated_smile_detection = False

	is_activated_mouth_detection = False

	is_activated_left_ear_detection = False

	is_activated_right_ear_detection = False

	is_activated_nose_detection = False

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

		if current_mode == ord('p'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = True)

		elif current_mode == ord('c'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = False)

		if c == ord('1'):

			shoot_a_photo_function('output_media_files/monImg', detection_module.frontal_facial_detection_application_function(frame))

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

				print(terminal_color_codes.terminal_color_codes.LightGreen + "[" + today_as_string + "]: Disable facial detection" + terminal_color_codes.terminal_color_codes.ResetAll)

			else:

				is_activated_face_detection = True

				print(terminal_color_codes.terminal_color_codes.LightGreen + "[" + today_as_string + "]: Enable facial detection" + terminal_color_codes.terminal_color_codes.ResetAll)

		elif c == ord('s'):

			if is_activated_smile_detection == True:

				is_activated_smile_detection = False

				print(terminal_color_codes.terminal_color_codes.LightMagenta + "[" + today_as_string + "]: Disable smile detection" + terminal_color_codes.terminal_color_codes.ResetAll)

			else:

				is_activated_smile_detection = True

				print(terminal_color_codes.terminal_color_codes.LightMagenta + "[" + today_as_string + "]: Enable smile detection" + terminal_color_codes.terminal_color_codes.ResetAll)

		elif c == ord('e'):

			if is_activated_eye_detection == True:

				is_activated_eye_detection = False

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Disable eyes detection" + terminal_color_codes.terminal_color_codes.ResetAll)

			else:

				is_activated_eye_detection = True

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Enable eyes detection" + terminal_color_codes.terminal_color_codes.ResetAll)

		elif c == ord('m'):

			if is_activated_mouth_detection == True:

				is_activated_mouth_detection = False

				print(terminal_color_codes.terminal_color_codes.LightCyan + "[" + today_as_string + "]: Disable mouth detection" + terminal_color_codes.terminal_color_codes.ResetAll)

			else:

				is_activated_mouth_detection = True

				print(terminal_color_codes.terminal_color_codes.LightCyan + "[" + today_as_string + "]: Enable mouth detection" + terminal_color_codes.terminal_color_codes.ResetAll)

		elif c == ord('n'):

			if is_activated_nose_detection == True:

				is_activated_nose_detection = False

			else:

				is_activated_nose_detection = True

		elif c == ord('l'):

			if is_activated_left_ear_detection == True:

				is_activated_left_ear_detection = False

			else:

				is_activated_left_ear_detection = True

		elif c == ord('r'):

			if is_activated_right_ear_detection == True:

				is_activated_right_ear_detection = False

			else:

				is_activated_right_ear_detection = True

		writing_frame_function(output_video_file, frame)

		if is_activated_smile_detection == True:

			frame = detection_module.smile_detection_application_function(frame)

		if is_activated_face_detection == True:

			frame = detection_module.frontal_facial_detection_application_function(frame)

		if is_activated_eye_detection == True:

			frame = detection_module.eye_detection_application_function(frame)

		if is_activated_mouth_detection == True:

			frame = detection_module.mouth_detection_application_function(frame)

		if is_activated_nose_detection == True:

			frame = detection_module.nose_detection_application_function(frame)

		if is_activated_left_ear_detection == True:

			frame = detection_module.left_ear_detection_application_function(frame)

		if is_activated_right_ear_detection == True:

			frame = detection_module.right_ear_detection_application_function(frame)

		cv2.imshow('Cartoonization', frame)

	cap.release()

	releasing_videoWriter_function(output_video_file)

	cv2.destroyAllWindows()
