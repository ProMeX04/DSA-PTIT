#include <iostream>
using namespace std;

char e;
bool visited [200];

bool check (string s) {
    for (int i = 1; i < s.length() - 1; i++ ){
        if (s[i] == 'A' or s[i] == 'E') {
            if (s[i - 1] != 'A' and s[i - 1] != 'E' and s[i + 1] != 'A' and s[i + 1] != 'E') return false;
        }
    }
    return true;
} 
void Try (int j, char s, string res) {
    if (j == e - 'A' + 1) {
        if (check (res))
            cout << res << endl;
    }
    else 
    for (char i = 'A'; i <= e; i ++ ) {
        if (!visited[i]) {
            visited [i] = true;
            Try (j + 1, s, res + i);
            visited [i] = false;
        }
    }
}
int main() {
    cin >> e;
    Try (0, 'A', "");


}