#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n, m; cin >> n >> m;
        int A[n + 1][m + 1] = {0};
        for (int i = 1; i <= n; i++) {
            for(int j = 1; j <= m; j ++) {
                cin >> A[i][j];
            }
        }

        int dp[n + 1][m + 1];
        for (auto &x : dp)
            for (auto &y : x) y = 99999999;

        dp[1][1] = 0;
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= m; j++){
                if (i == 1 and j == 1) {
                    dp[i][j] = 0;
                }
                else {
                    dp[i][j] = min ({dp[i - 1][j] + abs(A[i][j] - A[i - 1][j]),
                                    dp[i][j - 1] +  abs(A[i][j] - A[i][j - 1]),
                                    dp[i - 1][j - 1] +  abs(A[i][j] - A[i - 1][j - 1])});
                }
            }
        }
        cout << dp[n][m] << endl;
        for (auto &x: dp){
            for (auto y : x){
                cout << y << ' ';
            }
            cout << endl;
        }
    }   
}