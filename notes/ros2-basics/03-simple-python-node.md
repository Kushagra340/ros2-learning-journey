# Basics 03: The Simple Python Node

## 1. The Python Script (`node1.py`)
This is the absolute bare minimum code required to spin up a ROS 2 node using Python.

```python
#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

def main(args=None):
    # 1. Initialize ROS 2 communications
    rclpy.init(args=args)
    
    # 2. Create the node and give it a name across the ROS 2 network
    node = Node("node1")
    
    # 3. Print a log message to the terminal
    node.get_logger().info("Hello World!!")
    
    # 4. Keep the node alive and spinning (listening for callbacks)
    rclpy.spin(node)
    
    # 5. Cleanly destroy the node when Ctrl+C is pressed
    rclpy.shutdown()

if __name__ == "__main__":
    main()
```

### How it works:
* `#!/usr/bin/env python3`: The shebang line. It tells Ubuntu to execute this file using the Python 3 interpreter.
* `rclpy.init()`: Boots up the ROS 2 middleware so this script can talk to the rest of the computer.
* `rclpy.spin(node)`: This is an infinite loop. It literally pauses the code right here and keeps the node alive until you forcefully kill it. Without this line, the script would just print "Hello World!!" and instantly exit.

---

## 2. The Bridge (`setup.py`)
Writing the Python script isn't enough. You have to tell ROS 2 that this script exists and is allowed to be run as an executable. We do this by modifying the `entry_points` dictionary inside `setup.py`.

```python
    entry_points={
        'console_scripts': [
            "node1 = my_py_pkg.node1:main"
        ],
    },
```

### The Syntax Breakdown:
* `"node1 ..."`: The name of the executable you will type in the terminal.
* `... = my_py_pkg`: The name of the package the script lives in.
* `... .node1`: The name of the Python file (without the `.py`).
* `... :main"`: The exact function inside that Python file to run when the node starts.

---

## 3. The Execution Pipeline
Every time you create a new node or edit `setup.py`, you must rebuild the workspace before ROS 2 can see it.

1. **Build the workspace:**
   ```bash
   cd ~/ros2_ws
   colcon build --packages-select my_py_pkg
   ```
   *(Note: `--packages-select` is a pro-move that tells colcon to only build this specific package instead of wasting time building the C++ package too).*

2. **Source the environment:**
   ```bash
   source ~/.bashrc
   ```

3. **Run the node:**
   ```bash
   ros2 run my_py_pkg node1
   ```