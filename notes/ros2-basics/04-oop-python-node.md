# Basics 04: The OOP Python Node

## 1. The Python Script (`node1.py`)
This is the standard Object-Oriented template used for almost all professional ROS 2 Python nodes.

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

class Node1(Node):
    def __init__(self):
        # Initialize the Node class with the node name
        super().__init__("node1")
        
        # Internal state variable (memory)
        self.counter_ = 0
        
        self.get_logger().info("Hello World!!")
        
        # Create a timer that triggers the callback every 1.0 seconds
        self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        # Log the current count and increment it
        self.get_logger().info("Hello " + str(self.counter_))
        self.counter_ += 1

def main(args=None):
    rclpy.init(args=args)
    
    # Instantiate the custom OOP node
    node = Node1()
    
    # Keep the node alive and listening for timer callbacks
    rclpy.spin(node)
    
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

### Key Differences from the Minimal Node:
1. **The Class Structure (`class Node1(Node):`):** We inherit from the core ROS 2 `Node` module. This gives our custom class all the superpowers of a standard ROS 2 node (like logging, timers, and publishers) built right in.
2. **`super().__init__("node1")`:** This calls the constructor of the parent `Node` class and registers the name of our node (`node1`) with the ROS 2 network.
3. **`self.create_timer()`:** Standard Python `while` loops are dangerous in ROS 2 because they block the execution thread, meaning the node can't listen to other sensors while it's looping. `create_timer` runs asynchronously, executing the callback function exactly when it needs to without freezing the system.

## 2. The Bridge (`setup.py`)
Since you just modified the existing `node1.py` file, the `setup.py` entry point remains exactly the same!

```python
    entry_points={
        'console_scripts': [
            "node1 = my_py_pkg.node1:main"
        ],
    },
```