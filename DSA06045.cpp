#include <iostream>
#include <vector>
using namespace std;

int main() {
    int n;
    string s;
    cin >> n >> s;
    long long res = 0, tmp = 1;
    for (int i = 1; i < n; ++i) {
        if (s[i] == s[i - 1]) {
            tmp++;
            res += i - (tmp <= i);
        } else {
            res += i - tmp;
            tmp = 1;
        }
    }
    cout << res << endl;
    return 0;
}
