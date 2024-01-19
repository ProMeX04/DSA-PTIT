#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int count = 0;
        int x;
        for (int i = 0; i < n ; i++) {
            cin >> x;
            count += x;
        }
        cout << n - count << endl;
    }
}