#include <iostream>
using namespace std;

int main() {
  float vetor[5];

  cout << "Digite 5 valores: " << endl;
  for (int i = 0; i < 5; ++i) {
    cin >> vetor[i];
  }

  float maior = vetor[0];
  float menor = vetor[0];
  int p1 = 0;
  int p2 = 0;

  for (int i = 1; i < 5; i++) {
    if (vetor[i] > maior) {
      maior = vetor[i];
      p1 = i;
    }
    if (vetor[i] < menor) {
      menor = vetor[i];
      p2 = i;
    }
  }
  cout << "posição do maior valor: " << p1 << endl;
  cout << "posição do menor valor: " << p2 << endl;

  return 0;
}
