#include<iostream>
#include<cstring>
#include<vector>
using namespace std;
int n;
int cnt;
int A[1000];
bool visited[1000];
int result = 0;

bool check(vector<int> B) {
    for (int i = 0; i < n; i++) {
        if (A[i] != B[i]) return false;
    }
    return true;
}

void Try(int j, vector<int> B) {
    if (j == n) {
        cnt ++;
        if (check(B)) result = cnt;
    }
    else if (!result) {
        for (int i = 1 ; i <= n ; i++) {
            if (!visited[i]) {
                visited[i] = true;
                B.push_back(i);
                Try(j + 1, B);
                B.pop_back();
                visited[i] = false;
            }
        }
    }
}
int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n;
        cnt = result = 0;
        memset(visited, 0, sizeof(visited));
        for (int i = 0; i < n; i++) cin >> A[i];
        Try(0, vector<int>(0));
        cout << result << endl;
    }
}