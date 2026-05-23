#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
import random
import math

from turtlesim.srv import Spawn
from turtlesim.srv import Kill
from my_robot_interfaces.msg import Turtle, TurtleArray
from my_robot_interfaces.srv import CatchTurtle

class TurtleSpawnerNode(Node):
    def __init__(self):
        super().__init__("turtle_spawner")
        
        # Step 6: Declare parameters
        self.declare_parameter("spawn_frequency", 1.0)
        self.declare_parameter("turtle_name_prefix", "turtle")
        
        self.spawn_frequency_ = self.get_parameter("spawn_frequency").value
        self.turtle_name_prefix_ = self.get_parameter("turtle_name_prefix").value
        
        self.turtle_counter_ = 2 
        self.alive_turtles_ = [] 
        
        self.alive_turtles_publisher_ = self.create_publisher(
            TurtleArray, "alive_turtles", 10)

        # Timer uses the frequency parameter (e.g., 2.0 hz = 0.5 seconds)
        self.spawn_timer_ = self.create_timer(1.0 / self.spawn_frequency_, self.spawn_new_turtle)
        
        self.catch_turtle_service_ = self.create_service(
            CatchTurtle, "catch_turtle", self.callback_catch_turtle)

        self.get_logger().info("Turtle Spawner has been started.")

    def callback_catch_turtle(self, request, response):
        self.call_kill_service(request.name)
        
        for i, turtle in enumerate(self.alive_turtles_):
            if turtle.name == request.name:
                del self.alive_turtles_[i]
                break
                
        self.publish_alive_turtles()
        response.success = True
        return response

    def call_kill_service(self, turtle_name):
        client = self.create_client(Kill, "kill")
        while not client.wait_for_service(1.0):
            pass
        request = Kill.Request()
        request.name = turtle_name
        client.call_async(request) 

    def spawn_new_turtle(self):
        x = random.uniform(0.0, 11.0)
        y = random.uniform(0.0, 11.0)
        theta = random.uniform(0.0, 2 * math.pi)
        self.call_spawn_service(x, y, theta)

    def call_spawn_service(self, x, y, theta):
        client = self.create_client(Spawn, "spawn")
        while not client.wait_for_service(1.0):
            pass
            
        request = Spawn.Request()
        request.x = x
        request.y = y
        request.theta = theta
        
        # Use the custom prefix
        turtle_name = self.turtle_name_prefix_ + str(self.turtle_counter_)
        request.name = turtle_name
        self.turtle_counter_ += 1
        
        future = client.call_async(request)
        future.add_done_callback(
            lambda future_msg: self.spawn_callback(future_msg, turtle_name, x, y, theta)
        )
        
    def spawn_callback(self, future, turtle_name, x, y, theta):
        try:
            response = future.result()
            if response.name != "":
                new_turtle = Turtle()
                new_turtle.name = response.name
                new_turtle.x = x
                new_turtle.y = y
                new_turtle.theta = theta
                
                self.alive_turtles_.append(new_turtle)
                self.publish_alive_turtles()
        except Exception as e:
            pass

    def publish_alive_turtles(self):
        msg = TurtleArray()
        msg.turtles = self.alive_turtles_
        self.alive_turtles_publisher_.publish(msg)

def main(args=None):
    rclpy.init(args=args)
    node = TurtleSpawnerNode()
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()