#include<iostream>
#include <algorithm>

using namespace std;
int main(){   
    int n; cin >> n;
    int A[n];
    for(auto &x : A) cin >> x;

    int B[n];
    for(int i = 0; i < n ; i ++) B[i] = i + 1;
    auto gt = [](int n) {
        int gt = 1;
        for(int i = 2; i <= n ; i++) {
            gt *= i;
        }
        return gt;
    };
    sort(A, A + n);
    int times = gt(n);
    while(times --) {
        for(int i = 0; i < n ; i++) {
            cout << A[B[i] - 1] << " ";
        }
        cout << endl;
        next_permutation(B , B + n);
    }

}