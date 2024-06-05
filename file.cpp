#include <iostream>
#include <cstdlib>
#include <ctime>

int main() {
    // Seed the random number generator
    srand(time(0));

    // Generate and print a random number between 1 and 100
    int randomNumber = rand() % 100 + 1;
    std::cout << "Random number: " << randomNumber << std::endl;

    return 0;
}

