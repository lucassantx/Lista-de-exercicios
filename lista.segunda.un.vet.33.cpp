#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int tam = 15;
    vector<int> vetor(tam);

    cout << "Digite 15 numeros: " << endl;
    for (int i = 0; i < tam; i++) {
        cin >> vetor[i];
    }

    for (int i = 1; i < tam; i++) {
        if (vetor[i] == 0 && i > 0) {
            swap(vetor[i], vetor[i - 1]);
        }
    }

    cout << "Vetor compactado: ";
    for (int i = 0; i < tam; i++) {
        cout << vetor[i] << " ";
    }
    cout << endl;

    return 0;
}
