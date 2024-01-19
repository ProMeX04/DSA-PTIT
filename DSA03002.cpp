#include <iostream>
using namespace std;

long long convert (string a, char x, char y) {
    long long k = 0;
    for (auto c : a) {
        if (c == x) k = k * 10 + y -'0';
        else k = k * 10 + c -'0';
    }
    return k;
}
int main() {
    string a, b; cin >> a >> b;
    cout << convert(a, '6' , '5') + convert(b, '6' , '5') << " ";
    cout << convert(a, '5' , '6') + convert(b, '5' , '6');
}