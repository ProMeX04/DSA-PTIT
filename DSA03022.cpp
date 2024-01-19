#include <iostream>
#include <climits>
#include <algorithm>
using namespace std;
int main(){   
    int n; cin >> n;
    int A[n];
    for (auto &x: A) cin >> x;

    sort (A, A + n, greater<int> ());

    int result = INT_MIN;
    result = max ({A[0] * A[n - 1] * A[n - 2],
                   A[0] * A[1] * A[2],
                   A[n - 1] * A[n - 2],
                   A[0] * A[1]});
    cout << result;

}