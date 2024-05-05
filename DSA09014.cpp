#include <iostream>
#include <unordered_map>
#include <vector>
using namespace std;

void check_cycle(unordered_map<int, vector<int>> adj, unordered_map<int, bool>& visited, int u, bool& found, int parent) {
    visited[u] = true;
    for (auto x : adj[u]) {
        if (not visited[x]) {
            check_cycle(adj, visited, x, found, u);
        }
        else if (x != parent){
            found = true;
        }
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        unordered_map<int, vector<int>> adj;
        int v, e; cin >> v >> e;
        for (int i = 0; i < e; i++) {
            int u, v; cin >> u >> v;
            adj[u].push_back(v);
            adj[v].push_back(u);
        }
        bool found = false;
        unordered_map<int, bool> visited;
        for (auto x : adj) {
            if (not visited[x.first]) {
                check_cycle(adj, visited, x.first, found, -1);
                if (found) break;
            }
        }

        if (found) {
            cout << "YES\n";
        }
        else cout << "NO\n";
    }
}