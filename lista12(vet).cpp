#include <iostream>
using namespace std;

int main() {
  float vetor[5];
  float med = 0;
  float s = 0;

  cout << "Digite 5 valores: " << endl;
  for (int i = 0; i < 5; ++i) {
    cin >> vetor[i];
    s += vetor[i];
  }
  med = s / 5;

  float maior = vetor[0];
  float menor = vetor[0];

  for (int i = 1; i < 5; i++) {
    if (vetor[i] > maior) {
      maior = vetor[i];
    }
    if (vetor[i] < menor) {
      menor = vetor[i];
    }
  }
  cout << "Maior valor: " << maior << endl;
  cout << "Menor valor: " << menor << endl;
  cout << "Média: " << med << endl;

  return 0;
}
