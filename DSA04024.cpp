#include <iostream>
#include <vector>
using namespace std;

typedef vector<vector<long long>> vll;
const int mod = 1e9 + 7;

vll operator*(vll A, vll B) {
    int n = A.size();
    int m = B[0].size();
    int p = A[0].size();

    vll C(n, vector<long long>(m));

    for (int i = 0; i < n; i ++) {
        for (int j = 0; j < m; j ++) {
            for (int k = 0; k < p; k ++) {
                C[i][j] += A[i][k] * B[k][j];
                C[i][j] %= mod;
            }
        }
    }
    return C;
}

vll pow(vll A, int k) {
    if (k == 1) return A;
    vll temp = pow(A, k / 2);
    if (k % 2) return temp * temp * A;
    else return temp * temp;
}


int main() {
    int t; cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vll A(n, vector <long long>(n));
        for (auto &x : A) {
            for (auto &y : x) cin >> y;
        }
        vll C = pow(A, k);
        long long res = 0;
        for (auto x : C) res += *x.rbegin();

        cout << res % mod << endl;
    }
}