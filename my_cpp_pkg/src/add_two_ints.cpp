#include "rclcpp/rclcpp.hpp"
#include "example_interfaces/srv/add_two_ints.hpp"

class AddTwoInts : public rclcpp::Node 
{
public:
    AddTwoInts() : Node("add_two_ints") 
    { 
        client_ = this->create_client<example_interfaces::srv::AddTwoInts>("add_two_ints");
    }

    void call_add_two_ints(int64_t a, int64_t b)
    {
        while (!client_->wait_for_service(std::chrono::seconds(1))) {
            RCLCPP_INFO(this->get_logger(), "Waiting for service 'add_two_ints' to be available...");
        }

        auto request = std::make_shared<example_interfaces::srv::AddTwoInts::Request>();
        request->a = a;
        request->b = b;

       
        client_->async_send_request(request, 
            [this, a, b](rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedFuture future) {
                try {
                    auto response = future.get();
                    RCLCPP_INFO(this->get_logger(), "Result of %ld + %ld = %ld", a, b, response->sum);
                } catch (const std::exception &e) {
                    RCLCPP_ERROR(this->get_logger(), "Service call failed");
                }
            }
        );
    }

private:
    
    rclcpp::Client<example_interfaces::srv::AddTwoInts>::SharedPtr client_;
};

int main(int argc, char **argv)
{
    rclcpp::init(argc, argv);
    auto node = std::make_shared<AddTwoInts>(); 
    node->call_add_two_ints(5, 3);
    rclcpp::spin(node);
    rclcpp::shutdown();
    return 0;
}