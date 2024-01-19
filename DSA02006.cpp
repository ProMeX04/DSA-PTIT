#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;


int n, k;
int A[1000];
bool found = false;

void findSet (int sum, int min, vector<int> result) {
    if (sum == k) {
        found = true;
        cout << '[' << result[0];
        for (int i = 1; i < result.size(); i ++) {
            cout << " " << result [i];
        }
        cout << "]";
    }
    else
        for (int i = min; i < n; i++) {
            if (sum + A[i] <= k) {
                result.push_back(A[i]);
                findSet(sum + A[i], i + 1, result);
                result.pop_back();
            }
        }
}
int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n >> k;
        found = false;
        for (int i = 0; i < n; i++) cin >> A[i];
        sort (A, A + n);
        findSet(0, 0, vector<int>(0));
        if (not found) {cout << -1;}
        cout << endl;
    }
}