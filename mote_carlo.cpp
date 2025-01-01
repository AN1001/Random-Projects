//Mpnte Carlo simulation for a probability problem I once found
#include <iostream>
#include <random>
#include <cmath>

int main() {
    double target = 0;
    double hits = 1;
    double misses = 1;

    std::cout << "begin with target: " << target << std::endl;

    // Initialize random number generator once
    std::random_device rd;
    std::mt19937 gen(rd());
    std::uniform_real_distribution<> dist(0.0, 1.0);

    for(int i = 0; i < 10000000; i++) {
        // Generate random x and y between 0 and 1
        double x = dist(gen);
        double y = dist(gen);

        // Avoid division by zero
        if (y == 0) y = 1e-9;

        // Calculate floor(x/y)
        double result = std::floor(x / y);

        // Count hits and misses
        if(result == target) {
            hits++;
        } else {
            misses++;
        }
    }

    std::cout << std::endl << "Approx ~ " << hits / misses << std::endl;
    return 0;
}

