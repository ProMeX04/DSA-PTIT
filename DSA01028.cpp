#include<iostream>
#include<set>
using namespace std;

int n, k; 
int B[100];

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


int main(){   
    int n, k;
    cin >> n >> k;
    set<int> se;
    for(int i = 0; i < n ; i++) {
        int x; cin >> x;
        se.insert(x);
    }
    n = se.size();
    int i = 0;
    int A[k + 1];
    for(auto x: se) {B[i++] = x;}
    for(int i = 1; i <= k; i++) A[i] = i;
    ok = true;
    while(ok) {

        for(int i = 1; i <= k; i++) {
            cout << B[A[i] - 1] << " ";
        }
        cout <<endl;
        nextCombination(A, n, k);
    }



}