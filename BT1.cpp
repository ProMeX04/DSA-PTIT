#include <iostream>
#include <stack>
using namespace std;
int main(){   
    int t; cin >> t; 
    while (t--) {
        string s; cin >> s;
        stack<int> st;
        for (int i = 0; i < s.size(); i++) {
            if (s[i] == '(') {
                st.push(i);
            }
            else if (s[i] == ')'){
                if(!st.empty()) {
                    s[st.top()] = '0';
                    s[i] = '1';
                    st.pop();
                }
            }

        }
         for(int i = 0 ; i< s.size(); i ++) {
        if (s[i] == '(' or s[i] == ')') cout << "-1";
        else cout << s[i];
    }
    cout << endl;
    }
   
}