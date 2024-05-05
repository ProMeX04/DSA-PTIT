#include <iostream>
#include <vector>
#include <stack>
using namespace std;

int n, b;
vector<int> adj[1000];
vector<bool> visited(1000, 0);

void print(stack<int> st) {
    if (not st.empty()) {
        int top = st.top();
        st.pop();
        print(st);
        cout << top << " ";
    }
}
void hamilton_cycle(int j, stack<int> &st, int u) {
    if (j == n + 1 and u == b) {
        print(st);
        cout << endl;
    }

    else if (j == 1 or u != b){
        bool ok = false;
        for (auto x : adj[u]) {
            if (not visited[x]) {
                visited[x] = true;
                st.push(x);
                hamilton_cycle(j + 1, st, x);
                visited[x] = false;
                st.pop();
                ok = true;
            }
        }
        // if (not ok){
        //     print(st);
        //     cout << endl;
        // }
    }
}

void Hamilton(vector<vector<int>> a) {
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            if (a[i][j] == 1) {
                adj[i].push_back(j);
            }
        }
    }
    stack<int> st;
    st.push(b);

    hamilton_cycle(1, st, b);
}
int main () {
    cin >> n >> b;
    vector<vector<int>> a(n + 1, vector<int>(n + 1));
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            cin >> a[i][j];
        }
    }
    Hamilton(a);
}