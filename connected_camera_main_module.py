import cv2
import numpy as np

def print_howto():
	print("""
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 's'
		* Painting mode - press 'c'

		multimedia features:
		* Shoot a photo regardless of the mode - press '1'
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

def exploits_function(title):

	print_howto()

	cap = cv2.VideoCapture(0)

	current_mode = None

	is_shoting_video = False

	output_video_file = initialisation_of_videoWriter_function(title)

	while True:

		ret, frame = cap.read()

		c = cv2.waitKey(1)

		if c == 27:

			break

		if (c >= 97 and c <= 122) and c != current_mode:

			current_mode = c

		if current_mode == ord('s'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = True)

		elif current_mode == ord('c'):

			frame = cartoonizing_image_function(frame, ksize = 5, sketch_mode = False)

		if c == ord('1'):

			shoot_a_photo_function('monImg',frame)

		elif c == ord('2'):

			if is_shoting_video == False:

				is_shoting_video = True

				print('Beginning of video shooting...')

			else:

				is_shoting_video = False

				print('End of video shooting...')

		writing_frame_function(output_video_file, frame)

		cv2.imshow('Cartoonization', frame)

	cap.release()

	releasing_videoWriter_function(output_video_file)

	cv2.destroyAllWindows()

if __name__ == '__main__':

	exploits_function('outputVideo')
