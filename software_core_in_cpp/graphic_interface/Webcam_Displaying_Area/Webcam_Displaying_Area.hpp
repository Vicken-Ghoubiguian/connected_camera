#ifndef WEBCAM_DISPLAYING_AREA
#define	WEBCAM_DISPLAYING_AREA

#include <gtkmm/drawingarea.h>
#include <cairomm/context.h>
#include <opencv2/opencv.hpp>

using namespace Gtk;
using namespace cv;

class Webcam_Displaying_Area : public DrawingArea
{
	protected:
        	VideoCapture cv_cap;
        	bool cv_opened;
		virtual bool on_draw(const Cairo::RefPtr<Cairo::Context> &cr);
        	bool on_timeout ();

	public:
		Webcam_Displaying_Area();
		virtual ~Webcam_Displaying_Area();
};

#endif
