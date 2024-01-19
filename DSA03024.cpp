#include <iostream>
#include <algorithm>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t --) {
        int n; cin >> n;
        pair<int,int> A[n];
        for (auto &x : A) cin >> x.first >> x.second;

        sort (A, A + n, [](pair<int, int> a, pair<int, int> b) {
            return a.second < b.second;
        });

        int startTime = 0;
        int count = 0;
        for (int i = 0; i < n; i++) {
            if (startTime <= A[i].first) {
                startTime = A[i].second;
                count ++;
            }
        }
        cout << count << endl;
    }
}