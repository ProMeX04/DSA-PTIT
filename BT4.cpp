#include <iostream>
#include <stack>
using namespace std;
int main () {
    int n, q;cin >> n>> q;
    int a[n + 1];
    for (int i = 1; i <= n; i++) cin >> a[i];
    int r[n  + 5];
    stack<int> st;
    for (int i = n; i >= 1; i --) {
        while(not st.empty() and a[i] >= st.top()) {
            st.pop();
        }
        if (st.empty()){
            r[i] = 0;
        }
        else{
            r[i] = st.size();
        }
        st.push(a[i]);
    }

    for(int i = 0; i < q; i++) {
        int x; cin >> x;
        cout << r[x] << endl;
    }
}