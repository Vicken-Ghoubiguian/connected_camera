import argparse
import src.connected_camera_main_module as main_module

if __name__ == '__main__':

	arguments_parser = argparse.ArgumentParser()

	arguments_parser.add_argument('-output_video_name', action = 'store', dest = 'output_video_name', default = 'outputVideo', help = 'Store the video name informed by the user')
	arguments_parser.add_argument('-output_video_format', action = 'store', dest = 'output_video_format', default = '.avi', help = 'Store the video name informed by the user')
	arguments_parser.add_argument('-photo_name', action = 'store', dest = 'photo_name', default = 'monImg', help = 'Store the photo name informed by the user')
	arguments_parser.add_argument('-photo_format', action = 'store', dest = 'photo_format', default = '.jpg', help = 'Store the photo format informed by the user')

	arguments_results = arguments_parser.parse_args()

	main_module.exploits_function(arguments_results.output_video_name, arguments_results.output_video_format, arguments_results.photo_name, arguments_results.photo_format)
