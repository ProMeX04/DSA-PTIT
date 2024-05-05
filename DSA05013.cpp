#include <iostream>
#include <vector>
using namespace std;
typedef vector<long long> vll;

const int mod = 1e9 + 7;
long long stairs (long long n, long long k) {
    vll dp(n + 1, 0);
    long long x = 1;
    long long sum = 0;
    for (int i = 1; i <= k; i ++) {
        dp[i] = x;
        x *= 2;
        x %= mod;
        sum += dp[i];
        sum %= mod;
    }
    for (int i = k + 1; i <= n ; i++) {
        sum %= mod;
        dp[i] = sum;
        sum -= dp[i - k];
        sum += dp[i];
    }
    return dp[n];
        
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n, k;
        cin >> n >> k;
        cout << stairs (n , k)<< endl;
    }
}