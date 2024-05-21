#include <iostream>
using namespace std;

int main() {
    int vetor[10];

    cout << "Digite 10 valores inteiros: " << endl;
    for (int i = 0; i < 10; ++i) {
        cin >> vetor[i];
     
    }
  
   int maior = vetor[0];
   int menor = vetor[0];
  
  for (int i = 1; i < 10; i++) {
    if (vetor[i] > maior) {
      maior = vetor[i];
    }
    if (vetor[i] < menor) {
      menor = vetor[i];
    }
    
  }
   cout << "Maior valor: " << maior << endl;
   cout << "Menor valor: " << menor << endl;
  
  return 0;

  }
