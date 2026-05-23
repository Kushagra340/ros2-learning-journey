#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"


int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<rclcpp::Node>("add_two_ints_client_no_oop");

    auto client = node->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
    while (!client->wait_for_service(std::chrono::seconds(1))) {
        RCLCPP_INFO(node->get_logger(), "Waiting for service 'add_two_ints' to be available...");
    }

    auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
    request->a = 5;
    request->b = 3;
    auto result_future = client->async_send_request(request);
        if (rclcpp::spin_until_future_complete(node, result_future) ==
            rclcpp::FutureReturnCode::SUCCESS)
        {
            auto response = result_future.get();
            RCLCPP_INFO(node->get_logger(), "Result of %ld + %ld = %ld", request->a, request->b, response->sum);
        } else {
            RCLCPP_ERROR(node->get_logger(), "Failed to call service 'add_two_ints'");
        }

    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}
