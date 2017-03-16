#include <string>
#include <bitset>
#include <iostream>

int main()
{
   int target = 1500;
   std::cout << "Choose a Position";
   std::cin >> target;
  // target = target*4;

   std::string binary = std::bitset<14>(target).to_string(); //to binary
   std::cout<<binary<<"\n";
   std::string tempLowSpeed = binary.substr(7,7);
   std::string tempHighSpeed = binary.substr(0,7);
   std::cout<<tempLowSpeed<<" Low\n";
   std::cout<<tempHighSpeed<<" High\n";
   std::string lowSpeed = "0";
   std::string highSpeed = "0";
   lowSpeed.append(tempLowSpeed);
   highSpeed.append(tempHighSpeed);

   std::cout<<lowSpeed<<" Real Low\n";
   std::cout<<highSpeed<<" Real High\n";

   int lowSpeedInt = std::stoi (lowSpeed);
   // TODO: (Dropped because python is superior for serial data supposively )
   // use stoi to convert to integer then convert to hexidecimal
   unsigned long decimal = std::bitset<14>(target).to_ulong();
   std::cout<<decimal<<"\n";
   return 0;
}
