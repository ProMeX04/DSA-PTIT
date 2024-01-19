#include<iostream>
using namespace std;
int main(){   
    int t; cin >> t;
    while(t--) {
        int n; cin >> n;
        int A[n];
        for(auto &x : A) cin >> x;

        for(int i = 0; i < n; i++) {
            cout << '[' << A[i];
            for(int j = i + 1; j < n; j++) {
                cout <<" " << A[j];
            }
            cout << "]\n";
            for(int j = n - 1; j >= i; j --) {
                A[j] += A[j - 1];
            }
        }

    }
}