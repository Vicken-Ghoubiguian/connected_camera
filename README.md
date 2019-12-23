This is a connected camera project.

This connected camera has the following features:

* can take photos,

* can shoot videos,

* can add decorations to take the photo or shoot the video,

* can modify mode among the following: normal, cartoonized without colors, cartoonized with colors,

* can share videos or photos on different social networks (Facebook, Twitter, LinkedIn, YouTube and Instagram).

This camera can take photos in this format: `'.jpg'`, `'.jpeg'`, `'.jpe'`, `'.jp2'`, `'.png'`, `'.tiff'`, `'.tif'`, `'.bmp'`, `'.dib'`, `'.pbm'`, `'.pgm'`, `'.ppm'`.

This camera can record videos in this format: `'.avi'`, `'.mp4'`.

To use the cpp software core in the current project or to test it, follow this commands:

1. `cd connected_camera/software_core_in_cpp`

1. `g++ -o main main.cpp src/*/* graphic_interface/*/* `pkg-config --cflags --libs gtkmm-3.0 opencv``

To learn more about gtkmm (official C++ interface for the popular GUI library GTK+): https://www.lucidarme.me/gtkmm-exemple-de-tutoriel/
