#include <bits/stdc++.h>
using namespace std;

int n, m, dem;
vector<int> ke[1005];
int visited[1005], e[1005];

void dfs(int u) {
    visited[u] = 1;
    for (auto v : ke[u]) {
        if (!visited[v]) {
            dfs(v);
            e[v] = u;
        }
    }
}

void bfs(int u) {
    queue<int> q;
    q.push(u);
    visited[u] = 1;
    while (!q.empty()) {
        int u = q.front();
        q.pop();
        for (auto v : ke[u]) {
            if (not visited[v]) {
                q.push(v);
                e[v] = u;
                visited[v] = 1;
            }
        }
    }
}


void roaddfs(int s, int t) {
    memset(visited, 0, sizeof(visited));
    dfs(s);
    if (not visited[t]) cout << -1;
    else {
        vector<int> res;
        while (t != s) {
            res.push_back(t);
            t = e[t];

        }
        res.push_back(s);
        reverse(res.begin(), res.end());
        for (auto x : res) cout << x << " ";
    }
}

void roadbfs(int s, int t) {
    memset(visited, 0, sizeof(visited));
    bfs(s);
    if (not visited[t]) cout << -1;
    else {
        vector<int>res;
        while (t != s) {
            res.push_back(t);
            t = e[t];
        }
        res.push_back(s);
        reverse(res.begin(), res.end());
        for (auto x : res) cout << x << ' ';
    }
}
int main () {
    int n, m; cin >> n >> m;
    for (int i = 1; i <= m ; i++ ) {
        int x, y; cin >> x >> y;
        ke[x].push_back(y);
        ke[y].push_back(x);
    }
    for (int i = 2; i <= n; i++) {
        roaddfs(1, i);
        cout << endl;
        roadbfs(i, 1);
        cout << endl;
    }
    cout << endl;
}