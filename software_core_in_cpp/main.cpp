#include "opencv2/opencv.hpp"
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

void exploits_function(int mode)
{
    cv::VideoCapture cap;
    cv::Mat frame;

    cap.open(0); // open the default camera
    if(!cap.isOpened()) {
        // check if we succeeded
        return ;
    }

    for(;;)
    {
        cap.read(frame);

        if(mode == 0)
        {
            cv::cvtColor(frame, frame, cv::COLOR_BGR2GRAY);
            cv::Canny(frame, frame, 50, 150, 3);
        }
        else if(mode == 1)
        {
            cv::cvtColor(frame, frame, cv::COLOR_BGR2GRAY);
        }
        else if(mode == 2)
        {
            cv::medianBlur(frame, frame, 65);
        }
        else if(mode == 3)
        {
            cv::cvtColor(frame, frame, cv::COLOR_BGR2GRAY);
            cv::HoughLinesP(frame, frame, 1, CV_PI/180, 70, 30, 10);
        }

        cv::imshow("Connected camera", frame);

        if(cv::waitKey(40) >= 0) {
            break;
        }
    }
}

int main()
{
	exploits_function(4);

	return 0;
}
