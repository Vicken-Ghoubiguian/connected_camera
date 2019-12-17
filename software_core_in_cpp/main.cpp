#include <opencv2/opencv.hpp>
#include <opencv2/core.hpp>
#include <opencv2/videoio.hpp>
#include <opencv2/highgui.hpp>

#include <iostream>
#include <stdio.h>

#include "src/terminal_color_codes.h"

using namespace cv;
using namespace std;
using namespace terminal_color_codes;

void print_howto()
{
	cout << "\n";
	cout << terminal_color_codes::Yellow + "Change mode: \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Normal mode - press any keyboard key \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Draw mode - press 'p' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Painting mode - press 'c' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Black and white mode - press 'g' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Edge detection mode - press 'y' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Hue saturation lightness mode - press 'h' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Gray and white mode - press 'w' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Negative or inverted mode - press 'i' \n" + terminal_color_codes::ResetAll;
	cout << "\n";
	cout << terminal_color_codes::Yellow + "Activate body parts detection: \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating face detection - press 'f' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating profile face detection - press 'd' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating eye detection - press 'e' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating tree eye glasses - press 't' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating smile detection - press 's' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating mouth detection - press 'm' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating nose detection - press 'n' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating right ear detection - press 'r' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Activating left ear detection - press 'l' \n" + terminal_color_codes::ResetAll;
	cout << "\n";
	cout << terminal_color_codes::Yellow + "Multimedia features: \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Shoot a photo regardless of the mode - press '1' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Start/Stop shooting video - press '2' \n" + terminal_color_codes::ResetAll;
	cout << "\n";
	cout << terminal_color_codes::Yellow + "To leave or to quit: \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* To leave or to quit the connected camera - press 'Esc' \n" + terminal_color_codes::ResetAll;
	cout << "\n";
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

            Canny(frame, frame, 50, 150);

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
