import cv2

def shoot_a_photo_function(title, desired_frame, desired_format = '.jpg'):

        cv2.imwrite(title + desired_format, desired_frame)
