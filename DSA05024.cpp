#include <iostream>
#include <vector>

using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        vector<int> ls(n);
        for (int i = 0; i < n; ++i) {
            cin >> ls[i];
        }

        vector<int> dp(k + 1, 0);
        dp[0] = 1;
        for (int i = 1; i <= k; ++i) {
            for (int j : ls) {
                if (j <= i) {
                    dp[i] += dp[i - j];
                    dp[i] %= 1000000007;
                }
            }
        }

        cout << dp[k] << endl;
    }
    return 0;
}
