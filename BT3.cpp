#include <iostream>
#include <stack>
using namespace std;


long long calc (long long A[], long long n){
    long long result = 0;
    stack<pair<long long, long long>> st;
    st.push({A[0], 0});
    for (long long i = 1; i <= n; i++) {
        long long k = i;
        while (not st.empty() and st.top().first >= A[i]){
            auto [val, pos] = st.top(); st.pop();
            result = max(result, val * (i - pos));
            k = pos;
        }
        st.push({A[i], k});
    }
    return result;
}


int main(){   
    long long m, n; cin >> m >> n;
    long long A[n + 1];
    A[n] = 0;
    for (long long i = 0; i < n; i ++) cin >> A[i];
    long long result = calc(A, n);
    
    for (long long i = 0; i < n; i++) A[i] = m - A[i];
    result = max(result, calc(A, n));
    cout << result;

}