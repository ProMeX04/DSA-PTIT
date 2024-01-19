#include<iostream>
using namespace std;

bool ok = true;
void nextBinary(int n, int A[]) {
    int i = n;
    while (i >= 0 and A[i] == 1) {A[i] = 0; i --;}
    if (i < 0) ok = false;
    else {
        A[i] = 1;
    }
}
int main() {
    int n, k; cin >> n >> k;
    int A[n] = {0};
    int B[n];
    for (auto& x : B) cin >> x;

    int count = 0;
    while (ok) {
        int sum = 0;
        for (int i = 0; i < n; i++) {
            sum += A[i] * B[i];
        }
        if ( sum == k ) {
            for (int i = 0; i < n ; i++) {
                if (A[i]) cout << B[i] << " ";
            }
            cout << endl;
            count ++;
        }
        nextBinary(n - 1, A);
    }
    cout << count;
}