#include <iostream>
#include <vector>
using namespace std;

int main() {
  vector<int> numeros;
  int num;

  for (int i = 0; i < 6; ++i) {
    cout << "Digite o número " << i + 1 << ": ";
    cin >> num;
    numeros.push_back(num);
  }

  vector<int> pares;
  vector<int> impares;

  for (int num : numeros) {
    if (num % 2 == 0)
      pares.push_back(num);
    else
      impares.push_back(num);
  }

  int soma_pares = 0;
  for (int num : pares) {
    soma_pares += num;
  }

  int qtd_impares = impares.size();

  cout << "Números pares: ";
  for (int num : pares) {
    cout << " " << num;
  }
  cout << endl;

  cout << "Soma dos números pares: " << soma_pares << endl;

  cout << "Números ímpares: ";
  for (int num : impares) {
    cout << " " << num;
  }
  cout << endl;

  cout << "Quantidade de números ímpares: " << qtd_impares << endl;

  return 0;
}
