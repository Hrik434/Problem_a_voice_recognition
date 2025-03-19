#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

var= Twist()
energy = 100
busy= False

def hrik():

    rospy.init_node("control_node", anonymous=True)

    pub= rospy.Publisher("/cmd_vel", Twist, queue_size=10)

    rospy.loginfo("control node has started")

    def stop(event=None):
        global busy
        global var
        var.linear.x=0
        var.angular.z=0
        pub.publish(var)
        busy= False

    def callback(a):
        b= a.data.lower()
        rospy.loginfo(f"command received: {b}")
        global energy
        global var
        global busy

        if busy == True:
            rospy.loginfo("System is busy")
            return

        elif "kaboom" in b or "heal" in b:
            energy+=55
            rospy.loginfo(f"Energy : {energy}")
            return
        
        elif energy<5:
            rospy.loginfo("Not enough energy ")
            rospy.loginfo(f"Energy : {energy}")
            return

        elif "forward" in b and "5s" in b:
            busy = True
            energy-=5
            var.linear.x=1
            pub.publish(var)
            rospy.Timer(rospy.Duration(5), stop, oneshot=True)
            rospy.loginfo(f"Energy : {energy}")
            return
        
        elif "forward" in b:
            busy= True
            energy-=5
            var.linear.x=1
            pub.publish(var)
            rospy.Timer(rospy.Duration(2), stop, oneshot=True)
            rospy.loginfo(f"Energy : {energy}")
            return

        elif "backward" in b:
            busy=True
            energy-=5
            var.linear.x=-1
            pub.publish(var)
            rospy.Timer(rospy.Duration(2), stop, oneshot=True)
            rospy.loginfo(f"Energy : {energy}")
            return

        elif "right" in b:
            busy=True
            energy-=5
            var.angular.z=-1
            pub.publish(var)
            rospy.Timer(rospy.Duration(2), stop, oneshot=True)
            rospy.loginfo(f"Energy : {energy}")
            return

        elif "left" in b:
            busy= True
            energy-=5
            var.angular.z=1
            pub.publish(var)
            rospy.Timer(rospy.Duration(2), stop, oneshot=True)
            rospy.loginfo(f"Energy : {energy}")
            return

        


    rospy.Subscriber("/voice_commands", String, callback)

    rospy.spin()


if __name__=='__main__':
    try:
        hrik()
    except rospy.ROSInterruptException:
        pass
