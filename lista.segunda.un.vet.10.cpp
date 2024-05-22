#include <iostream>
using namespace std;

int main() {

  float vetor[15];
  float m;
  float s = 0;

  cout << "Digite as notas dos 15 alunos: " << endl;
  for (int i = 0; i < 15; ++i) {
    cin >> vetor[i];
    s += vetor[i];
  }

  m = s / 15;

  cout << "A média das notas é: " << m << endl;

  return 0;
}
