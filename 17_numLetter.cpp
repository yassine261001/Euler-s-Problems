#include <cstddef>
#include <iostream>
#include <string>
#include <vector>

std::string convert_number(int input) {

  std::vector<int> digits;
  int x = input;
  while (x) {
    digits.push_back(x % 10);
    x /= 10;
  }
  std::reverse(digits.begin(), digits.end());

  std::vector<std::string> suffixes = {"", "hundred", "thousand", "million",
                                       "billion"};

  std::vector<std::string> overTwenty = {"",       "ten",   "twenty", "thirty",
                                         "forty",  "fifty", "sixty",  "seventy",
                                         "eighty", "ninety"};

  std::vector<std::string> underTwenty = {
      "",        "one",     "two",       "three",    "four",
      "five",    "six",     "seven",     "eight",    "nine",
      "ten",     "eleven",  "twelve",    "thirteen", "fourteen",
      "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"};

  if (input == 0) {
    return "zero";
  }

  if (input < 20) {
    return underTwenty[input];
  }

  if (input >= 20 && input % 10 == 0 && input < 100) {
    return overTwenty[input / 10];
  }

  if (input > 20 && input < 100) {
    return overTwenty[digits[0]] + " " + underTwenty[digits[1]];
  }

  if (input >= 100 && input <= 999) {
    if (digits[1] == 0 && digits[2] == 0) {
      return underTwenty[digits[0]] + " " + suffixes[1];
    }

    if (digits[1] == 1) {
      return underTwenty[digits[0]] + " " + suffixes[1] + " and " +
             underTwenty[digits[2] + 10];
    }

    if (digits[1] == 0) {
      return underTwenty[digits[0]] + " " + suffixes[1] + " and " +
             underTwenty[digits[2]];
    }

    if (digits[2] == 0) {
      return underTwenty[digits[0]] + " " + suffixes[1] + " and " +
             overTwenty[digits[1]];
    } else {
      return underTwenty[digits[0]] + " " + suffixes[1] + " and " +
             overTwenty[digits[1]] + " " + underTwenty[digits[2]];
    }
  }

  if (input == 1000) {
    return underTwenty[digits[0]] + " " + suffixes[2];
  }
  return NULL;
}

int main() {
  for (int i = 1; i < 1001; i++)
    std::cout << convert_number(i) << std::endl;
}
