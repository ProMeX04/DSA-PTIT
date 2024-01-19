#include<iostream>
using namespace std;

bool check(int A[], int n) {
    for (int i = 1; i < n; i++) {
        if (A[i] == 1 and A[i - 1] == 1) {
            return 0;
        }
    }
    return A[0] == 1 and A[n - 1] == 0;
}


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
        ok = true;
        int A[n] = {0};
        while (ok) {
            if (check(A, n)) {
                for (auto x : A) cout << (x ? 'H' : 'A');
                cout << endl;
            }
            nextBinary(A, n);
        }
    }
}