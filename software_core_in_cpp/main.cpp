#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
#include <stdio.h>

#include "terminal_color_codes.h"

using namespace cv;
using namespace std;

void exploits_function()
{
    VideoCapture cap;
    Mat frame;

    int pressed_key;
    int mode;

    //Open the default camera
    cap.open(0);

    if(!cap.isOpened()) {

	//
        return ;
    }

    //
    for(;;)
    {
        cap.read(frame);

	//
	pressed_key = waitKey(1);

        if(pressed_key == 27) {

            break;

        }
        else if(pressed_key == 32) {

            cout << "Pressed...\n";

        }
	else if((pressed_key >= 65 && pressed_key <= 90) || (pressed_key >= 97 && pressed_key <= 122)) {

	    mode = pressed_key;

	}

	//
        if(mode == 121)
        {

            cvtColor(frame, frame, COLOR_BGR2GRAY);
            Canny(frame, frame, 50, 150, 3);

        }
        else if(mode == 119)
        {

            cvtColor(frame, frame, COLOR_BGR2GRAY);

        }
        else if(mode == 65)
        {

            medianBlur(frame, frame, 65);

        }
	else if(mode == 111)
	{
		frame = frame;
	}

        imshow("Connected camera", frame);
    }
}

int main()
{
	exploits_function();

	return 0;
}
