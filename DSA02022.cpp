#include <iostream>
#include <vector>
using namespace std;

int main() {
    vector<string> date = {"02", "20", "22"};
    vector<string> year = {"2000", "2002", "2020", "2022", "2200", "2202", "2220", "2222"};
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 8; j++)
            cout << date[i] + "/02/" + year[j] << endl;

}