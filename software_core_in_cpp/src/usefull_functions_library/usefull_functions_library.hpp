#ifndef USEFULL_FUNCTIONS_LIBRARY
#define USEFULL_FUNCTIONS_LIBRARY

#include <string>
#include <map>
#include <ctime>

namespace usefull_functions
{
	void print_howto_in_konsole();
	std::string print_howto_in_window();
	void writting_in_console_function(std::string desired_terminal_color_code, std::string desired_log_to_write);
	std::map<std::string, std::string> color_codes_map_initialisation_function();
	std::string today_as_string_returning_function();
}

#endif
