#include<iostream>
using namespace std;

bool ok = true;
void nextBinary(int n, int A[]) {
    int i = n;
    while (i >= 0 and A[i] == 1) {A[i] = 0; i --;}
    if (i < 0) ok = false;
    else {
        A[i] = 1;
    }
}
int main() {
    int n; cin >> n;
    int k = (n + 1) / 2;
    int A[k] = {0};
    while(ok){
        for(auto x: A) cout << x << " ";
        for(int i = k - ( n % 2 == 1) - 1; i >= 0; i--){
            cout << A[i] << " ";
        }

        nextBinary(k - 1, A);
        cout << endl;
    }

}