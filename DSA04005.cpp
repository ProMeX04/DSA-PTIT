#include <iostream>
using namespace std;
long long fib[100];

char findChar(long long n, long long pos) {
    if (n == 1) return 'A';
    if (n == 2) return 'B';

    if (pos > fib[n - 2]) return findChar(n - 1, pos - fib[n - 2]);
    return findChar(n - 2, pos);
}

void Fib() {
    fib[1] = 1;
    fib[2] = 1;

    for (long long i = 3; i <= 93 ; i++) {
        fib[i] = fib[i - 1] + fib[i - 2];
    }
}

int main() {
    Fib();
    int t; cin >> t;
    while (t--) {
        long long n, pos; cin >> n >> pos;
        cout << findChar(n, pos) << endl;

    }
}