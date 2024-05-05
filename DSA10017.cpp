#include <iostream>
#include <vector>
#include <limits>

using namespace std;

int function() {
    int V, E;
    cin >> V >> E;
    vector<vector<int>> edge_list(E, vector<int>(3));

    for (int i = 0; i < E; ++i) {
        cin >> edge_list[i][0] >> edge_list[i][1] >> edge_list[i][2];
    }

    vector<long long> d(V + 1, 1e9);
    d[1] = 0;

    for (int k = 0; k < V; ++k) {
        for (const auto& edge : edge_list) {
            int u = edge[0], v = edge[1], w = edge[2];
            if (d[u] != 1e9 && d[u] + w < d[v]) {
                d[v] = d[u] + w;
            }
        }
    }

    for (const auto& edge : edge_list) {
        int u = edge[0], v = edge[1], w = edge[2];
        if (d[u] != 1e9 && d[u] + w < d[v]) {
            return 1;
        }
    }
    return 0;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << function() << endl;
    }
    return 0;
}
