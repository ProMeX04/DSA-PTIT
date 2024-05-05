#include <iostream>
#include <vector>

using namespace std;
const int MOD = 1000000007;

int function(int n, int k) {
    vector<vector<int>> dp(n + 1, vector<int>(k + 1, 1));

    for (int i = 1; i <= n; ++i) {
        for (int j = 1; j <= k; ++j) {
            if (i == j || j == 0) {
                dp[i][j] = 1;
            } else if (j > i) {
                dp[i][j] = 0;
            } else {
                dp[i][j] = (dp[i - 1][j - 1] + dp[i - 1][j]) % MOD;
            }
        }
    }

    return dp[n][k];
}

int main() {
    int t;
    cin >> t;

    for (int i = 0; i < t; ++i) {
        int n, k;
        cin >> n >> k;
        cout << function(n, k) << endl;
    }

    return 0;
}
