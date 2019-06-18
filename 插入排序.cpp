#include<iostream>
#include <stdlib.h>
#include <time.h> 
using namespace std;
void main()
{
	srand((unsigned)time(NULL));
	int a[10] = { 0 };
	int key,len = 0;
	for (int i = 0; i < 10; i++){
		a[i] = rand();/*将随机数加入数组*/
		cout << a[i] << '\t';
		len++;
	}
	cout << endl;
	for (int j = 1,i; j < len; j++){
		key = a[j];
		i = j - 1;/*获得前面一个序号*/
		while (i>=0 && a[i]>key){
			a[i + 1] = a[i];
			i = i - 1;
		}
		a[i + 1] = key;
	}
	for (int i = 0; i < len; i++){
		cout << a[i] << '\t';
	}
	cout << endl;
}