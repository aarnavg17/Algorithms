#include<iostream>
using namespace std;

int fib(int n) {
    if (n <= 1) {
        return (n);
    }
    else {
        long long int A = 0, B = 1, C;
        C = A + B;
        for (int i = 0; i < n - 2; i++) {
            A = B;
            B = C;
            C = A + B;
        }
        return (C);
    }
}

int main() {
    long long int n;
    cin >> n;
    cout << fib(n);
}
