import rospy
import cv2
import numpy as np
from sensor_msgs.msg import Image
from std_msgs.msg import String

from cv_bridge import CvBridge, CvBridgeError
import time


def callback(data):
  cap = cv2.VideoCapture(0)
  cap.set(cv2.CAP_PROP_FRAME_WIDTH, 224)
  cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 224)
  _,img = cap.read()
  img = bridge.cv2_to_imgmsg(img, "bgr8")
  originalPub.publish(img)
  cap.release

def wait_for_trigger():
  rospy.init_node('take_image', anonymous=True)
  rospy.Subscriber("/capture_image", String, callback)
  rospy.spin()

def edit(img):
    img = img[400:480,0:864]
    return img

def imagePublisher():
    bridge = CvBridge()

    _, camInput = cap.read()
    while not rospy.is_shutdown():
        _, img = cap.read()
	editedimage = img[400:480, 0:864]
        imgs = bridge.cv2_to_imgmsg(editedimage, "bgr8")
        img = bridge.cv2_to_imgmsg(img, "bgr8")

        originalPub.publish(img)
        editedPub.publish(imgs)

if __name__ == '__main__':
    bridge = CvBridge()
    originalPub = rospy.Publisher('/originalImage', Image, queue_size=1)
    wait_for_trigger()
