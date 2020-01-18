#include <iostream>
#include <string>
#include <map>
using namespace std;
int evaluate(map<int, int> a, double x);
map<int, int> differentiate(map<int, int> a){
	map<int, int> deriv;
	map<int, int> :: iterator itr;
	for (itr = a.begin(); itr != a.end(); itr++){
		deriv.insert(pair<int, int>((itr->first)-1,(itr->first)*(itr->second)));
	}
	return deriv;
}
int lowerBound(map<int, int> a){
	int test = -10;
	while (evaluate(a, test) *evaluate(differentiate(a), test) < 0){
		test = test * 10;
	}
	return test;
}
int upperBound(map<int, int> a){
	int test = 10;
	while (evaluate(a, test) * evaluate(differentiate(a), test) < 0){
		test = test * 10;
	}
	return test;
}
int power(int a, int b){
	if (b == 0) return 1;
	if (b == 1) return a;
	else return  a * power(a, b-1);


}
double evaluate(map<int, int> a, double x){
	int value = 0;
	map<int, int> :: iterator itr;
	for (itr = a.begin(); itr != a.end(); itr++){
		value += (itr->second)*(power(x, itr->first));
	}
	return value;
}

double newton(map<int, int> a, int lower, int upper){
	double curr = evaluate(a, lower);


}
int main(){
	map<int, int> first;
	first.insert(pair<int, int>(1,2));
	first.insert(pair<int, int>(2,4));
	map<int, int> deriv = differentiate(first);
	map<int, int> :: iterator itr;
	for (itr = deriv.begin(); itr != deriv.end(); itr++){
		cout << itr -> first << endl;
		cout << itr -> second << endl;
	}
	cout << lowerBound(first) << endl;
	cout << upperBound(first) << endl;
	return 0;


}
