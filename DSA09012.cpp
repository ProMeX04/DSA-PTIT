#include <iostream>
#include <vector>
#include <unordered_map>
#include <set>
using namespace std;

void tarjan(int u, unordered_map<int, vector<int>>& adj, unordered_map<int, int>& low,
            unordered_map<int, int>& num, unordered_map<int, int>& par, set<int>& articulation_points, int& time) {
    low[u] = num[u] = time;
    time++;
    int child = 0;
    for (int v : adj[u]) {
        if (num[v] == 0) {
            par[v] = u;
            tarjan(v, adj, low, num, par, articulation_points, time);
            child++;
            low[u] = min(low[u], low[v]);
            if (par[u] == 0 && child > 1) {
                articulation_points.insert(u);
            }
            if (par[u] != 0 && low[v] >= num[u]) {
                articulation_points.insert(u);
            }
        } else {
            low[u] = min(low[u], num[v]);
        }
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int v, e;
        cin >> v >> e;

        vector<int> ls;
        while (ls.size() < 2 * e) {
            int x, y;
            cin >> x >> y;
            ls.push_back(x);
            ls.push_back(y);
        }

        unordered_map<int, vector<int>> adj;
        for (int i = 0; i < e; ++i) {
            adj[ls[2 * i]].push_back(ls[2 * i + 1]);
            adj[ls[2 * i + 1]].push_back(ls[2 * i]);
        }

        unordered_map<int, int> low, num, par;
        int time = 1;
        set<int> articulation_points;

        for (auto i : adj) {
            if (par[i.first] == 0) {
                tarjan(i.first, adj, low, num, par, articulation_points, time);
            }
        }

        for (int point : articulation_points) {
            cout << point << " ";
        }
        cout << endl;
    }
    return 0;
}
