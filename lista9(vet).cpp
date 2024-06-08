#include <iostream>
using namespace std;

int main() {

    int vetor[6];

    cout << "Digite 6 valores inteiros pares: " << endl;
    for (int i = 0; i < 6; ++i) {
        cin >> vetor[i];
        
        if (!(vetor[i] = vetor[i] % 2 == 0)) { 
          cout << "Insira apenas valores pares!" << endl;
          return 0;

          }

    }
    
    cout << "Valores: " << endl;
    for (int i = 0; i < 6; ++i) {
        cout << "Posição " << i << ": " << vetor[i] << endl;
    }

    for (int i = 0; i < 6 / 2; ++i) {
        int in = vetor[i];
        vetor[i] = vetor[6 - 1 - i]; 
        vetor[6 - 1 - i] = in;
    }

    cout << "Valores invertidos:" << endl;
    for (int i = 0; i < 6; ++i) {
        cout << "Posição " << i << ": " << vetor[i] << endl;
        
    }

    return 0;
}
