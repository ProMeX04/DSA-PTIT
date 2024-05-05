#include <iostream>
#include <algorithm>
#include <cstring>
using namespace std;

int longest_commom_substring(string a, string b) {
    int len_a = a.length();
    int len_b = b.length();

    int dp[len_b] = {0};

    for (auto x : a) {
        int MAX = 0;
        for (int i = 0; i < len_b; i ++) {
            if (x == b[i] and MAX != dp[i] - 1) dp[i] = max(MAX, dp[i]) + 1;
            else MAX = max (MAX, dp[i]);
        }
    }
    return *max_element(dp, dp + len_b);
}

int longest_commom_substring_2(string a, string b) {
    int len_a = a.length();
    int len_b = b.length();
    int dp[len_a + 1][len_b + 1];
    memset(dp, 0, sizeof(dp));
    for (int i = 1; i <= len_a; i ++) {
        for (int j = 1; j <= len_b; j ++) {
            dp[i][j] = max({dp[i - 1][j - 1] + (a[i - 1] == b[j - 1]), dp[i][j - 1], dp[i - 1][j]});
        }
    }
    return dp[len_a][len_b];
}



int main() {
    int t; cin >> t;
    while (t--) {
        string a, b; cin >> a >> b;
        cout << longest_commom_substring_2(a, b) << endl;
    }
}