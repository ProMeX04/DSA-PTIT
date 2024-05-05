#include <iostream>
#include <algorithm>
using namespace std;
int main() {
    long long t; cin >> t;
    while (t--) {
        long long n; cin >> n;
        long long A[n];
        for (auto& x : A) cin >> x;
        long long dp[n];
        for (long long i = 0; i < n ; i++) {
            dp[i] = 1;
            for (long long j = 0; j < i ; j ++) {
                if (A[j] <= A[i]) dp[i] = max(dp[i], dp[j]  + 1);
            }
        }
        cout << n - *max_element(dp, dp + n) << "\n";
    }
}