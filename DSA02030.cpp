#include <iostream>
using namespace std;
char x;
int n;
void Try(int j, char min, string res) {
    if (j == n) {
        cout << res << endl;
    }
    else 
    for (char i = min; i <= x; i ++) {
        Try (j + 1, i, res + i);
    }
}

int main(){   
    cin >> x >> n;
    Try (0, 'A' , "");
}