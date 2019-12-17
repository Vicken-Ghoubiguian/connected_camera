#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

#include "src/usefull_functions_library/usefull_functions_library.h"

using namespace cv;
using namespace std;

void exploits_function()
{
    int pressed_key;
    int mode;

    print_howto();

    VideoCapture cap;
    Mat frame, edge_detection_mode_frame;

    //Open the default camera
    cap.open(0);

    if(!cap.isOpened()) {

	//
        return ;
    }

    //We're entering an infinite loop...
    for(;;)
    {
        cap.read(frame);

	//
	pressed_key = waitKey(1);

	//If 'ESC' is pressed...
        if(pressed_key == 27) {

            break;

        }

	//If any alphabetic key (lower or upper case) is pressed...
	if((pressed_key >= 65 && pressed_key <= 90) || (pressed_key >= 97 && pressed_key <= 122))
	{

	    mode = pressed_key;

	}

	//If 'y' is pressed...
        if(mode == 121)
        {

            Canny(frame, edge_detection_mode_frame, 50, 150);

	    frame = edge_detection_mode_frame;

        }
	//If 'w' is pressed...
        else if(mode == 119)
        {

            cvtColor(frame, frame, COLOR_BGR2GRAY);

        }
	//If 'i' is pressed...
        else if(mode == 105)
        {

            bitwise_not(frame, frame);

        }
	//If 'h' is pressed...
	else if(mode == 104)
	{

		cvtColor(frame, frame, COLOR_BGR2HSV);

	}
	//If 'o' is pressed...
	else if(mode == 111)
	{
		frame = frame;
	}

	//Displaying the frame in a window...
        imshow("Connected camera", frame);
    }
}

int main()
{
	exploits_function();

	return 0;
}
