This is a connected camera project.

This connected camera has the following features:

1. can take photos,

1. can shoot videos,

1. can add decorations to take the photo or shoot the video,

1. can modify mode among the following: normal, cartoonized without colors, cartoonized with colors,

1. can share videos or photos on different social networks (Facebook, Twitter, LinkedIn, YouTube and Instagram).

This camera can take photos in this format: `'.jpg'`, `'.jpeg'`, `'.jpe'`, `'.jp2'`, `'.png'`, `'.tiff'`, `'.tif'`, `'.bmp'`, `'.dib'`, `'.pbm'`, `'.pgm'`, `'.ppm'`.

This camera can record videos in this format: `'.avi'`, `'.mp4'`.

To use the cpp software core in the current project or to test it, follow this commands:

1. `cd connected_camera/software_core_in_cpp`

1. `g++ -I /usr/local/include -L/usr/local/lib/ main.cpp src/'(asterisk)'/'(asterisk)' -o main -lopencv_core -lopencv_highgui -lopencv_imgproc -lopencv_imgcodecs -lopencv_videoio -lopencv_calib3d -lopencv_photo`
