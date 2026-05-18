# ROS2 Foundations & Architecture Notes

## 🧠 Core Learning Philosophy
This section documents the foundational concepts of ROS2 (Robot Operating System). The philosophy of these notes is **understanding over memorization**. 

ROS2 is not "robot code." It is a robotics middleware, a distributed communication architecture, and a message-passing infrastructure. The goal here is to understand *why* subsystems interact, *how* data flows, and *where* failures happen, rather than just memorizing CLI syntax.

---

## 🏗️ Middleware & Communication Architecture
At its core, ROS2 allows isolated programs to communicate with each other seamlessly.

* **Nodes:** The fundamental compute units. Single-purpose executable programs (e.g., a node for reading an encoder, a node for calculating odometry).
* **Topics:** The named buses over which nodes exchange messages. They act as the nervous system of the robot.
* **Publishers & Subscribers:** The standard unidirectional communication model. A node *publishes* data to a topic; another node *subscribes* to that topic to read it.
* **Messages:** The strictly typed data structures sent over topics (e.g., `geometry_msgs/msg/Twist`).
* **Services:** Synchronous, request-response communication (useful for quick, discrete actions like resetting a sensor).
* **Actions:** Asynchronous, goal-oriented communication with continuous feedback (useful for long-running tasks like navigating to a waypoint).

---

## 🌐 Distributed Robotics Architecture
This project intentionally separates high-level compute from low-level hardware control, mirroring real-world distributed systems:

1.  **Orchestration Layer (Laptop/Ubuntu/WSL2):** Hosts the heavy ROS2 compute, Gazebo simulation, RViz visualization, and high-level decision logic.
2.  **Embedded Interface Layer (ESP32):** Handles real-time motor control (via DRV8833), encoder reading, and sensor acquisition (MPU6050, VL53L0X TOF).

This physical separation forces a deep understanding of hardware abstraction and network-based message passing.

---

## ⚙️ Differential Drive & Motion Abstraction
The robot utilizes a 2WD differential drive architecture. Motion emerges entirely from the relative velocity differences between the left and right wheels. 

We abstract this low-level wheel control using standard ROS2 conventions:
* **`/cmd_vel` Topic:** The standard topic for velocity commands.
* **`linear.x`:** Forward/backward translational velocity.
* **`angular.z`:** Rotational velocity around the vertical axis.

---

## 💻 Simulation-First Workflow
Before deploying code to physical hardware, algorithms and communication graphs are verified in simulation.

* **Turtlesim:** The ROS2 architecture sandbox. Used to master topic communication, coordinate systems, and ROS graph interactions without hardware overhead.
* **Gazebo:** The physics-based simulation environment for the 3D differential drive model.
* **RViz:** The primary visualization tool for sensor data (IMU, TOF) and TF (Transform) trees.

---

## 🐛 Debugging Philosophy
**Debugging IS robotics.** Encountering communication drops, odometry drift, electrical noise, and tf-tree conflicts are not failures; they are the core curriculum. Understanding *why* a system failed is more valuable than having it work perfectly on the first try.