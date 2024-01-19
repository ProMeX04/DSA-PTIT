#include <iostream>
#include <set>
using namespace std;

string A[1000];
int n, k;
string B[1000];

void Try(int j, int min) {
    if (j == k) {
        for (int i = 0; i < k; i++) {
            cout << B[i] << " ";
        }
        cout << endl;
    }

    else {
        for(int i = min; i <= n - k + j; i++) {
            B[j] = A[i];
            Try(j + 1, i + 1); 
        }
    }
}
int main() {
    cin >> n >> k;
    set<string> se;
    for(int i = 0; i < n; i++) cin >> A[i];
    for(int i = 0; i < n; i++) se.insert(A[i]);
    n = se.size();
    int i = 0;
    for(auto x : se) {A[i ++] = x;}
    Try(0,0);
}