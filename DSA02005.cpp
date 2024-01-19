#include <iostream>
#include <algorithm>

using namespace std;
int main(){   
    int t; cin >> t;
    while(t--) {
        string s; cin >> s;
        int n = s.length();
        int A[n];
        for(int i = 1; i <= n; i++) A[i - 1] = i;
        int times = 1;
        for(int i = 2; i <= n; i++) times *= i;

        while( times -- ) {
            for(int i = 0; i < n; i++) {
                cout << s[A[i] - 1];
            }
            cout << " ";
            next_permutation(A, A+n);
        }
        cout << endl;
    }
}