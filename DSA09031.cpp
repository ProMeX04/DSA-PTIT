#include <iostream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;


long long n, k, m;
vector<vector<long long>> matrix(200, vector<long long>(200, 0));

bool check(long long i, long long j) {
    return i >= 0 && j >= 0 && i < 2 * n - 1 && j < 2 * n - 1;
}

void move(long long i, long long j, long long& cnt) {
    static const long long dx[] = {0, 0, -2, 2};
    static const long long dy[] = {2, -2, 0, 0};

    matrix[i][j] = -1;
    for (long long k = 0; k < 4; ++k) {
        long long iNew = i + dx[k];
        long long jNew = j + dy[k];
        if (check(iNew, jNew) && matrix[(i + iNew) / 2][(j + jNew) / 2] == 0) {
            if (matrix[iNew][jNew] == 2) {
                cnt++;
            }
            if (matrix[iNew][jNew] >= 0) {
                move(iNew, jNew, cnt);
            }
        }
    }
}

int main() {
    cin >> n >> k >> m;
    for (long long i = 0; i < m; ++i) {
        long long u, v, x, y;
        cin >> u >> v >> x >> y;
        u = 2 * (u - 1);
        v = 2 * (v - 1);
        x = 2 * (x - 1);
        y = 2 * (y - 1);
        if (u == x) {
            matrix[u][(v + y) / 2] = 1;
        } else {
            matrix[(u + x) / 2][y] = 1;
        }
    }

    for (long long i = 0; i < k; ++i) {
        long long u, v;
        cin >> u >> v;
        u = 2 * (u - 1);
        v = 2 * (v - 1);
        matrix[u][v] = 2;
    }

    vector<long long> ls;
    long long cnt = 1;

    for (long long i = 0; i < 2 * n - 1; i += 2) {
        for (long long j = 0; j < 2 * n - 1; j += 2) {
            if (matrix[i][j] == 2) {
                move(i, j, cnt);
                ls.push_back(cnt);
                cnt = 1;
            }
        }
    }

    long long res = 0;
    for (auto i = 0; i < ls.size(); ++i) {
        for (auto j = i + 1; j < ls.size(); ++j) {
            res += ls[i] * ls[j];
        }
    }


    cout << res << endl;

    return 0;
}
