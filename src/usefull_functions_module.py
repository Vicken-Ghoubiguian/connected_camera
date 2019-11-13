import src.terminal_color_codes as terminal_color_codes

def print_howto():
	print(terminal_color_codes.terminal_color_codes.Yellow + """
		Change mode:
		* Normal mode - press any keyboard key
		* Draw mode - press 's'
		* Painting mode - press 'c'
		* Activating face detection - press 'f'
		* Activating eye detection - press 'e'

		multimedia features:
		* Shoot a photo regardless of the mode - press '1'
		* Start/Stop shooting video - press '2'
	""" + terminal_color_codes.terminal_color_codes.ResetAll)
