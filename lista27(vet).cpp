#include <iostream>
#include <vector>
#include <math.h>

using namespace std;

bool ehPrimo(int num) {
    if (num <= 1) return false;
    if (num == 2) return true;
    if (num % 2 == 0) return false;

    for (int i = 3; i <= sqrt(num); i += 2) {
        if (num % i == 0) return false;
    }
    return true;
}

int main() {
    vector<int> num(10);
    cout << "Digite 10 números inteiros:" << endl;

    for (int i = 0; i < 10; ++i) {
        cout << "Número " << i + 1 << ": ";
        cin >> num[i];
    }

    cout << "Números primos e suas posições:" << endl;
    for (int i = 0; i < 10; ++i) {
        if (ehPrimo(num[i])) {
            cout << "Número: " << num[i] << " posição: " << i << endl;
        }
    }

    return 0;
}
