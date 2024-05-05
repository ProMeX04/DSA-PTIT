#include <iostream>
#include <vector>
#include <map>
#include <deque>

using namespace std;

bool function() {
    int v, e;
    cin >> v >> e;
    vector<int> ls;
    int temp;
    for (int i = 0; i < 2 * e; ++i) {
        cin >> temp;
        ls.push_back(temp);
    }

    map<int, vector<int>> adj;
    for (int i = 0; i < 2 * e; i += 2) {
        adj[ls[i]].push_back(ls[i + 1]);
    }

    map<int, bool> visited;
    map<int, int> parent;
    deque<int> stack;

    auto dfs = [&](int bVertex){
        stack.push_back(bVertex);
        bool has_cycle = false;

        while (!stack.empty()) {
            int u = stack.back();
            stack.pop_back();
            if (!visited[u]) {
                visited[u] = true;
                for (int x : adj[u]) {
                    if (!visited[x]) {
                        stack.push_back(x);
                        parent[x] = u;
                        break;
                    } else if (parent[u] != x) {
                        has_cycle = true;
                        break;
                    }
                }
            }
            if (has_cycle) break;
        }
        return has_cycle;
    };

    for (int i = 1; i <= v; ++i) {
        if (!visited[i]) {
            if (dfs(i)) {
                return true;
            }
        }
    }
    return false;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        cout << (function() ? "YES" : "NO") << endl;
    }
    return 0;
}
