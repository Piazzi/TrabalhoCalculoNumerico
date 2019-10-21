#include <iostream>

using namespace std;

int main()
{
    float n = 0.5;
    int cont = 0;
    while(1+n != 1)
    {
        n = n/2;
        cont++;
    }
    cout <<"N = " << n << endl;
    cout <<"Numero de iteracoes: " << cont << endl;
    return 0;
}
