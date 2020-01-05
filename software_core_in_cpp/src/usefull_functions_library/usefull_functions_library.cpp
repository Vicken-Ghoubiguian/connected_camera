#include "usefull_functions_library.hpp"
#include "../terminal_color_codes.hpp"

#include <iostream>
#include <stdio.h>

using namespace std;
using namespace terminal_color_codes;

std::map<std::string, std::string> usefull_functions::color_codes_map_initialisation_function()
{
	std::map<std::string, std::string> current_color_codes_map;

	current_color_codes_map["ResetAll"] = terminal_color_codes::ResetAll;

	current_color_codes_map["Bold"] = terminal_color_codes::Bold;
	current_color_codes_map["Dim"] = terminal_color_codes::Dim;
	current_color_codes_map["Underlined"] = terminal_color_codes::Underlined;
	current_color_codes_map["Blink"] = terminal_color_codes::Blink;
	current_color_codes_map["Reverse"] = terminal_color_codes::Reverse;
	current_color_codes_map["Hidden"] = terminal_color_codes::Hidden;

	current_color_codes_map["ResetBold"] = terminal_color_codes::ResetBold;
	current_color_codes_map["ResetDim"] = terminal_color_codes::ResetDim;
	current_color_codes_map["ResetUnderlined"] = terminal_color_codes::ResetUnderlined;
	current_color_codes_map["ResetBlink"] = terminal_color_codes::ResetBlink;
	current_color_codes_map["ResetReverse"] = terminal_color_codes::ResetReverse;
	current_color_codes_map["ResetHidden"] = terminal_color_codes::ResetHidden;

	current_color_codes_map["Default"] = terminal_color_codes::Default;
	current_color_codes_map["Black"] = terminal_color_codes::Black;
	current_color_codes_map["Red"] = terminal_color_codes::Red;
	current_color_codes_map["Green"] = terminal_color_codes::Green;
	current_color_codes_map["Yellow"] = terminal_color_codes::Yellow;
	current_color_codes_map["Blue"] = terminal_color_codes::Blue;
	current_color_codes_map["Magenta"] = terminal_color_codes::Magenta;
	current_color_codes_map["Cyan"] = terminal_color_codes::Cyan;
	current_color_codes_map["LightGray"] = terminal_color_codes::LightGray;
	current_color_codes_map["DarkGray"] = terminal_color_codes::DarkGray;
	current_color_codes_map["LightRed"] = terminal_color_codes::LightRed;
	current_color_codes_map["LightGreen"] = terminal_color_codes::LightGreen;
	current_color_codes_map["LightYellow"] = terminal_color_codes::LightYellow;
	current_color_codes_map["LightBlue"] = terminal_color_codes::LightBlue;
	current_color_codes_map["LightMagenta"] = terminal_color_codes::LightMagenta;
	current_color_codes_map["LightCyan"] = terminal_color_codes::LightCyan;
	current_color_codes_map["White"] = terminal_color_codes::White;

	current_color_codes_map["BackgroundDefault"] = terminal_color_codes::BackgroundDefault;
	current_color_codes_map["BackgroundBlack"] = terminal_color_codes::BackgroundBlack;
	current_color_codes_map["BackgroundRed"] = terminal_color_codes::BackgroundRed;
	current_color_codes_map["BackgroundGreen"] = terminal_color_codes::BackgroundGreen;
	current_color_codes_map["BackgroundYellow"] = terminal_color_codes::BackgroundYellow;
	current_color_codes_map["BackgroundBlue"] = terminal_color_codes::BackgroundBlue;
	current_color_codes_map["BackgroundMagenta"] = terminal_color_codes::BackgroundMagenta;
	current_color_codes_map["BackgroundCyan"] = terminal_color_codes::BackgroundCyan;
	current_color_codes_map["BackgroundLightGray"] = terminal_color_codes::BackgroundLightGray;
	current_color_codes_map["BackgroundDarkGray"] = terminal_color_codes::BackgroundDarkGray;
	current_color_codes_map["BackgroundLightRed"] = terminal_color_codes::BackgroundLightRed;
	current_color_codes_map["BackgroundLightGreen"] = terminal_color_codes::BackgroundLightGreen;
	current_color_codes_map["BackgroundLightYellow"] = terminal_color_codes::BackgroundLightYellow;
	current_color_codes_map["BackgroundLightBlue"] = terminal_color_codes::BackgroundLightBlue;
	current_color_codes_map["BackgroundLightMagenta"] = terminal_color_codes::BackgroundLightMagenta;
	current_color_codes_map["BackgroundLightCyan"] = terminal_color_codes::BackgroundLightCyan;
	current_color_codes_map["BackgroundWhite"] = terminal_color_codes::BackgroundWhite;

	return current_color_codes_map;
}

std::string usefull_functions::print_howto_in_window()
{
	std::string print_howto_string;

	print_howto_string = "\n";
	print_howto_string = print_howto_string + "Change mode: \n";
	print_howto_string = print_howto_string + "* Normal mode - press any keyboard key \n";
	print_howto_string = print_howto_string + "* Draw mode - press 'p' \n";
	print_howto_string = print_howto_string + "* Painting mode - press 'c' \n";
	print_howto_string = print_howto_string + "* Black and white mode with gray application mode - press 'g' \n";
	print_howto_string = print_howto_string + "* Black and white mode with RGB application mode - press 'a' \n";
	print_howto_string = print_howto_string + "* Edge detection mode - press 'y' \n";
	print_howto_string = print_howto_string + "* Hue saturation lightness mode - press 'h' \n";
	print_howto_string = print_howto_string + "* Gray and white mode - press 'w' \n";
	print_howto_string = print_howto_string + "* Negative or inverted mode - press 'i' \n";
	print_howto_string = print_howto_string + "\n";
	print_howto_string = print_howto_string + "Activate body parts detection: \n";
	print_howto_string = print_howto_string + "* Activating face detection - press 'f' \n";
	print_howto_string = print_howto_string + "* Activating profile face detection - press 'd' \n";
	print_howto_string = print_howto_string + "* Activating eye detection - press 'e' \n";
	print_howto_string = print_howto_string + "* Activating tree eye glasses - press 't' \n";
	print_howto_string = print_howto_string + "* Activating smile detection - press 's' \n";
	print_howto_string = print_howto_string + "* Activating mouth detection - press 'm' \n";
	print_howto_string = print_howto_string + "* Activating nose detection - press 'n' \n";
	print_howto_string = print_howto_string + "* Activating right ear detection - press 'r' \n";
	print_howto_string = print_howto_string + "* Activating left ear detection - press 'l' \n";
	print_howto_string = print_howto_string + "\n";
	print_howto_string = print_howto_string + "Multimedia features: \n";
	print_howto_string = print_howto_string + "* Shoot a photo regardless of the mode - press '1' \n";
	print_howto_string = print_howto_string + "* Start/Stop shooting video - press '2' \n";
	print_howto_string = print_howto_string + "\n";
	print_howto_string = print_howto_string + "To leave or to quit: \n";
	print_howto_string = print_howto_string + "* To leave or to quit the connected camera - press 'Esc' \n";
	print_howto_string = print_howto_string + "\n";

	return print_howto_string;
}

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

void usefull_functions::writting_in_console_function(std::string desired_terminal_color_code, std::string desired_log_to_write)
{
	cout << desired_terminal_color_code + desired_log_to_write + terminal_color_codes::ResetAll << std::endl;
}
