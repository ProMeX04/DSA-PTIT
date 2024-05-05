#include <iostream>
#include <algorithm>
using namespace std;
int main () {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int A[n];
        for (auto &x : A) cin >> x;

        long long dp[n];
        for (int i = 0; i < n; i ++) {
            dp[i] = A[i];
            for (int j = 0; j < i; j++) {
                if (A[i] > A[j])
                    dp[i] = max(dp[i], dp[j] + A[i]);
            }
        }
        cout << *max_element(dp, dp + n) << endl;
    }
}