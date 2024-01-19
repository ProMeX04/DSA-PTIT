#include<iostream>
#include<set>
using namespace std;
bool ok = true;
void nextCombination (int A[] , int n, int k) {
    int i = k;
    while (A[i] == n - k + i) {
        i --;
    }
    if (i == 0) {
        ok = false;
    }
    else {
        A[i] ++;
        for (int j = i + 1; j <= k; j++) {
            A[j] = A[j - 1] + 1;
        }
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int A[k + 1] = {0};
        set<int> se;
        for (int i = 1; i <= k; i++) {
            cin >> A[i];
            se.insert(A[i]);
        }

        ok = true;
        nextCombination (A, n, k);
        for (int i = 1; i <= k; i++) {
            se.insert(A[i]);
        }
        if(ok) cout << se.size() - k << endl;
        else cout << k << endl;
    }
}