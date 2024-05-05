#include <iostream>
#include <vector>
#include <stack>

using namespace std;

void function() {
    int n;cin >> n;
    vector<int> ls(n);
    for (auto& x : ls) cin >> x;
    ls.push_back(0);

    stack<pair<int, int>> st;
    int result = 0;
    for (int index = 0; index < n + 1; ++index) {
        int i = ls[index];
        int k = index;
        while (!st.empty() && st.top().first >= i) {
            auto [val, pos] = st.top();
            if (index - pos >= val)
                result = max(result, val);
            k = pos;
            st.pop();
        }
        st.push({i, k});
    }
    cout << result << endl;
}

int main() {
    int t;
    cin >> t;
    while (t--) {
        function();
    }
    return 0;
}
