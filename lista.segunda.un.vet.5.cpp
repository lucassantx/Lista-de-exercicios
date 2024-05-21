#include <iostream>
using namespace std;

int main() {
    int vetor[10];
    int cPar = 0;

    cout << "Digite 10 valores inteiros: " << endl;
    for (int i = 0; i < 10; ++i) {
        cin >> vetor[i];
        if (vetor[i] % 2 == 0) {
            ++cPar;
        }
    }

    cout << "Valores pares: " << cPar << endl;

    return 0;
}
