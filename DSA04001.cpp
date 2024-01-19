#include <iostream>
using namespace std;

const int mod = 1e9 + 7;

long long Pow(int n, int m) {
    if ( m == 0) return 1;
    long long temp = Pow(n, m / 2) % mod;
    if (m % 2) return (temp * temp % mod * n) % mod;
    return temp * temp % mod;
}
int main() {
    int t; cin >> t;
    while (t--) {
        int n, m;
        cin >> n >> m;
        cout << Pow(n, m) << endl;
    }
}