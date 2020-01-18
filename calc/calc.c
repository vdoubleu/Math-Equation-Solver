#include <iostream>
#include <string>
#include <map>
using namespace std;

map<int, int> differentiate(map<int, int> a){
	map<int, int> deriv;
	map<int, int> :: iterator itr;
	for (itr = a.begin()+1; itr != a.end(); itr++){
		deriv.insert(pair<int, int>((itr->first)-1,(itr->first)*(itr->second)));
	}
	return deriv;

}

int main(){
	map<int, int> first = { {1,4}, {2,3}  };
	map<int, int> deriv = differentiate(first);

	cout << deriv.begin()->first << endl;
	return 0;


}
