#include <iostream>
#include <fstream>

using namespace std;


int main(int argc, char const *argv[])
{
	ifstream myfile(argv[1]);
	ofstream myfileoutput;

	myfileoutput.open("input.txt");

	for(string line; getline(myfile, line);){
		
		string newString;
		
		if(line[0]=='2' && line[3] != '0'){
			
			int i = 3;
			while(line[i] != ' ')
			newString += line[i++]; 

			newString += " ";
			newString += line[i+1];
			newString += ",";


			while(line[i] != '0')
				i++;
			i++;
			i++;
			
			while(line[i] != '\0')
				newString += line[i++];
			
			myfileoutput << newString + "\n";

		} 

		
		
	}
	

	myfileoutput.close();
	myfile.close();


	return 0;
}