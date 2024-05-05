#include <iostream>
#include <queue>
using namespace std;


struct edge {
    int b, e, w;

    bool operator<(const edge&another) const {
        return w > another.w;
    }

};



int n;
vector<vector<edge>> adj;
vector<bool> visited;

void init() {
    cin >> n;
    adj.resize(n + 1);
    visited.resize(n + 1, false);
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int k; cin >> k;
            if (k != 10000 and k != 0) {
                adj[i].push_back({i, j, k});
            }
        }
    }
}


void prim() {
    priority_queue<edge> q;
    q.push({0, 1, 0});
    int total_weight = 0;
    while (not q.empty()) {
        edge e = q.top();
        q.pop();
        if (visited[e.e]) continue;
        total_weight += e.w;
        visited[e.e] = true;
        for (edge next : adj[e.e]) {
            if (!visited[next.e]) {
                q.push(next);
            }
        }
    }
    cout << total_weight;
}
int main() {
    init();
    prim();
}   