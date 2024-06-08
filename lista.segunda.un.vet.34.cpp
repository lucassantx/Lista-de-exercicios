#include <iostream>
#include <vector>
using namespace std;

int main() {
  const int tam = 10;
  vector<int> vetor;
  int numero;

  cout << "Digite 10 numeros diferentes: " << endl;
  while (vetor.size() < tam) {
    cin >> numero;

    bool existe = false;
    for (int i = 0; i < vetor.size(); i++) {
      if (vetor[i] == numero) {
        existe = true;
        break;
      }
    }

    if (existe) {
      cout << "digite um número diferente: " << endl;
    } else {
      vetor.push_back(numero);
    }
  }

  cout << "Vetor: ";
  for (int i = 0; i < vetor.size(); i++) {
    cout << vetor[i] << " ";
  }
  cout << endl;

  return 0;
}
