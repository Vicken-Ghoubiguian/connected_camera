#include "frame_mode_library.hpp"

Mat negative_or_inverted_effect_function(Mat desired_frame)
{
	Mat result_frame;

	bitwise_not(desired_frame, result_frame);

	return result_frame;
}

Mat edge_detection_mode_function(Mat desired_frame)
{
	Mat result_frame;

	Canny(desired_frame, result_frame, 50, 150);

	return result_frame;
}
