#include <iostream>
#include <set>
using namespace std;

int B[1000];
int n, k;
void Try(int j, int min) {
    if (j == k) {
        for (int i = 0; i < k; i++) {
            cout << char ('A' + B[i]) ;
        }
        cout << endl;
    }

    else {
        for (int i = min; i <= n - k + j; i++) {
            B[j] = i;
            Try(j + 1, i + 1);
        }
    }
}
int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n >> k;
        Try(0, 0);
    }
}