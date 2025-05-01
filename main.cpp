#include <iostream>
#include <spdlog/spdlog.h>

int main()
{
    std::cout << "Hello, World!" << std::endl;
    spdlog::info("Hello, spdlog!");
    return 0;
}