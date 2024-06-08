#include <iostream>
using namespace std;

int main() {
    int vetor[8];

    cout << "Digite 8 valores inteiros: " << endl;
    for (int i = 0; i < 8; ++i) {
        cin >> vetor[i];
    }

    int X, Y;
    cout << "Digite o valor de X (0 a 7): ";
    cin >> X;
    cout << "Digite o valor de Y (0 a 7): ";
    cin >> Y;

    if (X >= 0 && X < 8 && Y >= 0 && Y < 8) {
        int soma = vetor[X] + vetor[Y];
        cout << "A soma dos valores nas posições " << X << " e " << Y << " é: " << soma << endl;
    } else {
        cout << "insira valores entre 0 e 7." << endl;
    }

    return 0;
}
