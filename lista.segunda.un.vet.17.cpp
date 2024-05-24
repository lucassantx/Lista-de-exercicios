#include <iostream>
using namespace std;

int main() {
  float vetor[10];

  cout << "Digite 10 valores: " << endl;
  for (int i = 0; i < 10; ++i) {
    cin >> vetor[i];
  }

  for (int i = 0; i < 10; ++i) {
    if (vetor[i] < 0) {
      vetor[i] = 0;
    }
  }
  
  cout << "Lista sem números negativos: " << endl;
  for (int i = 0; i < 10; ++i) {
    cout << vetor[i] << endl;
  }

  return 0;
}
