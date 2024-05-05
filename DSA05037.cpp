#include <iostream>
const int mod = 1e9 + 7;
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n;cin >> n;
        long long dp[n + 1][10 + 1];
        for (int i = 0; i < 10; i ++){
            dp[0][i] = 1;
        }
        for (int i = 1; i <= n ; i++) {
            long long sum = 0;
            for (int j = 9; j >= 0; j--){
                sum += dp[i - 1][j];
                sum %= mod;
                dp[i][j] = sum;
            }
        }
        cout << dp[n][0] << endl;
    }
}