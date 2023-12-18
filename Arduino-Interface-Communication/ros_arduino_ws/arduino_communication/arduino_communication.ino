/* This code will subscribe to the topic "information",
 * then it will read messages from this topic. 
 * The message is an integer. It will mulitply the integer by 2,
 * and then it will send back (publish) the result to the topic called "info_back"
 */

#include <ros.h>
#include <std_msgs/Int32.h>

// Node handle
ros::NodeHandle nh;

// This message is sent back
std_msgs::Int32 outputMessage;

// Publisher, similar in python first we specify the topic name nd then the message
ros::Publisher pub("info_back", &outputMessage);

/* This is the callbackFunction for our subscriber when the message is
 * received, this funciton will be called this function will simply 
 * multiply inputMessage.data by 2 and publish the result
 */ 

void callbackFunction(const std_msgs::Int32 &inputMessage) {
  outputMessage.data = 2*inputMessage.data;
  pub.publish(&outputMessage);
}

// Subscriber
ros::Subscriber<std_msgs::Int32>sub("information", &callbackFunction);

void setup() {
  // put your setup code here, to run once:
  nh.initNode();
  nh.advertise(pub);
  nh.subscribe(sub);
}

void loop() {
  // put your main code here, to run repeatedly:
  nh.spinOnce();
  delay(1);
}
