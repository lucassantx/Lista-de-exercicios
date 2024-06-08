#include <iostream>
#include <math.h>
#include <vector>
using namespace std;

double Media(const vector<double> &vetor) {
  double soma = 0.0;
  for (double valor : vetor) {
    soma += valor;
  }
  return soma / vetor.size();
}

double Desvio(const vector<double> &vetor) {
  double media = Media(vetor);
  double sumq = 0.0;
  for (double valor : vetor) {
    sumq += (valor - media) * (valor - media);
  }
  return sqrt(sumq / vetor.size());
}

int main() {
  vector<double> vetor(10);

  cout << "Digite 10 valores: " << endl;
  for (int i = 0; i < 10; i++)
    cin >> vetor[i];
  double media = Media(vetor);
  double desvio = Desvio(vetor);

  cout << "Média: " << media << endl;
  cout << "Desvio Padrão: " << desvio << endl;

  return 0;
}
