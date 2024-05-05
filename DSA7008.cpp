#include <iostream>
#include <stack>
#include <map>
using namespace std;

map<char, int> op;

int main () {
    op['+'] = 1;
    op['-'] = 1;
    op['*'] = 2;
    op['/'] = 2;
    op['^'] = 3;
    op['('] = -1;
    op[')'] = -1;
    int t; cin >> t;
    while (t--) {
        string s;
        cin >> s;
        stack<char> st;

        for (auto x : s) {
            if (x == '(') {
                st.push(x);
            }

            else if (x == ')') {
                while (st.top() != '(') {
                    cout << st.top();
                    st.pop();
                }
                if (st.top() == '(') st.pop();
            }

            else if (op.count(x)) {
                while (!st.empty() && op[x] <= op[st.top()]) {
                    char c = st.top();
                    st.pop();
                    cout << c;
                }
                st.push(x);
            }

            else {
                cout << x;
            }
        }
        while(not st.empty()) {
            cout << st.top();
            st.pop();
        }
        cout << endl;

    }
}