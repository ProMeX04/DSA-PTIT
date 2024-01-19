#include<iostream>
#include <algorithm>
using namespace std;
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int A[n];
        for (int i = n - 1; i >= 0; i--) {
            A[i] = n - i;
        }

        int gt = 1;
        for (int i = 1; i <= n ; i++) gt *= i;

        while (gt--) {
            for (auto x : A) cout << x;
            cout << " ";
            prev_permutation(A, A + n);
        }
        cout << endl;
    }
}