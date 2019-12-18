#ifndef FRAME_MODE_LIBRARY
#define FRAME_MODE_LIBRARY

#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

using namespace cv;

Mat negative_or_inverted_effect_function(Mat desired_frame);
Mat edge_detection_mode_function(Mat desired_frame);

#endif
