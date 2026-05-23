#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class AddTwoIntsClient(Node):
    def __init__(self):
        super().__init__("add_two_ints_client")
        self.client_ = self.create_client(AddTwoInts, "add_two_ints")

    # FIXED: Indented correctly and renamed to match what main() is calling!
    def call_add_two_ints(self, a, b):
        while not self.client_.wait_for_service(timeout_sec=1.0):
            self.get_logger().warn("Waiting for the add_two_ints service to be available...")
        
        request = AddTwoInts.Request()
        request.a = a
        request.b = b

        future = self.client_.call_async(request)
        future.add_done_callback(self.callback_add_two_ints)
            
    # FIXED: Indented correctly!
    def callback_add_two_ints(self, future):
        response = future.result()
        self.get_logger().info(f"Result: {response.sum}")

def main(args=None):
    rclpy.init(args=args)
    node = AddTwoIntsClient()
    node.call_add_two_ints(5, 10)
    node.call_add_two_ints(15, 20)
    node.call_add_two_ints(25, 30)
    rclpy.spin(node)
    rclpy.shutdown()

if __name__ == "__main__":
    main()