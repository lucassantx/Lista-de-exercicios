#include <iostream>
#include <vector>
using namespace std;

float vetprod(const vector<float> &vA, const vector<float> &vB) {
  float R = 0.0;
  for (size_t i = 0; i < vA.size(); ++i) {
    R += vA[i] * vB[i];
  }
  return R;
}

int main() {

  vector<float> vA(5);
  vector<float> vB(5);

  cout << "Digite 5 números para o vetor A: " << endl;
  for (int i = 0; i < 5; ++i) {
    cin >> vA[i];
  }

  cout << "Digite 5 números para o vetor B: " << endl;
  for (int i = 0; i < 5; ++i) {
    cin >> vB[i];
  }

  cout << "vetor A: ";
  for (int i = 0; i < 5; ++i) {
    cout << vA[i] << " ";
    cout << endl;
  }

  cout << "vetor B: ";
  for (int i = 0; i < 5; ++i) {
    cout << vB[i] << " ";
    cout << endl;
  }

  float R = vetprod(vA, vB);
  cout << "vetor escalar: " << R;

  return 0;
}
