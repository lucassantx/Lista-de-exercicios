#include <iostream>
#include <vector>
using namespace std;

vector<int> mixVet(const vector<int> &vA, const vector<int> &vB) {
  vector<int> R(vA.size());
  for (size_t i = 0; i < vA.size(); ++i) {
    if (i % 2 == 0) {
      R[i] = vA[i];
    } else {
      R[i] = vB[i];
    }
  }
  return R;
}

int main() {

  vector<int> vA(10);
  vector<int> vB(10);

  cout << "Digite 10 números inteiros para o vetor A: " << endl;
  for (int i = 0; i < 10; ++i) {
    cin >> vA[i];
  }

  cout << "Digite 10 números inteiros para o vetor B: " << endl;
  for (int i = 0; i < 10; ++i) {
    cin >> vB[i];
  }

  vector<int> R = mixVet(vA, vB);

  cout << "Vetor resultante: ";
  for (size_t i = 0; i < R.size(); ++i) {
    cout << R[i] << " ";
  }

  cout << endl;

  return 0;
}
