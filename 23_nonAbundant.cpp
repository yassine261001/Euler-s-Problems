#include <iostream>
#include <vector>
#include <unordered_set>

std::vector<int> getDivisors(int n) {
    std::vector<int> divisors;
    for (int i = 1; i < n; i++) {
        if (n % i == 0) {
            divisors.push_back(i);
        }
    }
    return divisors;
}

int main() {
    std::vector<int> abundant;
    const int LIMIT = 28123;

    for (int n = 1; n <= LIMIT; n++) {
        std::vector<int> divisors = getDivisors(n);
        int s = 0;
        for (int d : divisors) s += d;
        if (s > n) {
            abundant.push_back(n);
        }
    }

    std::unordered_set<int> abundantSums;
    for (int x : abundant) {
        for (int y : abundant) {
            if (x + y <= LIMIT) {
                abundantSums.insert(x + y);
            }
        }
    }

    long long result = 0;
    for (int i = 1; i <= LIMIT; i++) {
        if (abundantSums.find(i) == abundantSums.end()) {
            result += i;
        }
    }

    std::cout << result << std::endl;
    return 0;
}