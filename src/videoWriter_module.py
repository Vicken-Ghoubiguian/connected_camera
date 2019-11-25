import cv2

def initialisation_of_videoWriter_function(desired_title):

        fourcc = cv2.VideoWriter_fourcc(*'MP4V')

        return cv2.VideoWriter(desired_title + '.mp4', fourcc, 20.0, (640,480))

def writing_frame_function(desired_videoWriter, desired_frame):

        desired_videoWriter.write(desired_frame)

def releasing_videoWriter_function(desired_videoWriter):

        desired_videoWriter.release()
