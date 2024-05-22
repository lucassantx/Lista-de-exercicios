#include <iostream>
using namespace std;

int main() {
  float vetor[10];
  int neg = 0;
  float sp = 0.0;

  cout << "Digite 10 valores: " << endl;
  for (int i = 0; i < 10; ++i) {
    cin >> vetor[i];
  }

  for (int i = 0; i < 10; ++i) {
    if (vetor[i] < 0) {
      neg++;
    } else {
      sp += vetor[i];
    }
  }

  cout << "números negativos: " << neg << endl;
  cout << "Soma dos numeros positivos: " << sp << endl;

  return 0;
}
