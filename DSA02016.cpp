#include <iostream>
#include <cstring>
using namespace std;

int t, n, count;
bool main_diagonal[100];
bool secondary_diagonal[100];
bool column[100];

void Try (int j) {
    if (j == n) {
        count ++;
    }
    for (int i = 0; i < n; i++) {
        if (!main_diagonal[n - i + j -] and !secondary_diagonal[i + j] and !column[i]) {
            main_diagonal[n - i + j - 1] = secondary_diagonal[i + j] = column[i] = true;
            Try(j + 1);
            main_diagonal[n - i + j - 1] = secondary_diagonal[i + j] = column[i] = false;
        }
    }
}
int main() {
    cin >> t;
    while (t --) {
        cin >> n;
        count = 0;
        memset(main_diagonal, 0, sizeof(main_diagonal));
        memset(secondary_diagonal, 0, sizeof(secondary_diagonal));
        memset(column, 0, sizeof(column));

        Try (0);
        cout << count << endl;
    }
}