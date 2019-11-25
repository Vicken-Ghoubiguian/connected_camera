import cv2

def shoot_a_photo_function(title, desired_frame):

        cv2.imwrite(title + '.jpg', desired_frame, [cv2.IMWRITE_JPEG_QUALITY, 90])
