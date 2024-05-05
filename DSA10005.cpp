#include <iostream>
#include <map>
using namespace std;
int main () { 
    int t; cin >> t;
    while(t--) {
        int v, e; cin >> v >> e;
        map<int, int> degp;
        map<int, int> degm;

        for (int i = 0; i < e; i ++){
            int u, v; cin >> u >> v;
            degp[u] ++;
            degm[v] ++;
        }
        int cnt = 0;
        for (int i = 1; i < v; i++) {
            if (degp[i] != degm[i]) cnt ++;
        }
        cout << (cnt == 0? 1 : 0) << endl;
    }
}