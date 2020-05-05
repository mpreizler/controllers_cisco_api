Testing

Getting started with REST APIs with Cisco Controllers

The goals of this application are various. First is to show how simple it is to develop applications in python by using the REST API that Cisco controllers provides. Second, is to help each SE to underdstand how the programmability could be oriented to networking as well as using this for demo when you talk about APIs with Cisco Controllers. And finally, it can be used as a base for further interactions.

This script only use a couple of GET request.  However, once you understand how each of the controllers works, you can create options at your own.

Requirements

To use this application you will need:

Connectivity to Cisco sandbox and Meraki Cloud
Install and Setup: Python3.7
Clone the code to your local machine.
From MAC: 
$git clone https://github.com/mpreizler/controllers_cisco_api.git
$cd controllers_cisco_api 
$pip3 install requests
Run the program:
$python3.7 controllers_api_cisco.py


If you prefer VENV, setup Python Virtual Environment (requires Python 3.7)
python3.7 -m venv venv
source venv/bin/activate
pip3 install requests
Setup local environment variables for your Cisco API controllers.

To execute the script:

$python3.7 controllers_api_cisco.py

Notes:
If you have issues with some options for DNA, please try to change sandboxdnac2.cisco.com to sandboxdnac.cisco.com in urls.
Check first if sandboxsdwan.cisco.com if (always-on)is up.
