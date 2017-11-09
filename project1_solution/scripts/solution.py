#!/usr/bin/env python  
import rospy
import sys
from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

class solution:
    def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        self.sum_pub = rospy.Publisher("/sum", Int16, queue_size=10)

        self.two_ints_sub = rospy.Subscriber("/two_ints", TwoInts, self.callback,  queue_size = 1)


    def callback(self, ros_data):
        '''Callback function of subscribed topic.'''
        
        # Publish the sum
        self.sum_pub.publish(ros_data.a + ros_data.b)

def main(args):
    '''Initializes and cleanup ros node'''
    ic = solution()
    rospy.init_node('sum_node', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS Image feature detector module"

if __name__ == '__main__':
    main(sys.argv)
