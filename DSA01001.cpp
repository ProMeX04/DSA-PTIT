#include<iostream>
using namespace std;

void nextBinary(int A[], int n){
    int i = n - 1;
    while(A[i] == 1 and i >= 0) {
        A[i] = 0;
        i --;
    }
    if (i >= 0) {
        A[i] = 1;
    }
}
int main() {
    int t; cin >> t;
    while (t--) {
        string s; cin >> s;
        int n = s.length();
        int A[n];
        for (int i = 0 ; i < n ; i++) {
            A[i] = s[i] - '0';
        }
        nextBinary(A, n);
        for(auto x: A) cout << x;
        cout << endl;
    }
}