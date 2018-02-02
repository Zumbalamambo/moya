import rospy
# ROS Image message
from sensor_msgs.msg import Image
from std_msgs.msg import Int8
# ROS Image message -> OpenCV2 image converter
from cv_bridge import CvBridge, CvBridgeError
# OpenCV2 for saving an image
import numpy as np
import cv2
import time


bridge = CvBridge()
def image_callback(msg):

    img = bridge.imgmsg_to_cv2(msg, "bgr8")
    cv2.imshow('hi', img)
    k = cv2.waitKey(5)



def main():
    rospy.init_node('viewcam')
    rospy.Subscriber('originalImage', Image, image_callback, queue_size = 1, buff_size = 2**24)
    rospy.spin()

if __name__ == '__main__':
    main()
