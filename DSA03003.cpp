#include <iostream>
#include <algorithm>

using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        long long A[n];
        for (int i = 0; i < n ;i ++) cin >> A[i];

        sort (A, A+ n);

        long long res = 0;
        for (int i = 0; i < n ; i ++) {
            res += i * A[i];

            res %= 1000000007;
        }
        cout << res << endl;
    }
}