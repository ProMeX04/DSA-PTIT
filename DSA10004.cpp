#include <iostream>
#include <map>
using namespace std;
int main () {
    int t; cin >> t;
    while (t--) {
        int v, e; cin >> v >> e;
        map <int, int> mp;
        for (int i = 0; i < e; i++) {
            int u, v; cin >> u>> v;
            mp[u]++;
            mp[v]++;
        }
        int odds = 0;
        for (auto x: mp){
            if (x.second % 2 == 1) {
                odds ++;
            }
        }
        if (odds == 2) cout << 1;
        else if (odds == 0) cout << 2;
        else cout << 0;
        cout << endl;       

    }
}