#include <iostream>
#include <climits>
#include <algorithm>
#include <cstring>

using namespace std;
int A[1000][1000];
bool visited[1000];
int n;
int MAX = 0;

void Try(int j, int sum) {
    if (j == n) {
        MAX = max(MAX, sum);
    }

    else {
        for (int i = 0; i < n; i ++) {
            if (!visited[i]) {
                visited[i] = true;
                Try(j + 1, sum + A[j][i]);
                visited[i] = false;
            }
        }
    }
}

int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n;;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                cin >> A[i][j];
            }   
        }
        memset(visited, sizeof(int), 0);
        MAX = INT_MIN;

        Try(0, 0);
        cout << MAX << endl;
    }
}