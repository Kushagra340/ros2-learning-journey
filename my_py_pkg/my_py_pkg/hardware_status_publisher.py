#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from my_robot_interfaces.msg import HardwareStatus


class HardwarePublisherNode(Node): 
    def __init__(self):
        super().__init__("hardware_status_publisher") 
        self.hw_status_pub_ = self.create_publisher(HardwareStatus, "hardware_status", 10)
        self.timer_ = self.create_timer(1.0, self.publish_hw_status)
        self.get_logger().info("Hardware Status Publisher Node has been started.")


    def publish_hw_status(self):
        msg = HardwareStatus()
        msg.temperature = 25.0
        msg.are_motors_ready = True
        msg.debug_message = "All systems nominal"
        self.hw_status_pub_.publish(msg)
        self.get_logger().info("Published hardware status: %s" % msg.debug_message)


def main(args=None):
    rclpy.init(args=args)
    node = HardwarePublisherNode() 
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
