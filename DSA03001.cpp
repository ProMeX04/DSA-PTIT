#include <iostream>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t-- ){
        int n; cin >> n;
        int count = 0;
        int A[10] = {1,2,5,10,20,50,100,200,500,1000};
        for (int i = 9;i >= 0; i--) {
            count += n / A[i];
            n %= A[i];
        }
        cout << count << endl;
    }
}