#include<iostream>
using namespace std;

void prevBinary(string& bin, int n) {
    while(bin[n - 1] == '0') {bin[n - 1] = '1'; n --;}
    bin[n - 1] = '0';
    bin = &bin[1]; 
}
int main(){   
    int t; cin >> t;
    while(t--) {
        string bin;
        cin >> bin;
        bin = "1" + bin;
        prevBinary(bin, bin.length());
        cout << bin << endl;
    }
}