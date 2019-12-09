import cv2
import numpy as np

def negative_or_inverted_effect_function(desired_frame):

	frame_with_negative_or_inverted_effect = cv2.bitwise_not(desired_frame)

	return frame_with_negative_or_inverted_effect

def vintage_effect_function(desired_frame):

	desired_frame_rows, desired_frame_cols = desired_frame.shape[:2]

	#Creation of the gaussian filter
	kernel_x = cv2.getGaussianKernel(desired_frame_cols,200)
	kernel_y = cv2.getGaussianKernel(desired_frame_rows,200)
	kernel = kernel_y * kernel_x.T

	filter = 255 * kernel / np.linalg.norm(kernel)
	vintage_desired_frame = np.copy(desired_frame)

	#Application of filter
	for i in range(3):

		vintage_desired_frame[:,:,i] = vintage_desired_frame[:,:,i] * filter

	return vintage_desired_frame

def edge_detection_mode_function(desired_frame):

	frame_with_edge_detection_mode = cv2.Canny(desired_frame,100,300)

	return frame_with_edge_detection_mode

def gray_and_white_effect_function(desired_frame):

	gray_and_white_frame = cv2.cvtColor(desired_frame, cv2.COLOR_BGR2GRAY)

	return gray_and_white_frame

def hue_saturation_lightness_effect_function(desired_frame):

	hue_saturation_lightness_frame = cv2.cvtColor(desired_frame, cv2.COLOR_BGR2HSV)

	return hue_saturation_lightness_frame

def black_and_white_frame_converting_function(desired_frame):

	grayed_frame = cv2.cvtColor(desired_frame, cv2.COLOR_BGR2GRAY)

	ret, black_and_white_frame = cv2.threshold(grayed_frame, 127, 255, cv2.THRESH_BINARY)

	return black_and_white_frame

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
