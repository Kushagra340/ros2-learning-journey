# ROS 2 Launch Files (XML)

Starting multiple nodes across different terminals is tedious and scales poorly. Launch files solve this by letting us start entire robotic systems, inject parameters, and remap topics with a single command.

## XML Launch Architecture
In ROS 2, launch files can be written in Python, XML, or YAML. XML is highly readable and great for standard node orchestration.

### Standard Node Tag
To launch a node, you need three essential attributes:
* `pkg`: The name of the package.
* `exec`: The name of the executable (defined in `setup.py` or `CMakeLists.txt`).
* `name`: The runtime name of the node.

```xml
<node pkg="turtlesim" exec="turtlesim_node" name="sim" />
```

## Injecting Parameters
You can dynamically pass parameters into a node at launch time without changing the source code. This is crucial for tuning variables on the fly.

```xml
<node pkg="my_robot_bringup" exec="turtle_spawner" name="spawner">
    <param name="spawn_frequency" value="1.5" />
</node>
```
## Remapping Topics
If a node expects a topic named /cmd_vel but your specific robot namespace uses /turtle1/cmd_vel, you can remap it directly in the launch file without rewriting the node logic:

```xml
<remap from="/cmd_vel" to="/turtle1/cmd_vel" />
```

## Execution
Launch files are typically stored in a dedicated package (e.g., my_robot_bringup/launch/).
Run them using:
ros2 launch <package_name> <launch_file_name.launch.xml>

