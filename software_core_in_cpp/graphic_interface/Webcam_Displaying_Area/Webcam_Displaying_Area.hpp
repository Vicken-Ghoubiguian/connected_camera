#ifndef WEBCAM_DISPLAYING_AREA
#define	WEBCAM_DISPLAYING_AREA

#include <gtkmm/drawingarea.h>
#include <cairomm/context.h>
#include <opencv2/opencv.hpp>

#include "../../src/connected_camera_mode.hpp"
#include "../../src/frame_mode_library/frame_mode_library.hpp"

using namespace Gtk;
using namespace cv;
using namespace frame_mode;

class Webcam_Displaying_Area : public DrawingArea
{
	protected:
        	VideoCapture cv_cap;
        	bool cv_opened;
		connected_camera_mode current_mode;
		virtual bool on_draw(const Cairo::RefPtr<Cairo::Context> &cr);
        	bool on_timeout ();

	public:
		Webcam_Displaying_Area();
		virtual ~Webcam_Displaying_Area();
		connected_camera_mode getCurrent_mode();
		void setCurrent_mode(connected_camera_mode new_current_mode);
};

#endif
