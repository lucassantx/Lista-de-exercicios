#include <iostream>
#include <vector>
using namespace std;

vector<int> subvet(const vector<int> &vA, const vector<int> &vB) {

  vector<int> R(vA.size());
  for (size_t i = 0; i < vA.size(); ++i) {
    R[i] = vA[i] - vB[i];
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

  vector<int> R = subvet(vA, vB);

  cout << "Vetor A - Vetor B: ";
  for (size_t i = 0; i < R.size(); ++i) {
    cout << R[i] << " ";
  }
  cout << endl;

  return 0;
}
