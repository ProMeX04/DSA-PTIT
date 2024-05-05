#include <iostream>
#include <vector>
using namespace std;
int main(){   
    int n, m; cin >> n >> m;
    int bills[10000];
    for (int i = 0 ; i < n; i++) cin >> bills[i];
    vector<int> dp(100000, 99999999);

    dp[0] = 0;
    for (int i = 0; i < n; i++){
        for (int j = m; j >= 0; j--){
            if (bills[i] + j <= m)
                dp[bills[i] + j] = min(dp[bills[i] + j], dp[j] + 1);
        }
    }
    if (dp[m] == 99999999) cout << -1;
    else cout << dp[m];

}