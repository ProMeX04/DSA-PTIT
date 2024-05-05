#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    int n; cin >> n;
    int A[n];
    for (auto& x : A) cin >> x;
    int dp[n];
    for(int i = 0; i < n ; i++) {
        dp[i] = 1;
        for (int j = 0; j < i ; j ++) {
            if (A[j] < A[i]) dp[i] = max(dp[i], dp[j]  + 1); 
        }
    }
    cout << *max_element(dp, dp + n);

}
