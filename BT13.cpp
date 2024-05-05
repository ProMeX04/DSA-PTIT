#include <iostream>
#include <map>
#include <vector>
using namespace std;

map<string, int> studentMap;
vector<int> adj[1000000] ;
bool hasCycle = false;
vector<int> visited(1000000, 0);

void dfs(int v){
    visited[v] = 1;
    for (int u: adj[v]) {
        if (visited[u] == 1) {
            hasCycle = true;
            return;
        }
        else if (visited[u] == 0) {
            dfs(u);
            if (hasCycle) return;
        }
    }
    visited[v] = 2;
} 

int main () {
    int N; cin >> N;
    int index = 0;

    for (int i = 0; i < N; i++) {
        string name1, name2, cmp;
        cin >> name1 >> cmp >> name2;

        if (studentMap.count(name1) == 0) studentMap[name1] = index ++;
        if (studentMap.count(name2) == 0) studentMap[name2] = index ++;

        int id1 = studentMap[name1];
        int id2 = studentMap[name2];

        if (cmp == ">") {
            adj[id1].push_back(id2);
        }
        else {
            adj[id2].push_back(id1);
        }
    }
    for (int i = 0; i < index and not hasCycle; i++) {
        if (visited[i] == 0) {
            dfs(i);
        }
    }
    cout << (hasCycle ? "impossible" : "possible") << endl;
}
