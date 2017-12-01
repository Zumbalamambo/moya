#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def talker():
    pub = rospy.Publisher('direction', String, queue_size=10)
    rospy.init_node('direction_publisher', anonymous=True)
    rate=rospy.Rate(10)
    while not rospy.is_shutdown():
        direction_string = "left %s" % rospy.get_time()
        rospy.loginfo(direction_string)
        pub.publish(direction_string)
        rate.sleep()

if __name__=='main':
    try: 
        talker()
    except rospy.ROSInterruptException:
        pass