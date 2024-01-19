#include<iostream>
#include<vector>
using namespace std;

void Try(int i, int j, int n, vector<vector<int>> A, string way, bool& found) {
    if (i + 1 < n and A[i + 1][j]) {
        Try(i + 1, j, n, A, way + "D", found);
    }
    if (j + 1 < n and A[i][j + 1]) {
        Try(i, j + 1, n, A, way + "R", found);
    }
    if (i == n - 1 and j == n - 1) {
        cout << way << " ";
        found = true;
    }
}
int main() {
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        vector<vector<int>> A(n, vector<int>(n));
        bool found = false;
        for (auto &x : A) {
            for (auto &y : x) {
                cin >> y;
            }
        }
        if (A[0][0]) Try(0, 0, n, A, "", found);
        if (not found) cout << -1;
        cout << endl;

    }
}