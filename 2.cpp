#include <iostream>
#include <fstream>
#include <string>

int get_score1(char a, char b){
    int initial = b-'X'+1;
    char _b = b-('X'-'A');
    int win = (_b-a+4)%3;
    int score = initial + win*3;
    return score;
}

int get_score2(char a, char b){
    char c;
    const char offset = 'X'-'A';
    if (b=='X') c=a+offset-1;
    else if (b=='Y') c=a+offset;
    else c=a+offset+1;
    if (c<'X') c+=3;
    if (c>'Z') c-=3;
    return get_score1(a,c);
}

int main() {
    int score1=0, score2=0;

    std::ifstream file("2.dat");
    char a, b;
    while (file >> a >> b) {
        score1 += get_score1(a,b);
        score2 += get_score2(a,b);
    }
    std::cout << score1 << std::endl << score2 << std::endl;
}