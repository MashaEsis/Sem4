// task.cpp : Этот файл содержит функцию "main". Здесь начинается и заканчивается выполнение программы.
//

#include <iostream>
extern "C" int some();

int main()
{
    std::cout << "Hello World!\n";
    std::cout << some();
}
