# ROS 2 Parameters & YAML Configurations

Parameters act as the "settings" or "configuration" for your ROS 2 nodes. Instead of hardcoding values directly into your Python or C++ scripts, parameters allow you to change how a node behaves on the fly at runtime.

## 🧠 Core Concepts
* **Definition:** Settings for your nodes, with values that can be dynamically set or changed at runtime.
* **Scope:** A parameter is always specific to a single node. 
* **Data Types Supported:**
  * Booleans (`True` / `False`)
  * Integers (`5`, `7`)
  * Doubles/Floats (`0.5`, `3.14`)
  * Strings (`"robot_news"`)
  * Lists (Arrays of the above types)

## 📄 Using YAML Files for Parameters
When you have multiple nodes or lots of settings, typing them into the terminal one by one is inefficient. ROS 2 uses **YAML files** to store and load multiple parameters at once.

### The YAML Structure
YAML relies heavily on exact indentation (use spaces, never tabs). Here is the standard blueprint for a ROS 2 parameter file:

```yaml
/number_publisher1:
  ros__parameters:
    number: 7
    timer_period: 1.0

/number_publisher2:
  ros__parameters:
    number: 5
    timer_period: 0.5
```

### The Execution command:
```bash 
ros2 run my_py_pkg number_publisher --ros-args -r __node:=number_publisher2 --params-file ~/yaml_params/number_params.yaml
```
