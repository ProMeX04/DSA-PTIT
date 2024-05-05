#include <iostream>
#include <stack>
#include <vector>
using namespace std;

int a[101][101];
int n;

void print(stack<int> st){
    if (st.empty()) {
        return;
    }
    int top = st.top();
    st.pop();
    if (not st.empty()){
        print (st);
    }
    cout << top << " ";
}

void dfs (int u) {
    vector<int> adj[n + 1];
    for (int i = 1; i <= n ; i++) {
        for (int j = 1; j <= n; j ++) {
            if (a[i][j] == 1) {
                adj[i].push_back(j);
            }
        }
    }

    stack<int> st;
    st.push(u);
    bool visited[101] = {0};
    visited[u] = true;
    while (not st.empty()) {
        int top = st.top();
        st.pop();
        for (auto i : adj[top]) {
            if (not visited[i]) {
                visited[i] = true;
                st.push(top);
                st.push(i);
                break;
            }
        }
        print(st);
        cout << endl;
    }
}
int main() {
    cin >> n;
    for (int i = 1; i <= n ; i++) {
        for (int j = 1; j <= n; j ++) {
            // int k; cin >> k;
            // a[i][j] = a[i][j] or k;
            // if (k == 1){
            //     a[j][i] = 1;
            // }
            cin >> a[i][j];
        }
    }
    int u; cin >> u;
    dfs(u);

}