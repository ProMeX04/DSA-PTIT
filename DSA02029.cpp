#include <iostream>
using namespace std;
int n;

void tower (int n, char source, char des, char intermediate) {
    if (n == 1) {
        cout << source << " -> " << des << endl;
    }
    else {
        tower (n - 1, source, intermediate, des);
        cout << source << " -> " << des << endl;
        tower (n - 1, intermediate, des, source);
    }
}
int main() {
    cin >> n;
    tower (n, 'A', 'C', 'B');
}