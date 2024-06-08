#include <iostream>
#include <vector>
#include <unordered_set>

using namespace std;

int main() {
    vector<int> vec(10);
    unordered_set<int> sr;
    unordered_set<int> dp;

    cout << "Digite 10 valores:" << endl;
    for (int i = 0; i < 10; ++i) {
        cin >> vec[i];
        if (sr.find(vec[i]) != sr.end()) {
            dp.insert(vec[i]);
        } else {
            sr.insert(vec[i]);
        }
    }

    cout << "Valores iguais: ";
    for (int val : dp) {
        cout << val << " ";
    }
    cout << endl;

    return 0;
}
