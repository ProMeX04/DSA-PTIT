#include <iostream>
#include <queue>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n;cin >> n;
        priority_queue<int, vector<int>, greater<int>> A;

        for (int i = 0; i < n ; i++) {
            int x; cin >> x;
            A.push(x);
        }
        long long count = 0;
        while (A.size() > 1) {
            int h1 = A.top();
            A.pop();
            int h2 = A.top();
            A.pop();
            count += h1 + h2;
            A.push(h1 + h2);
        }
        cout << count << endl;



    }
}