import cv2
from pygame import mixer

def shoot_a_photo_function(title, desired_frame, desired_format = '.jpg', desired_audio_file = '/home/eric/connected_camera/sounds/1_second_long_old_camera_sound.mp3'):

	mixer.init()

	mixer.music.load(desired_audio_file)

	mixer.music.play()

	cv2.imwrite(title + desired_format, desired_frame)
