Getting started with REST APIs with Cisco Controllers

The goals of this application are various. First is to show how simple it is to develop applications in python by using the REST API that Cisco controllers provides, learning python as well. Second, is to help each SE to underdstand how the programmability could be oriented to networking using this for demos. And finally, it can be used as a base for further interactions.

This script only use a couple of GET request.  However, once you understand how each of the controllers works, you can create options at your own.

Requirements
To use this application you will need:

Python 3.7
Access to Cisco sandbox
Install and Setup: Python3.7
Clone the code to your local machine.
From MAC type from terminal: git clone https://github.com/mpreizler/controllers_cisco_api.git
cd controllers_cisco_api 
Setup Python Virtual Environment (requires Python 3.7)

python3.7 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Setup local environment variables for your Cisco API controllers.

To execute the script:

$python3.7 controllers_api_cisco.py

