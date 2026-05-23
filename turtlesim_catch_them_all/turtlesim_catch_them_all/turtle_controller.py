#!/usr/bin/env python3
import math
import rclpy
from rclpy.node import Node
from functools import partial

from turtlesim.msg import Pose
from geometry_msgs.msg import Twist
from my_robot_interfaces.msg import TurtleArray
from my_robot_interfaces.srv import CatchTurtle

class TurtleControllerNode(Node):
    def __init__(self):
        super().__init__("turtle_controller")
        
        # Step 6: Declare the parameter from the PDF
        self.declare_parameter("catch_closest_turtle_first", True)
        
        self.pose_ = None
        self.turtle_to_catch_ = None

        self.pose_subscriber_ = self.create_subscription(
            Pose, "turtle1/pose", self.pose_callback, 10)
        
        self.cmd_vel_publisher_ = self.create_publisher(
            Twist, "turtle1/cmd_vel", 10)
            
        self.alive_turtles_subscriber_ = self.create_subscription(
            TurtleArray, "alive_turtles", self.alive_turtles_callback, 10)
        
        self.control_loop_timer_ = self.create_timer(0.01, self.control_loop)
        self.get_logger().info("Turtle Controller has been started.")

    def pose_callback(self, msg):
        self.pose_ = msg

    def alive_turtles_callback(self, msg):
        if len(msg.turtles) > 0:
            # Read the parameter to decide our strategy
            catch_closest = self.get_parameter("catch_closest_turtle_first").value
            
            if catch_closest and self.pose_ is not None:
                # Step 5: The Closest Turtle Algorithm
                closest_turtle = None
                closest_distance = float('inf')

                for turtle in msg.turtles:
                    dist_x = turtle.x - self.pose_.x
                    dist_y = turtle.y - self.pose_.y
                    distance = math.sqrt(dist_x**2 + dist_y**2)

                    if distance < closest_distance:
                        closest_distance = distance
                        closest_turtle = turtle

                self.turtle_to_catch_ = closest_turtle
            else:
                # Fallback to the old strategy
                self.turtle_to_catch_ = msg.turtles[0]
        else:
            self.turtle_to_catch_ = None

    def control_loop(self):
        if self.pose_ == None or self.turtle_to_catch_ == None:
            return

        dist_x = self.turtle_to_catch_.x - self.pose_.x
        dist_y = self.turtle_to_catch_.y - self.pose_.y
        distance = math.sqrt(dist_x * dist_x + dist_y * dist_y)

        msg = Twist()

        if distance > 0.5:
            msg.linear.x = 2.0 * distance
            goal_theta = math.atan2(dist_y, dist_x)
            diff = goal_theta - self.pose_.theta
            
            if diff > math.pi:
                diff -= 2 * math.pi
            elif diff < -math.pi:
                diff += 2 * math.pi
                
            msg.angular.z = 6.0 * diff
        else:
            msg.linear.x = 0.0
            msg.angular.z = 0.0
            
            self.call_catch_turtle_service(self.turtle_to_catch_.name)
            self.turtle_to_catch_ = None 

        self.cmd_vel_publisher_.publish(msg)

    def call_catch_turtle_service(self, turtle_name):
        client = self.create_client(CatchTurtle, "catch_turtle")
        while not client.wait_for_service(1.0):
            self.get_logger().warn("Waiting for the /catch_turtle service...")
            
        request = CatchTurtle.Request()
        request.name = turtle_name
        
        future = client.call_async(request)
        future.add_done_callback(
            partial(self.callback_call_catch_turtle, turtle_name=turtle_name))
            
    def callback_call_catch_turtle(self, future, turtle_name):
        try:
            response = future.result()
            if not response.success:
                self.get_logger().error(f"Turtle {turtle_name} could not be caught")
        except Exception as e:
            self.get_logger().error(f"Service call failed: {e}")

def main(args=None):
    rclpy.init(args=args)
    node = TurtleControllerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()