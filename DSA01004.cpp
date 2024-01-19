#include<iostream>
using namespace std;
bool ok = true;
void nextCombination (int A[] , int n, int k){
    int i = k;
    while(A[i] == n - k + i) {
         i --;
    }
    if (i == 0) {
        ok = false;
    }
    else {
        A[i] ++;
        for(int j = i + 1; j <= k; j++){
            A[j] = A[j - 1] + 1;
        }
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        int n, k; cin >> n >> k;
        int A[k + 1] = {0};

        for(int i = 1; i <= k; i++) {
            A[i] = i;
        }
        ok = true;
        while(ok) {
            for(int i = 1; i <= k; i++){
                cout << A[i] ;
            }
            cout << " ";
            nextCombination (A, n , k);
        }
        cout << endl;
    }
}