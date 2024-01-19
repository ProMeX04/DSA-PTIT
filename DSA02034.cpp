#include <iostream>
using namespace std;
int A[100];
int n;
bool visited[100];
void Try (int j, int prev) {
    if (j == n + 1) {
        for (int i = 1; i <= n ; i++) {
            cout << A[i];
        }
        cout << endl;
    }
    else
        for (int i = 1; i <= n; i ++) {
            if (!visited[i] and abs(i - prev) > 1) {
                visited[i] = true;
                A[j] = i;
                Try(j + 1, i);
                visited[i] = false;
            }
        }
}
int main() {
    int t; cin >> t;
    while (t--) {
        cin >> n;
        Try(1, -1);
    }
}