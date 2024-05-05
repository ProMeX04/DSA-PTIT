#include <iostream>
#include <vector>

using namespace std;
vector<int> res;

void Try(int j, int n) {
    if (n == 0) {
        cout << "(";
        for (int k = 1; k < j; ++k) {
            cout << res[k];
            if (k < j - 1) {
                cout << " ";
            }
        }
        cout << ") ";
        return;
    }
    for (int i = min(res[j - 1], n); i > 0; --i) {
        res[j] = i;
        Try(j + 1, n - i);
    }
}

void function() {
    int n;
    cin >> n;
    res.resize(n + 1);
    res[0] = n;
    Try(1, n);
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        function();
    }
    return 0;
}
