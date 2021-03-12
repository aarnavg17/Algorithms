//
//  main.cpp
//  TowerOfHanoi
//
//  Created by Aarnav Gupta on 03/03/21.
//

#include <iostream>
using namespace std;

void Towers (int n, int Source, int Target, int Interm) {
    if (n == 1) cout << "From " << Source << " To " << Target << endl;
    else {
        Towers (n-1, Source, Interm, Target);
        Towers(1, Source, Target, Interm);
        Towers(n-1, Interm, Target, Source);
    }
}

int main(int argc, const char * argv[]) {
    Towers(3, 0, 2, 1);
}
