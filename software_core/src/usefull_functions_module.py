import src.terminal_color_codes as terminal_color_codes
from datetime import datetime

def print_howto():

	print(terminal_color_codes.terminal_color_codes.Yellow + """
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 'p'
		* Painting mode - press 'c'
		* Black and white mode - press 'g'
		* Edge detection mode - press 'y'

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
