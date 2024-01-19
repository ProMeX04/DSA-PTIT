#include <iostream>
using namespace std;
int main(){   
    int t; cin >> t;
    while (t--) {
        int canBuy, needDay, dayNeed;
        cin >> canBuy >> needDay >> dayNeed;
        int result;
        if (7 * dayNeed > 6 * canBuy) result = -1;
        else {
            result = (needDay * dayNeed + canBuy-1) / canBuy;
        }   
        cout << result << endl;
    }
}