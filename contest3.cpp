#include<iostream>
#include<queue>
using namespace std;


int a[100][100];
int n;

void print(queue<int> q){
    while (not q.empty()) {
        cout << q.front() << " ";
        q.pop();
    }
}

void bfs(int u) {

    vector<int> adj[1000];
    for (int i = 1; i <= n ; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i][j]) {
                adj[i].push_back(j);
            }
        }
    }
    bool visited[1000] = {0};
    queue<int> q;
    q.push(u);
    visited[u] = 1;

    while (not q.empty()) {
        int u = q.front();
        q.pop();
        for (auto i : adj[u]) {
            if (not visited[i]) {
                visited[i] = true;
                q.push(i);
            }
        }
        print (q);
        cout << endl;
    }
}
int main() {
    cin >> n;
    for (int i = 1; i <= n ; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }
    int u; cin >> u;

    bfs(u);

}