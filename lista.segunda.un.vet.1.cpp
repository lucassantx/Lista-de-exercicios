#include <iostream>
using namespace std;

int main() {
    
    int A[6] = {1, 0, 5, -2, -5, 7};

    int soma = A[0] + A[1] + A[5];
   cout << "A soma dos valores nas posições definidas é: " << soma << endl;
  
    A[4] = 100;

    cout << "Os valores do vetor A são:" << endl;
    for(int i = 0; i < 6; i++) {
        cout << A[i] << endl;
    }

    return 0;
}
