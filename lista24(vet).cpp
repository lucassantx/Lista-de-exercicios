#include <iostream>
#include <vector>
using namespace std;

struct Aluno {
    int numero;
    float altura;
};

int main() {
  
    vector<Aluno> alunos(10);

    cout << "Digite o número e a altura (em metros) de 10 alunos: " << endl;
    for (int i = 0; i < 10; ++i) {
        cout << "Aluno " << i + 1 << ": ";
        cin >> alunos[i].numero >> alunos[i].altura;
    }

    int baixo = 0;
    int alto = 0;

    for (int i = 1; i < 10; ++i) {
        if (alunos[i].altura < alunos[baixo].altura) {
            baixo = i;
        }
        if (alunos[i].altura > alunos[alto].altura) {
            alto = i;
        }
    }

    cout << "Aluno mais baixo: Número " << alunos[baixo].numero 
         << ", Altura " << alunos[baixo].altura << " metros" << endl;
    cout << "Aluno mais alto: Número " << alunos[alto].numero 
         << ", Altura " << alunos[alto].altura << " metros" << endl;

    return 0;
}
