#include <iostream>
#include <vector>
using namespace std;

class DisjointSet {
private:
    vector<int> parent, rank;
public:
    DisjointSet(int n) : parent(n + 1), rank(n + 1, 0) {
        for (int i = 0; i <= n; ++i)
            parent[i] = i;
    }

    int find(int u) {
        if (u != parent[u])
            parent[u] = find(parent[u]);
        return parent[u];
    }

    void unionSet(int u, int v) {
        int x = find(u);
        int y = find(v);

        if (x == y) return;

        if (rank[x] < rank[y]) {
            parent[x] = y;
        } else if (rank[x] > rank[y]) {
            parent[y] = x;
        } else {
            parent[x] = y;
            rank[y]++;
        }
    }
};

bool hasCycle(int v, vector<pair<int, int>>& edges) {
    DisjointSet djs(v);
    for (auto& edge : edges) {
        if (djs.find(edge.first) != djs.find(edge.second)) {
            djs.unionSet(edge.first, edge.second);
        } else {
            return true;
        }
    }
    return false;
}

int main() {
    int T, v, e, a, b;
    cin >> T;
    while (T--) {
        cin >> v >> e;
        vector<pair<int, int>> edges;
        for (int i = 0; i < e; ++i) {
            cin >> a >> b;
            edges.push_back({a, b});
        }
        cout << (hasCycle(v, edges) ? "YES" : "NO") << endl;
    }
    return 0;
}
