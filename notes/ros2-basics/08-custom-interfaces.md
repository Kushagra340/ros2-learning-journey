# Custom Interfaces in ROS 2

While standard messages (like `geometry_msgs/Twist`) are great, complex robotic systems often require custom data structures. In ROS 2, we define these using `.msg` (for Topics) and `.srv` (for Services) files.

## The "Dictionary" Rule (Architectural Best Practice)
Custom interfaces act as a shared dictionary for your robot. 
It is a strict best practice to keep all `.msg` and `.srv` files in a **dedicated, independent package** (e.g., `my_robot_interfaces`) rather than bundling them inside the nodes that use them. 

* **Why?** If Node A and Node B need to talk, keeping the message definition in a third, independent package prevents messy, circular dependencies. It keeps the codebase modular.

## The Python Limitation
ROS 2 physically cannot generate custom interfaces inside a pure Python (`ament_python`) package. The `rosidl` compiler relies on CMake to translate the interface files into usable code across different languages. 
* **The Solution:** Always create your interface package as a C++ (`ament_cmake`) build type. Python nodes can then easily import the compiled messages from this CMake package.

## Creating a Custom Message (.msg)
Used for broadcasting data on a Topic.
```text
# Example: Turtle.msg
string name
float64 x
float64 y
float64 theta
```

## Creating a Custom Service (.srv)
Used for synchronous Client/Server requests. It uses --- to separate the Request from the Response.
```text
string name
---
bool success
```

## Updating CMakeLists.txt
To compile the interfaces, you must add them to the rosidl_generate_interfaces block in the interface package's CMakeLists.txt:
```cmake
rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/Turtle.msg"
  "srv/CatchTurtle.srv"
)
```