#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;
struct edge {
    int b, e, w;

    bool operator<(edge another) {
        return w < another.w;
    }
};


class Disjoint_Sets {
private:
    int n;
    int* parent;
    int* rank;
public:
    Disjoint_Sets(int n) {
        this -> n = n;
        this -> rank = new int[this -> n + 1];
        this -> parent = new int[this -> n + 1];
        for (int i = 1; i <= n; i ++) {
            this -> parent[i] = i;
            this -> rank[i] = 0;
        }
    }

    int find(int u) {
        if (parent[u] != u) parent[u] = find(parent[u]);
        return parent[u];
    }

    void Union(int b, int e) {
        int xset = find(b);
        int yset = find(e);

        if (xset == yset) return;
        if (rank [xset] < rank[yset]) parent[xset] = yset; 
        else if (rank[xset] > rank[yset]) parent[yset] = xset;
        else {
            parent [yset] = xset;
            rank[xset] += 1;
        }
    }
};


int n;
vector<edge> edges;


void init() {
    cin >> n;
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= n; j++) {
            int k; cin >> k;
            if (k != 10000 and k != 0) {
                edges.push_back({i, j, k});
            }
        }
    }
    sort(edges.begin (), edges.end());
    for (auto x: edges){
        cout << x.b << " " << x.e << " " << x.w << endl;
    }
}

void kruskal() {
    Disjoint_Sets djs(n);
    int num_edge = 0;
    int len_tree = 0;
    vector <edge> result;
    for (auto x : edges) {
        if (num_edge == n - 1) break;
        if (djs.find(x.b) != djs.find(x.e)){
            djs.Union(x.b, x.e);
            num_edge ++;
            len_tree += x.w;
            result.push_back(x);
        }
    }

    // for (auto x: result){
    //     cout << x.b << " " << x.e <<  " " << x.w << endl;
    // }
    cout << len_tree << " ";
    // for (int i = 1; i <= n; i++) djs.find(i); 
    // djs.print();
}

int main() {
    init();
    kruskal();

}
