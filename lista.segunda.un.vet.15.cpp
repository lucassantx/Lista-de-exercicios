#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    vector<int> vec(20);
    unordered_set<int> sr;
    unordered_set<int> dp;
    vector<int> vu;

    cout << "Digite 20 valores:" << endl;
    for (int i = 0; i < 20; ++i) {
        cin >> vec[i];
        if (sr.find(vec[i]) != sr.end()) {
            dp.insert(vec[i]);
        } else {
            sr.insert(vec[i]);
        }
    }

    for (int i = 0; i < 20; ++i) {
        if (dp.find(vec[i]) == dp.end()) {
            vu.push_back(vec[i]);
        }
    }

    cout << "Valores sem repetições : ";
    for (int val : vu) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
