#include <iostream>
using namespace std;

const int mod = 1e9 + 7;

long long Pow(long long n, long long m) {
    if ( m == 0) return 1;
    long long temp = Pow(n, m / 2) % mod;
    if (m % 2) return (temp * temp % mod * n) % mod;
    return temp * temp % mod;
}

int main(){   
    long long a, b;
    while (cin >> a >> b) {
        if (a == 0 and b == 0) {
            break;
        }
        else {
            cout << Pow(a, b) << endl;
        }
    }
}