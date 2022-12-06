#include <iostream>
#include <fstream>
#include <string>

struct s {
    int first, second, third;
};

void rearrange(s& top, int cur) {
    if (cur < top.third) return;
    if (cur < top.second) {
        top.third = cur;
        return;
    }
    if (cur < top.first) {
        top.third = top.second;
        top.second = cur;
        return;
    }
    top.third = top.second;
    top.second = top.first;
    top.first = cur;
}

int main() {
    std::ifstream file("1.dat");
    int cur = 0;
    std::string text;
    s top {0, 0, 0};
    while (std::getline(file, text)) {
        if (text == "") {
            rearrange(top, cur);
            cur = 0;
        } else {
            cur += std::stoi(text);
        }
    }

    std::cout << top.first << " " << top.second << " "
              << top.third << " " << top.first+top.second+top.third
              << std::endl;
}