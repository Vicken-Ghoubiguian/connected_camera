#include "frame_mode_library.hpp"

Mat frame_mode::negative_or_inverted_effect_function(Mat desired_frame)
{
	Mat result_frame;

	bitwise_not(desired_frame, result_frame);

	return result_frame;
}

Mat frame_mode::edge_detection_mode_function(Mat desired_frame)
{
	Mat result_frame;

	Canny(desired_frame, result_frame, 50, 150);

	return result_frame;
}

Mat frame_mode::hue_saturation_lightness_effect_function(Mat desired_frame)
{
	Mat result_frame;

	cvtColor(desired_frame, result_frame, COLOR_BGR2HSV);

	return result_frame;
}

Mat frame_mode::gray_and_white_effect_function(Mat desired_frame)
{
	Mat result_frame;

	cvtColor(desired_frame, result_frame, COLOR_BGR2HSV);

	return result_frame;
}
