import src.terminal_color_codes as terminal_color_codes

def print_howto():

	print(terminal_color_codes.terminal_color_codes.Yellow + """
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 'p'
		* Painting mode - press 'c'
		* Black and white mode - press 'g'

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

def writing_in_log_files_function(desired_log_function, desired_log_to_write):

	log_file = open(desired_log_function, 'a')

	log_file.write(desired_log_to_write)

	log_file.close()
