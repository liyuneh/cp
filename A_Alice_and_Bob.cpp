#include <iostream>
#include <vector>
using namespace std;

int main(){
    int t;
    cin >> t;
    for (int i = 0; i < t; i++){
        int n, m;
        int l = 0, r = 0;
        cin >> n >> m;
        vector<int> arr(n);
        for (int j = 0 ; j < n; j++){
            cin >> arr[j];
            if (m < arr[j]) ++l;
            if (m > arr[j]) ++r;
        }
        cout << (l <= r ? m + 1 : m - 1) << endl;

    }
    return 0;
}