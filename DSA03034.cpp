#include<iostream>
#include <vector>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n , m, p; cin >> n >> m >> p;
        vector<long long> A(n + 1), B(m + 1), C(p + 1);
        bool found = false;
        for (int i = 0; i < n ; i++) cin >> A[i];
        for (int i = 0; i < m ; i++) cin >> B[i];
        for (int i = 0; i < p ; i++) cin >> C[i];

        A[n] = B[m] = C[p] = 1e18;
        int i = 0 , j = 0, k = 0;
        while (i != n || j != m || k != p) {
            if (A[i] == B[j] && A[i] == C[k]) {
                cout << A[i] << " ";
                i++; j++; k++;
                found = true;
            }
            else {
                if (A[i] < B[j] || A[i] < C[k]) i++;
                if (B[j] < A[i] || B[j] < C[k]) j++;
                if (C[k] < B[j] || C[k] < A[i]) k++;
            }
        }
        if (!found) cout << "NO";
        cout << endl;
    }
}