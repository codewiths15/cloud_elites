#include<iostream>
using namespace std;

void bus_line(char ch)
{
  for (int x=80;x>0;x--)
  cout<<ch;
}

int main(){


bus_line('*');
cout<<endl;
cout<<"Bus Number: \t"<<"123"
  <<"\nDriver: \t"<<"ABC"
  <<"\t\tArrival Time: \t"<<"11.44"
  <<"\tDeparture Time:"<<"12.45"
  <<"\nFrom: \t\t"<<"xyz"
  <<"\t\tTo: \t\t"<<"pqr"<<"\n"<<"\n";
bus_line('*');



}
