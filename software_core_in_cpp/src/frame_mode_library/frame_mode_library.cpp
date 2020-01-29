#include "frame_mode_library.hpp"

Mat frame_mode::improved_detail_effect_function(Mat desired_frame, float s_sigma, float r_sigma)
{
	Mat result_frame;

	detailEnhance(desired_frame, result_frame, s_sigma, r_sigma);

	return result_frame;
}

Mat frame_mode::stylization_effect_application_function(Mat desired_frame, float sigma_s, float sigma_r)
{
	Mat result_frame;

	stylization(desired_frame, result_frame, sigma_s, sigma_r);

	return result_frame;
}

Mat frame_mode::pencil_effect_application_function(Mat desired_frame, bool output_indicator, float sigma_s, float sigma_r, float shade_factor)
{
	Mat result_frame, result_frame_bis;

	if(output_indicator == true)
	{
		pencilSketch(desired_frame, result_frame, result_frame_bis, sigma_s, sigma_r, shade_factor);
	}
	else
	{
		pencilSketch(desired_frame, result_frame_bis, result_frame, sigma_s, sigma_r, shade_factor);
	}

	return result_frame;
}

Mat frame_mode::colormap_effect_application_function(Mat desired_frame, enum ColormapTypes chosen_colormap)
{
	Mat result_frame, grayed_frame;

	cvtColor(desired_frame, grayed_frame, COLOR_BGR2GRAY);

	applyColorMap(grayed_frame, result_frame, chosen_colormap);

	return result_frame;
}

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

	cvtColor(desired_frame, result_frame, COLOR_BGR2GRAY);

	return result_frame;
}

Mat frame_mode::black_and_white_frame_converting_function(Mat desired_frame, enum ColorConversionCodes color_conversion_code)
{
	Mat result_frame;

	cvtColor(desired_frame, desired_frame, color_conversion_code);

	threshold(desired_frame, result_frame, 150, 255, THRESH_BINARY);

	return result_frame;
}

Mat frame_mode::cartoonizing_image_function(Mat desired_frame, int ksize, bool sketch_mode)
{
	Mat gray_frame, edge_frame, edge_preserving_frame, cartoonized_image;

	//Convert to gray scale
    	cvtColor(desired_frame, gray_frame, COLOR_BGR2GRAY);

    	//apply gaussian blur
    	GaussianBlur(gray_frame, gray_frame, Size(3, 3), 0);

    	//find edges
    	Laplacian(gray_frame, edge_frame, -1, ksize);
    	convertScaleAbs(edge_frame, edge_frame);

    	//invert the image
    	edge_frame = 255 - edge_frame;

    	//apply thresholding
    	threshold(edge_frame, edge_frame, 150, 255, THRESH_BINARY);

	//
	if(sketch_mode == true)
	{

		//
		cvtColor(edge_frame, edge_frame, COLOR_GRAY2BGR);

		//
		return edge_frame;
	}

    	//blur images heavily using edgePreservingFilter
    	edgePreservingFilter(desired_frame, edge_preserving_frame, 2, 50, 0.4);

    	// Create a output Matrix
    	cartoonized_image = Scalar::all(0);

    	// Combine the cartoon and edges
    	cv::bitwise_and(edge_preserving_frame, edge_preserving_frame, cartoonized_image, edge_frame);

	return cartoonized_image;
}
