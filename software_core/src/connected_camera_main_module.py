import cv2
from datetime import datetime
import src.frame_mode_module as frame_mode_module
import src.terminal_color_codes as terminal_color_codes
import src.detection_module as detection_module
import src.usefull_functions_module as usefull_functions_module
import src.videoWriter_module as videoWriter_module
import src.photography_management_module as photography_management_module

def exploits_function(output_video_name, output_video_format, output_photo_name, output_photo_format):

	usefull_functions_module.print_howto()

	cap = cv2.VideoCapture(0)

	is_shoting_video = False

	is_activated_face_detection = False

	is_activated_eye_detection = False

	is_activated_tree_eye_glasses_detection = False

	is_activated_smile_detection = False

	is_activated_mouth_detection = False

	is_activated_left_ear_detection = False

	is_activated_right_ear_detection = False

	is_activated_nose_detection = False

	is_current_mode = 'o'

	output_video_file = None

	usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', '-------------------------------------\n')

	while True:

		ret, frame = cap.read()

		c = cv2.waitKey(1)

		today = datetime.today()

		today_as_string = today.strftime("%B %d, %Y at %I:%M%p")

		if is_activated_smile_detection == True:

			frame = detection_module.smile_detection_application_function(frame)

		if is_activated_face_detection == True:

			frame = detection_module.frontal_facial_detection_application_function(frame)

		if is_activated_eye_detection == True:

			frame = detection_module.eye_detection_application_function(frame)

		if is_activated_tree_eye_glasses_detection == True:

			frame = detection_module.eye_tree_eyeglasses_detection_application_function(frame)

		if is_activated_mouth_detection == True:

			frame = detection_module.mouth_detection_application_function(frame)

		if is_activated_nose_detection == True:

			frame = detection_module.nose_detection_application_function(frame)

		if is_activated_left_ear_detection == True:

			frame = detection_module.left_ear_detection_application_function(frame)

		if is_activated_right_ear_detection == True:

			frame = detection_module.right_ear_detection_application_function(frame)

		if is_current_mode == 'p':

			frame = frame_mode_module.cartoonizing_image_function(frame, ksize = 5, sketch_mode = True)

		elif is_current_mode == 'c':

			frame = frame_mode_module.cartoonizing_image_function(frame, ksize = 5, sketch_mode = False)

		elif is_current_mode == 'g':

			frame = frame_mode_module.black_and_white_frame_converting_function(frame)

		else:

			frame = frame

		if c == 27:

			if is_shoting_video == True:

				videoWriter_module.releasing_videoWriter_function(output_video_file)

				output_video_file = None

				print(terminal_color_codes.terminal_color_codes.Yellow + "[" + today_as_string + "]: End of video shooting" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: End of video shooting\n")

			break

		if c == ord('1'):

			photography_management_module.shoot_a_photo_function('output_media_files/photos/' + output_photo_name, output_photo_format, frame)

			print(terminal_color_codes.terminal_color_codes.DarkGray + "[" + today_as_string + "]: Photo shooted" + terminal_color_codes.terminal_color_codes.ResetAll)

			usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Photo shooted\n")

		elif c == ord('2'):

			if is_shoting_video == False:

				output_video_file = videoWriter_module.initialisation_of_videoWriter_function('output_media_files/videos/' + output_video_name, output_video_format)

				if output_video_file != None:

					is_shoting_video = True

					print(terminal_color_codes.terminal_color_codes.Yellow + "[" + today_as_string + "]: Beginning of video shooting" + terminal_color_codes.terminal_color_codes.ResetAll)

					usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Beginning of video shooting\n")

				else:

					print(terminal_color_codes.terminal_color_codes.Red + "[" + today_as_string + "]: Video doesn't shooting" + terminal_color_codes.terminal_color_codes.ResetAll)

					usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Video doesn't shooting\n")

			else:

				is_shoting_video = False

				videoWriter_module.releasing_videoWriter_function(output_video_file)

				output_video_file = None

				print(terminal_color_codes.terminal_color_codes.Yellow + "[" + today_as_string + "]: End of video shooting" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: End of video shooting\n")

		elif c == ord('p'):

			if is_current_mode != 'p':

				print(terminal_color_codes.terminal_color_codes.BackgroundGreen + "[" + today_as_string + "]: Activation of printed mode" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of printed mode\n")

				is_current_mode = 'p'

		elif c == ord('g'):

			if is_current_mode != 'g':

				print(terminal_color_codes.terminal_color_codes.BackgroundGreen + "[" + today_as_string + "]: Activation of black and white mode" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of black and white mode\n")

				is_current_mode = 'g'

		elif c == ord('c'):

			if is_current_mode != 'c':

				print(terminal_color_codes.terminal_color_codes.BackgroundGreen + "[" + today_as_string + "]: Activation of cartoonized mode" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of cartoonized mode\n")

				is_current_mode = 'c'

		elif c == ord('o'):

			if is_current_mode != 'o':

				print(terminal_color_codes.terminal_color_codes.BackgroundGreen + "[" + today_as_string + "]: Activation of ordinary mode" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of ordinary mode\n")

				is_current_mode = 'o'

		elif c == ord('f'):

			if is_activated_face_detection == True:

				is_activated_face_detection = False

				print(terminal_color_codes.terminal_color_codes.LightGreen + "[" + today_as_string + "]: Disable facial detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable facial detection\n")

			else:

				is_activated_face_detection = True

				print(terminal_color_codes.terminal_color_codes.LightGreen + "[" + today_as_string + "]: Enable facial detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable facial detection\n")

		elif c == ord('s'):

			if is_activated_smile_detection == True:

				is_activated_smile_detection = False

				print(terminal_color_codes.terminal_color_codes.LightMagenta + "[" + today_as_string + "]: Disable smile detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable smile detection\n")

			else:

				is_activated_smile_detection = True

				print(terminal_color_codes.terminal_color_codes.LightMagenta + "[" + today_as_string + "]: Enable smile detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable smile detection\n")

		elif c == ord('e'):

			if is_activated_eye_detection == True:

				is_activated_eye_detection = False

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Disable eyes detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable eyes detection\n")

			else:

				is_activated_eye_detection = True

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Enable eyes detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable eyes detection\n")

		elif c == ord('t'):

			if is_activated_tree_eye_glasses_detection == True:

				is_activated_tree_eye_glasses_detection = False

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Disable tree eye glasses detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable tree eye glasses detection\n")

			else:

				is_activated_tree_eye_glasses_detection = True

				print(terminal_color_codes.terminal_color_codes.LightBlue + "[" + today_as_string + "]: Enable tree eye glasses detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable tree eye glasses detection\n")

		elif c == ord('m'):

			if is_activated_mouth_detection == True:

				is_activated_mouth_detection = False

				print(terminal_color_codes.terminal_color_codes.LightCyan + "[" + today_as_string + "]: Disable mouth detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable mouth detection\n")

			else:

				is_activated_mouth_detection = True

				print(terminal_color_codes.terminal_color_codes.LightCyan + "[" + today_as_string + "]: Enable mouth detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable mouth detection\n")

		elif c == ord('n'):

			if is_activated_nose_detection == True:

				is_activated_nose_detection = False

				print(terminal_color_codes.terminal_color_codes.White + "[" + today_as_string + "]: Disable nose detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable nose detection\n")

			else:

				is_activated_nose_detection = True

				print(terminal_color_codes.terminal_color_codes.White + "[" + today_as_string + "]: Enable nose detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable nose detection\n")

		elif c == ord('l'):

			if is_activated_left_ear_detection == True:

				is_activated_left_ear_detection = False

				print(terminal_color_codes.terminal_color_codes.DarkGray + "[" + today_as_string + "]: Disable left ear detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable left ear detection\n")

			else:

				is_activated_left_ear_detection = True

				print(terminal_color_codes.terminal_color_codes.DarkGray + "[" + today_as_string + "]: Enable left ear detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable left ear detection\n")

		elif c == ord('r'):

			if is_activated_right_ear_detection == True:

				is_activated_right_ear_detection = False

				print(terminal_color_codes.terminal_color_codes.DarkGray + "[" + today_as_string + "]: Disable right ear detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable right ear detection\n")

			else:

				is_activated_right_ear_detection = True

				print(terminal_color_codes.terminal_color_codes.DarkGray + "[" + today_as_string + "]: Enable right ear detection" + terminal_color_codes.terminal_color_codes.ResetAll)

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable right ear detection\n")

		if is_shoting_video == True:

			videoWriter_module.writing_frame_function(output_video_file, frame)

		cv2.imshow('Connected camera', frame)

	cap.release()

	usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', '-------------------------------------\n')

	cv2.destroyAllWindows()