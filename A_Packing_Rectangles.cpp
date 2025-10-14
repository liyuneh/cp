#include<iostream>
#include<algorithm>
long long w , h , n;
using namespace std;


bool good(long long x){
    return (x / w) * (x / h) >= n;
}

int main(){
    cin >> w >> h >> n;
    long long l = 0, r = 1;
    while (!good(r)) r *= 2;

    while (r > l + 1){
        long long middle = l + (r - l)/2;
        if(good(middle)){
            r= middle;
        }
        else{
            l = middle;
        }
    }
    cout << r<<"\n";
    return 0;
}