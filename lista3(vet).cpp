#include <iostream>
#include <vector>
using namespace std;

int main() {
    const int size = 10;
    vector<double> numbers(size); 
    vector<double> squares(size);
  
    cout << "Digite 10 números reais: " << endl;
    for(int i = 0; i < size; ++i) {
        cin >> numbers[i];
    }

    for(int i = 0; i < size; ++i) {
        squares[i] = numbers[i] * numbers[i];
        
    }
    

    
    cout << "Números reais: " << endl;
    for(int i = 0; i < size; ++i) {
        cout << numbers[i] << " " << endl;
      
    }
    cout << endl;

  
    cout << "Quadrados: " << endl; 
    for(int i = 0; i < size; ++i) {
        cout << squares[i] << " " << endl;
    }
    cout << endl;

    return 0;
}
