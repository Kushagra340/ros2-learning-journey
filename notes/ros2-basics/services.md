# ROS 2 Services: Call and Response

Services provide a structured way for nodes to ask questions and receive specific answers, acting as the primary Request/Response mechanism in ROS 2.

## 🧠 Core Concepts
* **The Concept:** A classic Client/Server communication model.
* **Execution:** Can be synchronous or asynchronous (though Asynchronous is highly recommended, even if you wait for the response later in the thread).
* **Anonymity:** A client does not know which node hosts the service, and the server does not know which nodes are calling it.

## ⚙️ Implementation Rules
To successfully call a Service Server from a Service Client, you must ensure:
1. **Matching Names:** The Service name must be identical on both sides.
2. **Matching Types:** The Service type (which includes both the Request and Response structure) must be identical.

## 🛠️ System Architecture
* **Node Integration:** A single node can host as many Service servers as you want, provided they all have unique names.
* **The Golden Rule of Services:** You can only create **ONE** Server for a specific service, but you can have **MANY** Clients calling that server.

> **When to use a Service:** Ask yourself, *"Am I just sending data, or do I expect a specific response after I send the message?"* If you expect a response (like asking a robot to calculate a path and return the result), use a Service.