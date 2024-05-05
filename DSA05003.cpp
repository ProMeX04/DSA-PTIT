#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;

    while (T--) {
        int n, m, p;
        cin >> n >> m >> p;
        string s1, s2, s3;
        cin >> s1 >> s2 >> s3;

        vector<vector<vector<int>>> dp(n + 1, vector<vector<int>>(m + 1, vector<int>(p + 1, 0)));

        for (int i = 1; i <= n; ++i) {
            for (int j = 1; j <= m; ++j) {
                for (int k = 1; k <= p; ++k) {
                    dp[i][j][k] = max({dp[i][j - 1][k], dp[i][j][k - 1], dp[i - 1][j][k]});
                    if (s1[i - 1] == s2[j - 1] && s2[j - 1] == s3[k - 1]) {
                        dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j - 1][k - 1] + 1);
                    }
                }
            }
        }

        cout << dp[n][m][p] << endl;
    }

    return 0;
}
