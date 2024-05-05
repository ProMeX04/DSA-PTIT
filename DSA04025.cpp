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

vll operator^(vll A, int k) {
    if (k == 1) return A;
    vll temp = A ^ (k / 2);
    if (k % 2) return temp * temp * A;
    else return temp * temp;
}


int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vll C = ((vll) {{1, 1}, {1, 0}}^n ) * (vll) {{1}, {0}};
        cout << C[1][0] << endl;
    }
}