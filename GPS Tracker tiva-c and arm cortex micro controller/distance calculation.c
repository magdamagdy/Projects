#include "distance.h"

void SystemInit(){CPAC |= 0x00F00000;}

//l1(latitude1),l2(latitude2),lg1(longitude1),lg2(longitude2) are global variables 
//we send them as parameters to function dist() to calculte distance between two points with coordinates(l1,lg1)&(l2,lg2)
float l1=0, lg1=0,l2=0,lg2=0; 

//cal_distance is global variable that's priodically updated with total distance covered by user
float cal_distance=0;

// this function is called to calculate distance between last 2 points and update 'cal_distance'
//scenario of calling this function :
// 1) get coordinates of point from the gps 
// 2) update l2 & lg2 with the new coordinates just read from gps
// 3) call dist(l1,l2,lg1,lg2) function
// 4) the returned value is then added to cal_distance to update total distance

float dist(float lat1, float lat2, float lon1, float lon2)
{
    float d=0; //the returned value
    if (l1!=0 && lg1!=0)
    {
				float phi1 = lat1 * (pi/ 180); //  in radians
				float phi2 = lat2 * (pi / 180);
				float delta_phi = (lat2 - lat1) * (pi / 180);
				float delta_lamda = (lon2 - lon1) * (pi / 180);
				float a = (sin(delta_phi / 2) * sin(delta_phi / 2)) +
				cos(phi1) * cos(phi2) *sin(delta_lamda / 2) * sin(delta_lamda / 2);
				float c = 2 * atan2(sqrt(a), sqrt(1 - a));
				d = (R) * (c); // in metres
    }
    // here we put the values of l2 and lg2 in l1 and lg1 respectively so that
    // the next time we call this function it will calulate distance between the previous point and the 
    // point just read from gps 
    l1=l2;
    lg1=lg2;
    return d;
}
