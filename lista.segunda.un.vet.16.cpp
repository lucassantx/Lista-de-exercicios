#include <iostream>
using namespace std;

int main() {

    float vetor[5];

    cout << "Digite 5 valores: " << endl;
    for (int i = 0; i < 5; ++i) {
        cin >> vetor[i];
    }

   
int cod;
  cout << "digite 0 para encerrar; 1 para mostrar a lista na ordem direta; 2 para mostrar a lista na ordem inversa: ";
  cin >> cod;

  switch (cod) {
    case 0:
    return 0;
    
  case 1:
    cout << "Valores: " << endl;
    for (int i = 0; i < 5; ++i) {
        cout << "Posição " << i << ": " << vetor[i] << endl;
    }
    break;

    case 2:
    for (int i = 0; i < 5 / 2; ++i) {
        int in = vetor[i];
        vetor[i] = vetor[5 - 1 - i]; 
        vetor[5 - 1 - i] = in;
    }
    cout << "Valores invertidos:" << endl;
    for (int i = 0; i < 5; ++i) {
        cout << "Posição " << i << ": " << vetor[i] << endl;
    }
     break;
    
default: 
  cout << "insira um valor válido! (0,1 ou 2)";
    return 1;
    
  }
}
