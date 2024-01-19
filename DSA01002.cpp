#include<iostream>
using namespace std;

void nextCombination (int A[], int n, int k) {
    int i = k;
    while (A[i] == n + i - k) i--;
    A[i]++;
    for (int j = i + 1; j <= k; j++) {
        A[j] = A[j - 1] + 1;
    }
}
int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int A[k + 1] = {0};
        A[0] = -1;
        for (int i = 1; i <= k; i ++) {
            cin >> A[i];
        }

        nextCombination(A, n, k);

        for (int i = 1; i <= k; i ++) {
            cout << A[i] << " ";
        }

        cout << endl;
    }
}