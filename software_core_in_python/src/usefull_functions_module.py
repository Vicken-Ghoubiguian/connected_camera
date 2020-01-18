import src.terminal_color_codes as terminal_color_codes
import subprocess
import ffmpeg
from datetime import datetime

def print_howto():

	print(terminal_color_codes.terminal_color_codes.Yellow + """
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 'p'
		* Painting mode - press 'c'
		* Black and white with gray application mode - press 'g'
		* Black and white with RGB application mode - press 'a'
		* Edge detection mode - press 'y'
		* Hue saturation lightness mode - press 'h'
		* Gray and white mode - press 'w'
		* Negative or inverted mode - press 'i'

		Activate body parts detection:
		* Activating face detection - press 'f'
		* Activating profile face detection - press 'd'
		* Activating eye detection - press 'e'
		* Activating tree eye glasses - press 't'
		* Activating smile detection - press 's'
		* Activating mouth detection - press 'm'
		* Activating nose detection - press 'n'
		* Activating right ear detection - press 'r'
		* Activating left ear detection - press 'l'

		Multimedia features:
		* Shoot a photo regardless of the mode - press '1'
		* Start/Stop shooting video - press '2'

		To leave or to quit:
		* To leave or to quit the connected camera - press 'Esc'
	""" + terminal_color_codes.terminal_color_codes.ResetAll)

def today_as_string_returning_function(desired_format):

	today = datetime.today()

	today_as_string = today.strftime(desired_format)

	return today_as_string

def writing_in_console_function(desired_terminal_color_code, desired_log_to_write):

	print(desired_terminal_color_code + desired_log_to_write + terminal_color_codes.terminal_color_codes.ResetAll)

def writing_in_log_files_function(desired_log_file, desired_log_to_write):

	log_file = open(desired_log_file, 'a')

	log_file.write(desired_log_to_write)

	log_file.close()

def merging_audio_file_and_video_file_function(video_file, audio_file, output_file):

	input_video_to_merge = ffmpeg.input(video_file)

	input_audio_to_merge = ffmpeg.input(audio_file)

	ffmpeg.concat(input_video_to_merge, input_audio_to_merge, v=1, a=1).output(output_file).run(overwrite_output=True)

def deleting_buffer_file_function(buffer_video_file):

	subprocess.run(["rm", "-r", buffer_video_file])
