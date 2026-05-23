#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoIntsServerNode : public rclcpp::Node 
{
public:
    AddTwoIntsServerNode() : Node("add_two_ints_server") 
    {
        server_ = this->create_service<example_interfaces::srv::AddTwoInts>(
            "add_two_ints",
            std::bind(&AddTwoIntsServerNode::callback_add_two_ints, this, std::placeholders::_1, std::placeholders::_2)
        );
    }

private:
    void callback_add_two_ints(
        const std::shared_ptr<example_interfaces::srv::AddTwoInts::Request> request,
        const std::shared_ptr<example_interfaces::srv::AddTwoInts::Response> response)
    {
        response->sum = request->a + request->b;
        RCLCPP_INFO(this->get_logger(), "Received request: a=%ld, b=%ld, responding with sum=%ld", request->a, request->b, response->sum);
    }
    rclcpp::Service<example_interfaces::srv::AddTwoInts>::SharedPtr server_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoIntsServerNode>(); 
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
