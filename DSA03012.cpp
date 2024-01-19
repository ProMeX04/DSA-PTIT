#include <iostream>
#include <map>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t --) {
        string s; cin >> s;
        map <char, int> mp;
        int MAX = 0;
        for (auto x : s) {
            mp[x] ++;
            MAX = max (MAX, mp[x]);
        }
        if (MAX > (s.length() + 1) / 2) cout << -1;
        else cout << 1;
        cout << endl;
    }
}