#include <iostream>
int main(int argc, char const *argv[])
{
    std::string todoName = (std::string)argv[1];
    std::string command = "python create.py "+todoName;
    system(command.c_str());
    return 0;
}
