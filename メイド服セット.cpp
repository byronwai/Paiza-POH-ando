#include <iostream>
using namespace std;
int main(void){
	int N;
	cin >> N;
	int extra;
	while (N--){
		cin >> extra;
		int sleep = (24+1)*60 - extra / 3;
		int hr = (sleep/60)%24;
		int min = sleep%60;
		if (hr > 10)
			cout << hr << ":";
		else
			cout<< 0 << hr << ":";
		
		if (min > 10)
			cout << min << endl;
		else
			cout<< 0 << min << endl;
	}
}