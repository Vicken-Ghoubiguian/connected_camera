import cv2

def initialisation_of_videoWriter_function(desired_title, desired_format):

	fourcc_list = {
		".avi": "XVID",
		".mp4": "MP4V"
	}

	if desired_format in fourcc_list:

        	fourcc = cv2.VideoWriter_fourcc(*fourcc_list[desired_format])

        	return cv2.VideoWriter(desired_title + desired_format, fourcc, 20.0, (640,480))

	else:

		return None

def writing_frame_function(desired_videoWriter, desired_frame):

        desired_videoWriter.write(desired_frame)

def releasing_videoWriter_function(desired_videoWriter):

        desired_videoWriter.release()
