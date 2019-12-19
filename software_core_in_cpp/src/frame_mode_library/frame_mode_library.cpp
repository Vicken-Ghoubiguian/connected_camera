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

Mat frame_mode::cartoonizing_image_function(Mat desired_frame)
{
	Mat gray_frame, edge_frame, edge_preserving_frame, cartoonized_image;

	//Convert to gray scale
    	cvtColor(desired_frame, gray_frame, COLOR_BGR2GRAY);

    	//apply gaussian blur
    	GaussianBlur(gray_frame, gray_frame, Size(3, 3), 0);

    	//find edges
    	Laplacian(gray_frame, edge_frame, -1, 5);
    	convertScaleAbs(edge_frame, edge_frame);

    	//invert the image
    	edge_frame = 255 - edge_frame;

    	//apply thresholding
    	threshold(edge_frame, edge_frame, 150, 255, THRESH_BINARY);

    	//blur images heavily using edgePreservingFilter
    	edgePreservingFilter(desired_frame, edge_preserving_frame, 2, 50, 0.4);

    	// Create a output Matrix
    	cartoonized_image = Scalar::all(0);

    	// Combine the cartoon and edges
    	cv::bitwise_and(edge_preserving_frame, edge_preserving_frame, cartoonized_image, edge_frame);

	return cartoonized_image;
}
