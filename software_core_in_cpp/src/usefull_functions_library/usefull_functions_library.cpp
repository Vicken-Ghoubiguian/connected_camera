#include "usefull_functions_library.hpp"
#include "../terminal_color_codes.hpp"

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace terminal_color_codes;

void usefull_functions::print_howto_in_konsole()
{
        cout << "\n";
        cout << terminal_color_codes::Yellow + "Change mode: \n" + terminal_color_codes::ResetAll;
        cout << terminal_color_codes::Yellow + "* Normal mode - press any keyboard key \n" + terminal_color_codes::ResetAll;
        cout << terminal_color_codes::Yellow + "* Draw mode - press 'p' \n" + terminal_color_codes::ResetAll;
        cout << terminal_color_codes::Yellow + "* Painting mode - press 'c' \n" + terminal_color_codes::ResetAll;
        cout << terminal_color_codes::Yellow + "* Black and white mode with gray application mode - press 'g' \n" + terminal_color_codes::ResetAll;
	cout << terminal_color_codes::Yellow + "* Black and white mode with RGB application mode - press 'a' \n" + terminal_color_codes::ResetAll;
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
