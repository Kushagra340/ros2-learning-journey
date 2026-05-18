# Basics 02: Creating a C++ Package

## 1. The Creation Command
To create a new ROS 2 C++ package, you must be inside the `src` folder of your workspace.

```bash
cd ~/ros2_ws/src
ros2 pkg create my_cpp_pkg --build-type ament_cmake --dependencies rclcpp
```

### The Command Breakdown:
* `ros2 pkg create`: The core ROS 2 command to generate the package template.
* `my_cpp_pkg`: The name of your package (always use lowercase and underscores).
* `--build-type ament_cmake`: CRITICAL. This tells the `colcon` build system to use CMake to compile this as a C++ project.
* `--dependencies rclcpp`: Automatically injects the ROS 2 C++ client library (`rclcpp`) into your `package.xml` and `CMakeLists.txt`.

---

## 2. The Core Files Generated
The C++ architecture is slightly different from Python. The most important files/folders are:

1. **`package.xml`**: The manifest file. Identical purpose to Python, but holds C++ dependencies (like `rclcpp`).
2. **`CMakeLists.txt`**: The C++ equivalent of `setup.py`. This is a highly specific file where you tell the compiler exactly which `.cpp` files to turn into executables, and which libraries to link them against.
3. **`src/` folder**: This is where you save your actual C++ source code files (e.g., `node1.cpp`).
4. **`include/` folder**: This is where you save your C++ header files (`.hpp` or `.h`) if you are writing complex, multi-file programs.

---

## 3. The Build Step
C++ packages take slightly longer to build because they actually compile down to machine code. Run this from the workspace root:

```bash
cd ~/ros2_ws
colcon build --packages-select my_cpp_pkg
source ~/.bashrc
```