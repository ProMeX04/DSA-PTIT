#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int A[n];
        for (auto &x : A) cin >> x;
        sort (A , A + n);
        long long k1 = 0, k2 = 0;
        for (int i = 0; i < n; i ++) {
            if (i%2 == 0) k1 = k1 *10 + A[i];
            else k2 = k2 * 10 + A[i];
        }
        cout << k1 + k2 << endl;
    }
}