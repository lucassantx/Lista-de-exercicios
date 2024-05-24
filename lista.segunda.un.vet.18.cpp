#include <iostream>
#include <vector>
using namespace std;

int main() {
  
    vector<int> vetor(10);
    int x;

    cout << "Digite 10 números inteiros:" << endl;
    for (int i = 0; i < 10; ++i) {
        cin >> vetor[i];
    }

    cout << "Digite um número inteiro: ";
    cin >> x;

    vector<int> m;
    for (int i = 0; i < 10; ++i) {
        if (vetor[i] % x == 0) {
            m.push_back(vetor[i]);
        }
    }

    cout << "Os múltiplos de " << x << " no vetor são: ";
    for (int i = 0; i < m.size(); ++i) {
        cout << m[i] << " ";
    }
  
    return 0;
}
