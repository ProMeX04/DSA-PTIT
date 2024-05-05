#include <iostream>
#include <vector>
#include <unordered_map>

using namespace std;
void hamilton(int l, int i, int v, unordered_map<int, vector<int>>& adj, vector<bool>& visited, bool& found) {
    if (l == v) {
        found = true;
    } else {
        for (int x : adj[i]) {
            if (!visited[x]) {
                visited[i] = true;
                hamilton(l + 1, x, v, adj, visited, found);
                visited[i] = false;
            }
        }
    }
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        int v, e;
        cin >> v >> e;
        unordered_map<int, vector<int>> adj;
        vector<bool> visited(v + 1, false);
        int a, b;
        for (int i = 0; i < e; ++i) {
            cin >> a >> b;
            adj[a].push_back(b);
            adj[b].push_back(a);
        }
        bool found = false;
        for (int i = 1; i <= v + 1; i++) {
            hamilton(1, i, v, adj, visited, found);
            if (found) break;
        }
        cout << found << endl;
    }
    return 0;
}
