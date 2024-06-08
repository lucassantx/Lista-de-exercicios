#include <iostream>
#include <vector>

using namespace std;

int main() {
  vector<int> v(10);
  vector<int> v1;
  vector<int> v2;

  cout << "Digite 10 números inteiros:" << endl;

  for (int i = 0; i < 10; ++i) {
    cout << "Número " << i + 1 << ": ";
    cin >> v[i];
  }

  for (int i = 0; i < 10; ++i) {
    if (v[i] % 2 != 0) {
      v1.push_back(v[i]);
    } else {
      v2.push_back(v[i]);
    }
  }

  cout << "Elementos utilizados do vetor v1 (ímpares):" << endl;
  for (int num : v1) {
    cout << num << " ";
  }
  cout << endl;

  cout << "Elementos utilizados do vetor v2 (pares):" << endl;
  for (int num : v2) {
    cout << num << " ";
  }
  cout << endl;

  return 0;
}
