#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

void function() {
    int n; cin >> n;
    vector<pair<int, int>> new_ls;
    int input;
    for (int i = 0; i < n; ++i) {
        cin >> input;
        new_ls.push_back(make_pair(input, i + 1));
    }

    sort(new_ls.begin(), new_ls.end());

    vector<int> res;
    int MAX = 0;
    for (int i = 0; i < n; ++i) {
        MAX = max(MAX, new_ls[i].second);
        if (i + 1 >= MAX) {
            res.push_back(MAX);
        }
    }

    cout << res.size() - 1 << endl;
    for (int i = 0; i < res.size() - 1; ++i) {
        cout << res[i] << " ";
    }
    cout << endl;
}

int main() {
    ios_base::sync_with_stdio(false);cin.tie(0);
    int t;
    cin >> t;
    while (t--) {
        function();
    }
    return 0;
}
