/* Extra Long Factorials

URL: https://www.hackerrank.com/challenges/extra-long-factorials/

*/

#include <iostream>
using namespace std;

void extraLongFactorials(int n) {
	int max_size = 3;
	int result[max_size];
	result[max_size-1] = 1;
	for(int i = 1; i <= n; i++) { 
		for (int j = max_size-1; j >= 0; j--){
			int mul_result = result[j] * i;
			if (mul_result > 9) {
				int first_digit = mul_result % 10;
				int second_digit = mul_result % 100;
				result[j] = first_digit;
				result[--j]+= second_digit;
			} else {
				result[j] = mul_result;
			}
		}
	}
	for (int i = max_size-1; i >= 0; i++) {
		cout << result[i] << " ";
	}

}

int main() {
	int n;
	cin >> n;
	cin.ignore(numeric_limits<streamsize>::max(), '\n');
	extraLongFactorials(n);
	return 0;
}
