#include <iostream>
#include <vector>
using namespace std;

bool isValidNumber(int num) {
    if (num % 7 == 0 || num % 10 == 7) {
        return false;
    }
    return true;
}

int main() {
    vector<int> vetor(100);
    int count = 0;
    int num = 1;

    while (count < 100) {
        if (isValidNumber(num)) {
            vetor[count] = num;
            count++;
        }
        num++;
    }

    cout << "Vetor com os 100 primeiros naturais que não são múltiplos de 7 ou terminam com 7:" << endl;
    for (int i = 0; i < 100; ++i) {
        cout << vetor[i] << " ";
    }
    cout << endl;

    return 0;
}
