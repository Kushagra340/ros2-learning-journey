# ROS 2 Topics: The Data Stream

Topics are the backbone of ROS 2 communication, allowing different nodes (modules) to exchange data continuously. 

## 🧠 Core Concepts
* **The Concept:** A named bus over which nodes exchange messages.
* **Flow:** Unidirectional (One-way data streams).
* **Anonymity:** Publishers do not know who is subscribing, and subscribers do not know who is publishing.
* **Naming:** Topic names must always start with a letter. 

## ⚙️ Implementation Rules
To successfully implement topic communication in your application, two strict conditions must be met:
1. **Matching Names:** The Publisher and Subscriber must use the exact same topic name.
2. **Matching Types:** The Publisher and Subscriber must use the exact same data type (message type).

## 🛠️ System Architecture
* **Node Integration:** You can create any number of publishers and subscribers inside a single node.
* **Debugging:** Once launched, topic communication happens automatically. You can monitor and debug it using standard `ros2` command-line tools or the graphical `rqt` interface.

> **When to use a Topic:** Use topics when you are just sending or streaming data continuously (like sensor readings) and do not need a direct response back from the receiver.