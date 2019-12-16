#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
#include <stdio.h>

#include "terminal_color_codes.h"

using namespace cv;
using namespace std;
using namespace terminal_color_codes;

void print_howto()
{
	cout << terminal_color_codes::Yellow + "Change mode \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Normal mode - press any keyboard key \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Draw mode - press 'p' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Painting mode - press 'c' \n" + terminal_color_codes::ResetAll;
}

void exploits_function()
{
    int pressed_key;
    int mode;

    print_howto();

    VideoCapture cap;
    Mat frame;

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

            Canny(frame, frame, 50, 150, 3);

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
