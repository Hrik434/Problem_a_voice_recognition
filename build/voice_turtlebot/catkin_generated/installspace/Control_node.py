#!/usr/bin/env python3

import rospy
from std_msgs.msg import String
from geometry_msgs.msg import Twist

class ControlNode:
    def __init__(self):
        rospy.init_node("control_node", anonymous=True)

        # Subscribe to voice commands
        rospy.Subscriber("/voice_commands", String, self.command_callback)

        # Publisher to control the robot
        self.cmd_vel_pub = rospy.Publisher("/cmd_vel", Twist, queue_size=10)

        # Robot movement settings
        self.twist = Twist()
        self.speed = 0.2
        self.turn_speed = 0.5
        self.energy = 100  # Initial energy

        rospy.loginfo("Control Node Started")
        rospy.spin()

    def command_callback(self, msg):
        command = msg.data.lower()
        rospy.loginfo(f"Received command: {command}")

        # Energy control
        if command in ["heal", "kaboom"]:
            self.energy += 20
            rospy.loginfo(f"Energy increased! Current energy: {self.energy}")
            return

        if self.energy <= 0:
            rospy.logwarn("Energy depleted! Cannot move.")
            return

        # Movement commands
        if "forward" in command:
            self.twist.linear.x = self.speed
            duration = self.get_duration(command)
        elif command == "left":
            self.twist.angular.z = self.turn_speed
            duration = 2
        elif command == "right":
            self.twist.angular.z = -self.turn_speed
            duration = 2
        elif command == "stop":
            self.twist.linear.x = 0
            self.twist.angular.z = 0
            duration = 0
        else:
            rospy.logwarn("Unknown command!")
            return

        # Publish movement command
        self.cmd_vel_pub.publish(self.twist)
        rospy.sleep(duration)

        # Stop the robot after moving
        self.twist.linear.x = 0
        self.twist.angular.z = 0
        self.cmd_vel_pub.publish(self.twist)

        # Reduce energy
        self.energy -= 10
        rospy.loginfo(f"Energy left: {self.energy}")

    def get_duration(self, command):
        words = command.split()
        for word in words:
            if word.isdigit():
                return int(word)
        return 2  # Default duration

if __name__ == "__main__":
    try:
        ControlNode()
    except rospy.ROSInterruptException:
        pass
