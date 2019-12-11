-- Creation of the supported_image_formats_table table --
CREATE TABLE IF NOT EXISTS supported_image_formats_table(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	image_format_extension VARCHAR(10) NOT NULL
);

-- Insertion of image formats --
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".jpg");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".jpeg");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".jpe");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".jp2");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".png");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".tiff");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".tif");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".bmp");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".dib");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".pbm");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".pgm");
INSERT INTO supported_image_formats_table(image_format_extension) VALUES(".ppm");

-- Creation of the supported_image_formats_table table --
CREATE TABLE IF NOT EXISTS supported_video_formats_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        video_format_extension VARCHAR(10) NOT NULL,
	associated_fourcc VARCHAR(10) NOT NULL
);

-- Insertion of video formats --
INSERT INTO supported_video_formats_table(video_format_extension, associated_fourcc) VALUES(".avi", "XVID");
INSERT INTO supported_video_formats_table(video_format_extension, associated_fourcc) VALUES(".mp4", "MP4V");

-- Creation of the sound_effect_files_to_shot_photos_table table --
CREATE TABLE IF NOT EXISTS sound_effect_files_to_shot_photos_table(
	id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
	file_path VARCHAR(100) NOT NULL,
	file_name VARCHAR(100) NOT NULL
);

-- Insertion of sound effect files to shot photos --
INSERT INTO supported_image_formats_table(file_path, file_name) VALUES("sounds/4_seconds_long_paparazzi_camera_sound.mp3", "Paparazzi camera sound");
INSERT INTO supported_image_formats_table(file_path, file_name) VALUES("sounds/1_second_long_old_camera_sound.mp3", "Old camera sound");

-- Creation of the sound_effect_files_to_record_videos_table table --
CREATE TABLE IF NOT EXISTS sound_effect_files_to_record_videos_table(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        file_path VARCHAR(100) NOT NULL,
        file_name VARCHAR(100) NOT NULL
);

-- Insertion of sound effect files to shot photos --
INSERT INTO supported_image_formats_table(file_path, file_name) VALUES("sounds/16_seconds_old_video_projector_sound.mp3", "Old video projector sound");
