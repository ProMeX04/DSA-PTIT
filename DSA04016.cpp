#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n, m, k; cin >> n >> m >> k;
        int A[n], B[m];
        for (auto &x : A) cin >> x;
        for (auto &x : B) cin >> x;
        int C[n + m];
        merge(A, A + n, B, B + m, C);
        cout << C[k - 1] << endl;
    }
}