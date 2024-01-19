#include<iostream>
using namespace std;
bool check (int A[], int n) {
    for (int i = 1; i < n ; i++) {
        if ( A[i] == 1 and A[i - 1] == 1) return false;
        if ( i > 3 and A[i] == 0 and A[i - 1] == 0 and A[i - 2] == 0 and A[i - 3] == 0) return false;
    }
    return true;
}

int ok = true;
void nextBinary(int A[], int n) {
    int i = n - 1;
    while (A[i] == 1 and i >= 0) A[i--] = 0;
    if (i >= 0) {
        A[i] = 1;
    }
    else ok = false;
}


int main() {
    int n; cin >> n;
    int A[n] = {0};
    A[0] = 1;
    A[1] = 0;
    A[n - 1] = 0;

    while (ok) {
        if (check(A, n)) {
            for (auto x : A) cout << (x ? 8 : 6);
            cout << endl;
        }
        nextBinary(A + 2, n - 3);
    }

}