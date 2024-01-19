#include <iostream>
#include <climits>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int n; cin >> n;
        long long sum = 0;
        long long result = INT_MIN;
        for (int i = 0; i < n; i++) {
            int x; cin >> x;
            sum += x;
            result = max (sum, result);
            if (sum < 0) sum = 0;
        }
        cout << result << endl;
    }   
}