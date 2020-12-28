#include<iostream>
using namespace std;
int a[5] = { 15, 6, 8, 19, 20 };
void quicksort(int l, int r){
	int i = l;
	int j = r;
	int temp = a[i];
	if (i<j){
		while (i < j){
			while (a[j] >= temp && i<j){
				j--;
			}
			if (i < j){
				a[i] = a[j];
				i++;
			}
			while (a[i] < temp && i < j){
				i++;
			}
			if (i < j){
				a[j] = a[i];
				j--;
			}
		}
		a[i] = temp;
		quicksort(l, i - 1);
		quicksort(i + 1, r);
	}
}
int main(){
	quicksort(0, 4);
	for (int i = 0; i <= 4; i++){
		cout << a[i] << endl;
	}
	return 0;
}
