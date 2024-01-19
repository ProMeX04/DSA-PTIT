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
        int n, k; cin >> n >> k;
        int A[n] = {0};
        ok = true;
        while (ok) {
            int count = 0;
            for (auto x : A) {
                if (x == 1) count ++;
            }
            if (count == k) {
                for (auto x : A) cout << x;
                cout << endl;
            }
            nextBinary(A, n);

        }
    }
}