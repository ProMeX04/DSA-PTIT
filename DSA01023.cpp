#include<iostream>
using namespace std;

int cnt = 0;
int result = 0;
bool check (int A[], int B[], int n) {
    for (int i = 0; i < n; i++) {
        if (A[i] != B[i]) return false;
    }
    return true;
}

void Try(int A[], int B[], int j, int n, int k, int min) {
    if (j == k) {
        cnt ++;
        if (check(A, B, k) == true) {
            result = cnt;
        }
    }

    else if (!result) {
        for (int i = min; i <= n - k + j; i++ ) {
            B[j] = i + 1;
            Try(A, B, j + 1, n, k, i + 1);
        }
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int A[k];
        for (auto &x : A) cin >> x;
        cnt = 0;
        result = 0;
        int B[n];
        Try(A, B, 0, n, k, 0);
        cout << result << endl;

    }
}