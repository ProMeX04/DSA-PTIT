#include <iostream>
using namespace std;

const int mod = 1e9 + 7;

long long Pow(long long n, long long m) {
    if ( m == 0) return 1;
    long long temp = Pow(n, m / 2) % mod;
    if (m % 2) return (temp * temp % mod * n) % mod;
    return temp * temp % mod;
}

long long rev(long long n) {
    long long rev = 0;
    while (n) {
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev;
}
int main() {
    int t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        cout << Pow (n, rev(n)) << endl;
    }
}