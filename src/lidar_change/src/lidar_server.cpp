#include"ros/ros.h"
#include"lidar_change/lidar.h"
#include<curl/curl.h>
#include<iostream>
using namespace std;

bool change(lidar_change::lidar::Request &request,lidar_change::lidar::Response &response){

    CURL *curl;
    CURLcode res;
    curl = curl_easy_init();
    if(curl) {
        curl_easy_setopt(curl, CURLOPT_CUSTOMREQUEST, "POST");
        curl_easy_setopt(curl, CURLOPT_URL, "http://192.168.1.201/pandar.cgi?action=set&object=lidar_data&key=lidar_range");
        curl_easy_setopt(curl, CURLOPT_FOLLOWLOCATION, 1L);
        curl_easy_setopt(curl, CURLOPT_DEFAULT_PROTOCOL, "https");
        struct curl_slist *headers = NULL;
        headers = curl_slist_append(headers, "Content-Type: application/json");
        curl_easy_setopt(curl, CURLOPT_HTTPHEADER, headers);
        string from = to_string(request.num1);
        string to = to_string(request.num2);
        string str = "{\"angle_setting_method\":0,\"lidar_range\":[" + from + "," + to + "]}";
        const char *data = str.c_str();
        curl_easy_setopt(curl, CURLOPT_POSTFIELDS, data);
        res = curl_easy_perform(curl);
    }
    curl_easy_cleanup(curl);
    string str = "修改成功";
    response.result = str;

    return true;
}

int main(int argc, char *argv[])
{
    setlocale(LC_ALL,"");
    ros::init(argc,argv,"server");

    ros::NodeHandle nh;
    ros::ServiceServer server = nh.advertiseService("changes",change);

    ros::spin();

    return 0;
}
