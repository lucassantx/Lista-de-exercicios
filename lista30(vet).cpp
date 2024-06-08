#include <algorithm>
#include <iostream>
#include <vector>
using namespace std;

vector<int> encontrarIntersecao(const vector<int> &vetor1,
                                const vector<int> &vetor2) {
  vector<int> intersecao;

  vector<int> v1 = vetor1;
  vector<int> v2 = vetor2;
  sort(v1.begin(), v1.end());
  sort(v2.begin(), v2.end());

  int i = 0, j = 0;
  while (i < v1.size() && j < v2.size()) {
    if (v1[i] < v2[j]) {
      i++;
    } else if (v1[i] > v2[j]) {
      j++;
    } else {

      if (intersecao.empty() || v1[i] != intersecao.back()) {
        intersecao.push_back(v1[i]);
      }
      i++;
      j++;
    }
  }
  return intersecao;
}

int main() {
  const int tamanho = 10;
  vector<int> vetor1(tamanho);
  vector<int> vetor2(tamanho);

  cout << "Digite os elementos do primeiro vetor:" << endl;
  for (int i = 0; i < tamanho; ++i) {
    cout << "Elemento " << i + 1 << ": ";
    cin >> vetor1[i];
  }

  cout << "\nDigite os elementos do segundo vetor:" << endl;
  for (int i = 0; i < tamanho; ++i) {
    cout << "Elemento " << i + 1 << ": ";
    cin >> vetor2[i];
  }

  vector<int> intersecao = encontrarIntersecao(vetor1, vetor2);

  cout << "\nInterseção dos dois vetores:" << endl;
  if (intersecao.empty()) {
    cout << "Nenhum elemento em comum encontrado." << endl;
  } else {
    for (int num : intersecao) {
      cout << num << " ";
    }
    cout << endl;
  }

  return 0;
}
