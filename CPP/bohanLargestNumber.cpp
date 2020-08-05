#include <iostream>
#include <cstring>
#include <stddef.h>
#include <algorithm>
#include <vector>
#include <string>     // std::string, std::to_string
/*
    receive an array of non positive integers and arrange them such that they give
    the largest number possible. For exmaple below 3,30,34,5,9 should result in 
    9534330
*/
bool compareFunc(int i, int j)
{
    return std::to_string(i) + std::to_string(j) > 
           std::to_string(j) + std::to_string(i); 
}

std::string LargestNumber(int *arr, size_t size)
{
    std::vector<int> vec(arr, arr + size);
 
    std::sort(vec.begin(), vec.end(), compareFunc);
    
    std::cout << "\n";
    for (size_t i = 0; i < vec.size(); ++i)
    {
        std::cout << vec[i];
    }

    std::string str;

    return str;
}

int main()
{
    int arr[] = {3,30,34,5,9};
    LargestNumber(arr, 5);



    return 0;
}
