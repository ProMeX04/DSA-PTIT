#include <iostream>
#include <vector>
using namespace std;


void print(int i, vector<int> A, int n) {
    for (int j = 0; j < n - i; j ++) {
        A[j] += A[j + 1];
    }
    if (i < n - 1) print(i + 1, A, n);

    cout << '[' << A[0];
    for (int j = 1; j < n - i; j++) {
        cout << " " << A[j];
    }
    cout << "] ";

}
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<int> A(n);
        for (auto &x : A) cin >> x;
        print(1, A, n);
        if (n > 1) {
            cout << '[' << A[0];
            for (int j = 1; j < n; j++) {
                cout << " " << A[j];
            }
            cout << "] ";
        }
        cout << endl;
    }
}