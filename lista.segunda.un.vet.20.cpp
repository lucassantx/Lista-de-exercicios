#include <iostream>
#include <vector>
using namespace std;

int main() {

  int vetor[10];
  vector<int> vi;

  cout << "Digite 10 números inteiros entre 0 e 50: " << endl;
  for (int i = 0; i < 10; ++i) {
    do {
      cin >> vetor[i];
      if (vetor[i] < 0 || vetor[i] > 50) {
        cout << "digite um número entre 0 e 50!: ";
      }
    } while (vetor[i] < 0 || vetor[i] > 50);
  }

  for (int i = 0; i < 10; ++i) {
    if (vetor[i] % 2 != 0) {
      vi.push_back(vetor[i]);
    }
  }

  cout << "lista Original:\tlista de Ímpares:" << endl;
  for (int i = 0; i < 10; ++i) {
    cout << vetor[i];
    if (i < 10 - 1) {
      cout << "\t\t";
    }
    if (i < vi.size()) {
      cout << vi[i];
    }
    cout << endl;
  }

  return 0;
}
