#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

int main () {

  const int size = 10;
  vector<int> v1(size);
  vector<int> v2(size);
  unordered_set<int> uniao;

  cout << "digite 10 números para o vetor 1: " << endl;
  for (int i = 0; i < size; i++) {
    cin >> v1[i]; 
    uniao.insert(v1[i]); 
  }

  cout << "digite 10 números para o vetor 2: " << endl;
  for (int i = 0; i < size; i++) {
    cin >> v2[i];
  uniao.insert(v2[i]); 
}

vector<int> res(uniao.begin(), uniao.end());

  cout << "A união dos vetores é: " << endl;
  for (const int& num : res) {
    cout << num << " ";
  }
  
  cout << endl;

  return 0;
 
}
