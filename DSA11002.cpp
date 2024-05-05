#include <iostream>
#include <deque>
#include <vector>
#include <algorithm>
#include <cstring>
#include <string>
#include <sstream>
using namespace std;
void function() {
    int n; cin >> n;
    deque<int> stack;
    string str;
    getline(cin >> ws, str);
    string i;
    stringstream ss(str);
    vector <string> formulation;
    while (ss >> i){
        formulation.push_back(i);
    }
    reverse(formulation.begin(), formulation.end());
    string operators = "+-*/";
    for (auto i: formulation){
        if (operators.find(i) == string::npos) {
            stack.push_back(stoi(i));
        } else {
            int operand2 = stack.front();
            stack.pop_front();
            int operand1 = stack.front();
            stack.pop_front();
            int result;
            if (i == "+") {
                result = operand1 + operand2;
            } else if (i == "-") {
                result = operand1 - operand2;
            } else if (i == "*") {
                result = operand1 * operand2;
            } else if (i == "/") {
                result = operand1 / operand2;
            }
            stack.push_back(result);
        }
    }
    cout << stack.front() << endl;
}

int main() {
    int t;
    cin >> t;
    for (int i = 0; i < t; ++i) {
        function();
    }
    return 0;
}
