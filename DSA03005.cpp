#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t; cin >> t;
    while (t-- ) {
        int n, k; cin >> n >> k;
        int A[n];
        int sum = 0;
        for (auto&x : A){ cin >> x; sum += x;}
        sort (A, A + n , greater<int>());
        int m = 0;
        for (int i = 0; i < max(k,n - k); i++) {
            m += A[i];
        }
        cout << 2 * m - sum<< endl;

    }
}