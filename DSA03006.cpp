#include <iostream>
#include <algorithm>
using namespace std;


bool check (int A[], int n, int sortedArray[]) {
    int i = 0, j = n - 1;
    while (j > i) {
        if ((A[i] != sortedArray[i] or A[j] != sortedArray[j]) and (A[i] != sortedArray[j] or A[j] != sortedArray[i])) {
            return false;
        }
        i ++;
        j --;
    }
    return true;
}
int main() {
    int t; cin >> t;
    while (t-- ) {
        int n; cin >> n;
        int A[n], B[n];
        int i = 0;
        for (auto& x : A) { cin >> x; B[i ++] = x;}

        sort (B, B + n);
        cout << (check (A, n, B) ?"Yes\n" : "No\n");


    }
}