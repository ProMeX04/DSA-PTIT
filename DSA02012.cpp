#include <iostream>
using namespace std;

int K_Combine (int n, int k) {
    if (k == n or k == 0) return 1;
    return (n - k + 1) * K_Combine(n, k - 1) / k;
}
int main(){   
    int t; cin >> t;
    while (t -- ){ 
        int n, m;
        cin >> n >> m;
        int x;
        for(int i = 0; i < n * m; i++) cin >> x;
        cout <<K_Combine(n + m - 2, n - 1) << endl;
    }
    
}