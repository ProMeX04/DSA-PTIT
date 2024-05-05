#include <iostream>
#include <vector>
#include <algorithm>

void function() {
    int n;
    std::cin >> n;
    std::vector<int> ls(n);
    for (int i = 0; i < n; ++i) {
        int x; std::cin >>x;
        ls[i] = -x;
    }

    std::make_heap(ls.begin(), ls.end());

    int result = 0;
    while (ls.size() > 1) {
        int top1 = ls[0];
        std::pop_heap(ls.begin(), ls.end());
        ls.pop_back();
        int top2 = ls[0];
        std::pop_heap(ls.begin(), ls.end());
        ls.pop_back();
        result -= (top1 + top2) % 1000000007;
        result %= 1000000007;
        ls.push_back((top1 + top2) % 1000000007);
        std::push_heap(ls.begin(), ls.end());
    }
    std::cout << result << std::endl;
}

int main() {
    int t;
    std::cin >> t;
    while (t--) {
        function();
    }
    return 0;
}
