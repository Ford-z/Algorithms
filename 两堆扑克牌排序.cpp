#include<iostream>
#include<stack>
using namespace std;

void main(){
	stack<int>s1;
	stack<int>s2;
	int a[5] = { 17, 8, 7, 6, 2};
	int b[5] = { 20, 18, 15, 10, 6 };
	int c[10];
	for (int i = 0; i < 5; i++){
		s1.push(a[i]);
		s2.push(b[i]);
	}
	int i= 0;
	while (s1.empty() != true || s2.empty() != true){
		if (s1.empty() == true || s2.empty() == true){
			if (s1.empty() == true){
				c[i] = s2.top();
				s2.pop();
			}
			else{
				c[i] = s1.top();
				s1.pop();
			}
		}
		else{
			if ((s1.top()) <= (s2.top())){
				c[i] = s1.top();
				s1.pop();
			}
			else{
				c[i] = s2.top();
				s2.pop();
			}
		}
		i++;
	}
	for (int j = 0; j < 10; j++){
		cout << c[j] << "\t";
	}
	cout << endl;
}