import cv2
from pygame import mixer

def initialisation_of_videoWriter_function(desired_title, desired_format, desired_audio_file = 'sounds/16_seconds_old_video_projector_sound.mp3'):

	mixer.init()

	mixer.music.load(desired_audio_file)

	mixer.music.play()

	fourcc = cv2.VideoWriter_fourcc(*fourcc_list[desired_format])

	return cv2.VideoWriter(desired_title + desired_format, fourcc, 20.0, (640,480))

def writing_frame_function(desired_videoWriter, desired_frame):

        desired_videoWriter.write(desired_frame)

def releasing_videoWriter_function(desired_videoWriter):

        desired_videoWriter.release()
