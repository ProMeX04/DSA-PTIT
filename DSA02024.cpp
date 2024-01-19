#include <iostream>
#include <vector>
#include <set>
using namespace std;

int n;
vector<int> A;
set<string> se;
void push (const vector<int> &B) {
    string res = "";
    for (auto x : B ) {
        res += to_string(x) + " ";
    }
    se.insert(res);
}

void generate(int j, vector <int> B, int min, int prev) {
    if (j > 1) {
        push (B);
    }
    for (int i = min; i < n; i++) {
        if (A[i] > prev) {
            B.push_back(A[i]);
            generate (j + 1, B, i + 1, A[i]);
            B.pop_back();
        }
    }
}
int main() {
    cin >> n;
    for (int i = 0; i < n ; i ++) {
        int x; cin >> x;
        A.push_back(x);
    }
    generate(0, vector<int> (0), 0, 0);
    for (auto x : se) cout << x << endl;


}