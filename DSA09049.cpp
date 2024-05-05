#include <iostream>
#include <vector>
using namespace std;
long long n;
vector<pair<long long, long long>> value;
vector<vector<int>> adj;
pair <long long, long long> transfer(int root) {
    for (auto branch: adj[root]) {
        value[branch] = transfer(branch);
        value[root].first += value[branch].first + value[branch].second;
        value[root].second += value[branch].second;
    }
    return value[root];
}
int main() {
    cin >> n;
    adj.resize(n + 1, vector<int> ());
    value.resize(n + 1, {1,1});
    for (int i = 2; i <= n; i++) {
        int x; cin >> x;
        adj[x].push_back(i);
    }
    transfer(1);    
    for (int i = 1; i <= n; i ++){
        cout << value[i].first << " ";
    }
}