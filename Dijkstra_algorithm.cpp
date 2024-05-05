#include <iostream>
#include <vector>
#include <queue>
using namespace std;

int n, b;
const int INF = 1000000000;
vector<pair<int, int>> adj[100];
vector <int> cost;

void print(priority_queue<pair<int, int>, vector <pair<int, int>>, greater<pair<int, int>>> q) {
    while (not q.empty()) {
        pair<int,int> t = q.top();
        cout << "{" << t.first << " " << t.second << "}" <<" ";
        q.pop();
    }
    cout << endl;
}

void init() {
    cin >> n >> b;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int k; cin >> k;
            if (k) {
                adj[i].push_back({j, k});
            }
        }
    }
}

void dijkstra () {
    cost.resize(n + 1, INF);
    vector <bool> visited(100, false);
    priority_queue<pair<int, int>, vector <pair<int, int>>, greater<pair<int, int>>> q;
    vector <int> parrent(n + 1);
    cost[b] = 0;

    parrent[b] = b;
    q.push({cost[b], b});

    while (not q.empty()) {
        int top = q.top().second;
        q.pop();
        print(q);
        if (visited[top]) continue;
        visited[top] = true;
        for (auto x : adj[top]) {
            if (x.second + cost[top] < cost[x.first]) {
                parrent[x.first] = top;
                cost[x.first] = x.second + cost[top];
                q.push({cost[x.first], x.first});
            }
        }
    }
    for (auto x : cost) {
        cout << x << " ";
    }
    cout << endl;
    for (auto x : parrent) {
        cout << x << " ";
    }
}
int main () {
    init();
    dijkstra();
}
