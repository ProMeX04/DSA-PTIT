#include <iostream>
#include <cmath>
using namespace std;


char Try (long long j, long long k, int u) { 
    if (k == j) return 'A' + u;
    
    if (k > j) return Try(j / 2, k - j, u - 1);
    else return Try(j / 2, k, u - 1);
}

int main(){   
    int t; cin >> t;
    while (t--) {
        long long n, m; cin >> n >> m;
        long long x = pow(2, n);
        cout << Try (x, m, n) << endl;
    }
}