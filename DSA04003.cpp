#include <iostream>
using namespace std;

const int mod = 123456789;

long long Pow(long long n, long long m) {
    if ( m == 0) return 1;
    long long temp = Pow(n, m / 2) % mod;
    if (m % 2) return (temp * temp % mod * n) % mod;
    return temp * temp % mod;
}
int main() {
    int t; cin >> t;
    while (t--) {
        long long n;
        cin >> n;
        cout << Pow(2, n - 1) << endl;
    }
}