#include <iostream>
#include <queue>
#include <vector>
#include <algorithm>
using namespace std;

void test() {
    int n; cin >> n;
    vector<pair<int,int>> ls(n);
    for (int i = 0; i < n ; i++) {
        cin >> ls[i].first >> ls[i].first >> ls[i].second;
    }
    sort(ls.begin(), ls.end(),greater<pair<int, int>>());
    priority_queue<int> q;
    long long result = 0;
    int cv = 0;
    int deadline = ls[0].first;
    int i = 0;
    while (deadline > 0) {
        while (ls[i].first == deadline and i < n) q.push(ls[i++].second);
        deadline--;
        if (!q.empty()) {
            cv ++;
            result += q.top();
            q.pop();
        }
    }
    cout <<cv << " " << result << endl;
}

int main() {
    int t; cin >> t;
    while (t--) {
        test();
    }
}
