#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k; 
        int A[n];
        for (auto &x : A) cin >> x;
        int pos = lower_bound(A, A + n, k) - A;
        if (A[pos] == k) cout << pos + 1<< endl;
        else cout << "NO\n";
    }   
}