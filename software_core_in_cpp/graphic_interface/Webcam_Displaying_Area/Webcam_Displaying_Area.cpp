#include "Webcam_Displaying_Area.hpp"

#include <gdkmm/pixbuf.h>
#include <gdkmm/general.h>
#include <glibmm/main.h>

Webcam_Displaying_Area::Webcam_Displaying_Area() : cv_opened(false)
{
	cv_cap.open(0);

	if (cv_cap.isOpened() == true)
	{
		cv_opened = true;
		Glib::signal_timeout().connect(sigc::mem_fun(*this, &Webcam_Displaying_Area::on_timeout), 50);
	}
}

Webcam_Displaying_Area::~Webcam_Displaying_Area()
{

}

bool Webcam_Displaying_Area::on_timeout()
{
	Glib::RefPtr<Gdk::Window> win = get_window();
	if(win)
	{
		Gdk::Rectangle r(0, 0, get_allocation().get_width(), get_allocation().get_height());
		win->invalidate_rect(r, false);
	}

	return true;
}

bool Webcam_Displaying_Area::on_draw(const Cairo::RefPtr<Cairo::Context> &cr)
{
	if(!cv_opened)
	{
		return false;
	}

	Mat cv_frame, cv_frame1;

	cv_cap.read(cv_frame);

	if(cv_frame.empty())
	{
		return false;
	}

	cvtColor (cv_frame, cv_frame1, CV_BGR2RGB);

	Gdk::Cairo::set_source_pixbuf (cr, Gdk::Pixbuf::create_from_data(cv_frame1.data, Gdk::COLORSPACE_RGB, false, 8, cv_frame1.cols, cv_frame1.rows, cv_frame1.step));

	cr->paint();

	return true;
}
