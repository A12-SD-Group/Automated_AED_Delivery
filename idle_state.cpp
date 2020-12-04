#include <iostream>
#include <wiringPi.h>

using namespace std;
 

int main()
{
	wiringPiSetup();	//Setup the library
	pinMode(0, OUTPUT); //configure SPIO0 as ouptut
	pinMode(1, INPUT);	//configure GPIO1 as input
	cout<<"Hello World";
	cout<<"testing git";
	
	while(1)
	{
		if(digitalRead(1)==1){
				digitalWrite(0, !digitalRead(0));
				delay(500);
		}
	}
	return 0;
}
