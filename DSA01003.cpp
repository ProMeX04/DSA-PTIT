#include<iostream>
#include <algorithm>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int A[n];
        for (int i = 0; i < n; i++) cin >> A[i];
        next_permutation(A, A + n);
        for (auto x : A) cout << x << " ";
        cout << endl;
    }
}