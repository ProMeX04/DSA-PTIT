#include <iostream>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        long long A[n];
        for (auto &x : A) cin >> x;
        long long result = 0;
        for (int i = 0; i < n - 1; i++) {
            long long x; cin >> x;
            if (x != A[i] and result == 0) result = i + 1;

        }   
        cout << result << endl;
    }   
}