#ifndef FRAME_MODE_LIBRARY
#define FRAME_MODE_LIBRARY

#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/photo.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/photo.hpp>

using namespace cv;

namespace frame_mode
{
	Mat negative_or_inverted_effect_function(Mat desired_frame);
	Mat edge_detection_mode_function(Mat desired_frame);
	Mat hue_saturation_lightness_effect_function(Mat desired_frame);
	Mat gray_and_white_effect_function(Mat desired_frame);
	Mat cartoonizing_image_function(Mat desired_frame, int ksize, bool sketch_mode);
	Mat black_and_white_frame_converting_function(Mat desired_frame, enum ColorConversionCodes color_conversion_code);
	Mat colormap_effect_application_function(Mat desired_frame, enum ColormapTypes chosen_colormap);
	Mat pencil_effect_application_function(Mat desired_frame, bool output_indicator, float sigma_s, float sigma_r, float shade_factor);
	Mat stylization_effect_application_function(Mat desired_frame, float sigma_s, float sigma_r);
}

#endif
