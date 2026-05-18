# Basics 01: Creating a Python Package

## 1. The Creation Command
To create a new ROS 2 Python package, you must be inside the `src` folder of your workspace.

```bash
cd ~/ros2_ws/src
ros2 pkg create my_py_pkg --build-type ament_python --dependencies rclpy
```

### The Command Breakdown:
* `ros2 pkg create`: The core ROS 2 command to generate the package template.
* `my_py_pkg`: The name of your package (always use lowercase and underscores).
* `--build-type ament_python`: CRITICAL. This tells the `colcon` build system to treat this as a Python project instead of C++.
* `--dependencies rclpy`: Automatically injects the ROS 2 Python client library (`rclpy`) into your package dependencies so you don't have to add it manually later.

---

## 2. The Core Files Generated
When you run that command, ROS 2 generates a specific folder structure. The three most important files/folders are:

1. **`package.xml`**: The manifest file. This holds the package name, version, author info, and a list of all the dependencies (like `rclpy`) this package needs to run.
2. **`setup.py`**: The build instructions. This is where you declare your `entry_points` (the actual nodes/executables) so ROS 2 knows how to run your code.
3. **`my_py_pkg/` (The inner folder)**: This is where you actually save your Python scripts (e.g., `node1.py`). Note: It has the exact same name as the outer package folder.

---

## 3. The Build Step
After creating a package (or adding a new node to it), you must compile the workspace from the root directory:

```bash
cd ~/ros2_ws
colcon build --packages-select my_py_pkg
source ~/.bashrc
```