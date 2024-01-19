#include <iostream>
#include <map>
#include <vector>
using namespace std;
int ok;
bool visited[10000];
vector <int> A;
int array_total[10000];
int D; string s;
int sz;

vector<int> arr(string s, int n) {
    map <char, int > mp;
    for (auto x : s) {
        mp[x] ++;
    }
    vector <int> A;
    for (auto x : mp) {
        A.push_back(x.second);
        if (x.second != 1) {
            ok = -1;
        }

    }
    return A;
}

void Try (int j, int min, int sum) {
    if (j == D) {
        ok = 1;
        return;
    }
    if (ok == -1) {
        for (int i = min; i < sz; i++) {
            if (not visited[i]) {
                if (sum + A[i] < array_total[j]) {
                    visited[i] = true;
                    Try (j, i + 1, sum + A[i]);
                    visited[j] = false;
                }
                if (sum + A[i] == array_total[j]) {
                    visited[i] = true;
                    Try(j + 1, 0, 0);
                    visited[i] = false;
                }
            }

        }
    }
}
int main() {
    ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
    int t; cin >> t;
    while (t-- ) {
        cin >> D >> s;
        int len = s.length();
        ok = 1;
        A = arr(s, D);
        int k = len % D;
        for (int i = 0; i < D; i++) {
            if (i < k) {
                array_total[i] = len / D + 1;
            }
            else {
                array_total[i] = len / D;
            }
        }
        sz = A.size();
        Try (0,0,0);
        cout << ok << endl;
    }
}