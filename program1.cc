//Written by Rasoul Nikmehr

#include <iostream> 
#include <cmath> // Includes pow()

int convert(int input, int base) {
    int sum = 0;
    int position = 0;

    while (input != 0) {
        int tmp = input % 10;
        sum += (tmp * pow(base, position));
        position++;
        input /= 10;
    }

    return sum;
}


int main() {

    int input;
    int base;
   
   // Read input and base from standard input
    std::cin >> input >> base;


    if (base < 2 || base > 9)  {
        std::cout << "Base Not Accepted";

        return 0;
    }

   
    int maxAllowedDigit = base - 1;
    int tempNumber = input;
//Making sure that all the digits are less than base
    while (tempNumber != 0) {
        int tmp = tempNumber % 10;
        if (tmp > maxAllowedDigit) {
            std::cout << "Invalid Digit(s) In Number" << std::endl;
            return 0;
        }
        tempNumber /= 10;
    }

    int result = convert(input, base);

   
    std::cout << result << std::endl;


    return 0;
}