#include <iostream>
#include <stack>
#include <vector>
#include <algorithm>
using namespace std;
int v, e, b;
vector <int> adj[100];

void init() {
    cin >> v >> e >> b;
    for (int i = 1; i <= v; i ++) {
        for (int j = 1; j <= v; j ++) {
            int k; cin >> k;
            if (k == 1) {
                adj[i].push_back(j);
            }

        }
    }
}

void print(stack<int> st) {
    if (not st.empty()) {
        int s = st.top();
        st.pop();
        print(st);
        cout << s << " ";
    }

}

void cycle_euler() {
    stack <int> st;
    vector <int> CE;
    st.push(b);
    vector <vector <bool>> visited(100, vector<bool> (100, false));
    while (not st.empty()) {
        int s = st.top();
        bool ok = false;
        // print(st);
        // cout << endl << "{CE}";
        for (auto x : CE) {
            cout << x << " ";
        }
        cout << endl;
        for (auto t : adj[s]) {
            if (not visited[s][t]) {
                visited[s][t] = true;
                // visited[t][s] = true;
                st.push(t);
                ok = true;
                break;
            }
        }
        if (not ok) {
            st.pop();
            CE.push_back(s);
        }
        
        
    }
    cout << "{RESULT}";
    reverse(CE.begin(),CE.end());
    for (auto x : CE) {
        cout << x << " ";
    }
}
int main() {
    init();
    cycle_euler();
}