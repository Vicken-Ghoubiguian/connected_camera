import cv2
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

	is_activated_profile_face_detection = False

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

		today_as_string = usefull_functions_module.today_as_string_returning_function("%B %d, %Y at %I:%M%p")

		if is_activated_smile_detection == True:

			frame = detection_module.smile_detection_application_function(frame)

		if is_activated_face_detection == True:

			frame = detection_module.frontal_facial_detection_application_function(frame)

		if is_activated_profile_face_detection == True:

			frame = detection_module.profile_facial_detection_application_function(frame)

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

		elif is_current_mode == 'v':

			frame = frame_mode_module.vintage_effect_function(frame)

		elif is_current_mode == 'y':

			frame = frame_mode_module.edge_detection_mode_function(frame)

		else:

			frame = frame

		if c == 27:

			if is_shoting_video == True:

				videoWriter_module.releasing_videoWriter_function(output_video_file)

				output_video_file = None

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.Yellow, "[" + today_as_string + "]: End of video shooting")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: End of video shooting\n")

			break

		if c == ord('1'):

			photography_management_module.shoot_a_photo_function('output_media_files/photos/' + output_photo_name, output_photo_format, frame)

			usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.DarkGray, "[" + today_as_string + "]: Photo shooted")

			usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Photo shooted\n")

		elif c == ord('2'):

			if is_shoting_video == False:

				output_video_file = videoWriter_module.initialisation_of_videoWriter_function('output_media_files/videos/' + output_video_name, output_video_format)

				if output_video_file != None:

					is_shoting_video = True

					usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.Yellow, "[" + today_as_string + "]: Beginning of video shooting")

					usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Beginning of video shooting\n")

				else:

					usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.Red, "[" + today_as_string + "]: Video doesn't shooting")

					usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Video doesn't shooting\n")

			else:

				is_shoting_video = False

				videoWriter_module.releasing_videoWriter_function(output_video_file)

				output_video_file = None

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.Yellow, "[" + today_as_string + "]: End of video shooting")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: End of video shooting\n")

		elif c == ord('p'):

			if is_current_mode != 'p':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of printed mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of printed mode\n")

				is_current_mode = 'p'

		elif c == ord('y'):

			if is_current_mode != 'y':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of edge detection mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of edge detection mode\n")

				is_current_mode = 'y'

		elif c == ord('g'):

			if is_current_mode != 'g':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of black and white mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of black and white mode\n")

				is_current_mode = 'g'

		elif c == ord('v'):

			if is_current_mode != 'v':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of vintage mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of vintage mode\n")

				is_current_mode = 'v'

		elif c == ord('c'):

			if is_current_mode != 'c':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of cartoonized mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of cartoonized mode\n")

				is_current_mode = 'c'

		elif c == ord('o'):

			if is_current_mode != 'o':

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.BackgroundGreen, "[" + today_as_string + "]: Activation of ordinary mode")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Activation of ordinary mode\n")

				is_current_mode = 'o'

		elif c == ord('f'):

			if is_activated_face_detection == True:

				is_activated_face_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightGreen, "[" + today_as_string + "]: Disable facial detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable facial detection\n")

			else:

				is_activated_face_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightGreen, "[" + today_as_string + "]: Enable facial detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable facial detection\n")

		elif c == ord('s'):

			if is_activated_smile_detection == True:

				is_activated_smile_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightMagenta, "[" + today_as_string + "]: Disable smile detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable smile detection\n")

			else:

				is_activated_smile_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightMagenta, "[" + today_as_string + "]: Enable smile detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable smile detection\n")

		elif c == ord('d'):

			if is_activated_profile_face_detection == True:

				is_activated_profile_face_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightMagenta, "[" + today_as_string + "]: Disable profile face detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable profile face detection\n")

			else:

				is_activated_profile_face_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightMagenta, "[" + today_as_string + "]: Enable profile face detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable profile face detection\n")

		elif c == ord('e'):

			if is_activated_eye_detection == True:

				is_activated_eye_detection = False

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable eyes detection\n")

			else:

				is_activated_eye_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightBlue, "[" + today_as_string + "]: Enable eyes detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable eyes detection\n")

		elif c == ord('t'):

			if is_activated_tree_eye_glasses_detection == True:

				is_activated_tree_eye_glasses_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightBlue, "[" + today_as_string + "]: Disable tree eye glasses detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable tree eye glasses detection\n")

			else:

				is_activated_tree_eye_glasses_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightBlue, "[" + today_as_string + "]: Enable tree eye glasses detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable tree eye glasses detection\n")

		elif c == ord('m'):

			if is_activated_mouth_detection == True:

				is_activated_mouth_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightCyan, "[" + today_as_string + "]: Disable mouth detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable mouth detection\n")

			else:

				is_activated_mouth_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.LightCyan, "[" + today_as_string + "]: Enable mouth detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable mouth detection\n")

		elif c == ord('n'):

			if is_activated_nose_detection == True:

				is_activated_nose_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.White, "[" + today_as_string + "]: Disable nose detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable nose detection\n")

			else:

				is_activated_nose_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.White, "[" + today_as_string + "]: Enable nose detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable nose detection\n")

		elif c == ord('l'):

			if is_activated_left_ear_detection == True:

				is_activated_left_ear_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.DarkGray, "[" + today_as_string + "]: Disable left ear detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable left ear detection\n")

			else:

				is_activated_left_ear_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.DarkGray, "[" + today_as_string + "]: Enable left ear detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable left ear detection\n")

		elif c == ord('r'):

			if is_activated_right_ear_detection == True:

				is_activated_right_ear_detection = False

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.DarkGray, "[" + today_as_string + "]: Disable right ear detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Disable right ear detection\n")

			else:

				is_activated_right_ear_detection = True

				usefull_functions_module.writing_in_console_function(terminal_color_codes.terminal_color_codes.DarkGray, "[" + today_as_string + "]: Enable right ear detection")

				usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', "[" + today_as_string + "]: Enable right ear detection\n")

		if is_shoting_video == True:

			videoWriter_module.writing_frame_function(output_video_file, frame)

		cv2.imshow('Connected camera', frame)

	cap.release()

	usefull_functions_module.writing_in_log_files_function('logs/general_logs_file.txt', '-------------------------------------\n')

	cv2.destroyAllWindows()
