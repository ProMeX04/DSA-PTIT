#include<iostream>
using namespace std;
int ok = true;
void nextBinary(int A[], int n) {
    int i = n - 1;
    while (A[i] == 1 and i >= 0) {
        A[i] = 0;
        i --;
    }
    if (i >= 0) {
        A[i] = 1;
    }
    else ok = false;
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        int A[n] = {0};
        ok = true;
        while (ok) {
            for (auto x : A) cout << char('A' + x);
            nextBinary(A, n);
            cout << " ";
        }
        cout << endl;
    }
}