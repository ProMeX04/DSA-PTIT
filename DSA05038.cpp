#include <iostream>
#include <map>
using namespace std;
int main () {
    int n; cin >> n;
    int A[n], B[n];
    for (int i = 0; i < n; i ++) {
        cin >> A[i] >> B[i];
    }
    map<int, map<int, int>> mp;
    map<int, map<int, int>> mp1;
    int res = 0;
    for (int i = 0; i < n; i++) {
        int k = 0;

        auto x = mp.lower_bound(A[i]);
        while (x != mp.begin()) {
            x--;
            auto y = x->second.lower_bound(B[i]);
            if (y != x -> second.begin()) {
                y--;
                k = max(y -> second + 1, k);
            }
        }

        mp[A[i]][B[i]] = k;
        res = max(res, k);
    }
    cout << res + 1;
}
