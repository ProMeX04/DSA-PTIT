#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int A[n];
        for (auto &x :A) cin >> x;
        int pos = upper_bound(A, A + n, k) - A;
        if (pos == 0) cout << -1;
        else {
            cout << pos;
        }
        cout << endl;
    }   
}