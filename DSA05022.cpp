#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int t; cin >> t;
    while (t--) {
        int n;
        cin >> n;
        int x, y, z;
        cin >> x >> y >> z;

        vector<int> dp(n + 1);
        dp[1] = x;
        dp[2] = x + min(x, z);

        for (int i = 3; i <= n; ++i) {
            dp[i] = min(dp[(i + 1) / 2] + z + (i % 2) * y, dp[i - 1] + x);
        }

        cout << dp[n] << endl;
    }
}
