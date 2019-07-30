
#! /usr/bin/env python
"""
A demo to interact with DNA Center and Meraki Cloud
Author: Mariano Preizler <mpreizle@cisco.com>

controllers_api.py
Illustrate the following concepts:
- Understanding REST API with DNA Center and Meraki Dashboard
"""

__author__ = "Mariano Preizler"
__author_email__ = "mpreizle@cisco.com"
__copyright__ = "Copyright (c) 2019 Cisco Systems, Inc."

# importing some important libraries
import time
import requests
import json
import urllib3
from requests.auth import HTTPBasicAuth

# url for DNA-C.  See DNA center API docs for more information.
url = "https://sandboxdnac2.cisco.com:443/dna/system/api/v1/auth/token"
url1 = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/network-device"
url2 = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/discovery/count"
url3 = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/topology/vlan/vlan-names"
url4 = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/topology/physical-topology"
url5 = "https://sandboxdnac2.cisco.com:443/dna/intent/api/v1/site-health?timestamp=<1000>"
url6 = "https://sandboxdnac2.cisco.com:443/dna/system/api/v1/site"

# url for meraki. See Meraki API docs for more information.
urlm1 = "https://dashboard.meraki.com/api/v0/organizations"
urlm2 = "https://dashboard.meraki.com/api/v0/organizations/681155/networks"
urlm3 = "https://dashboard.meraki.com/api/v0/organizations/865776/networks"
urlm4 = "https://dashboard.meraki.com/api/v0/organizations/52636/networks"
urlm5 = "https://dashboard.meraki.com/api/v0/organizations/549236/networks"
urlm22 = "https://dashboard.meraki.com/api/v0/organizations/681155/inventory"
urlm33 = "https://dashboard.meraki.com/api/v0/organizations/865776/inventory"
urlm44 = "https://dashboard.meraki.com/api/v0/organizations/52636/inventory"
urlm55 = "https://dashboard.meraki.com/api/v0/organizations/549236/inventory"

# headers for DNA Center
headers = {
    'cache-control': "no-cache",
    'Postman-Token': "e4151c25-42cf-42a9-82b4-a23e405c02be",
    'Content-Type': "application/json"
}
headers2 = {
    'content-type': "application/json",
    'x-auth-token': ""
}

# header for Meraki
headers3 = {
    'X-Cisco-Meraki-API-Key': "6bec40cf957de430a6f1f2baa056b99a4fac9ea0",
    'User-Agent': "PostmanRuntime/7.15.2",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Postman-Token': "fe649f0a-62ec-4f2e-851c-0a3c5a135b71,40749cd4-ed22-465c-90dc-f7bdd0ac6d4a",
    'Accept-Encoding': "gzip, deflate",
    'Referer': "https://api.meraki.com/api/v0/organizations",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
}

params = {
    '__runsync': "false",
    '__timeout': "30",
    '__persistbapioutput': "true"
}

# This function check status code returned


def get_status_code(x):
    print("You received this status code for your token authentication request: {}\n".format(x))
    if x == 400:
        print(status_code)
        print("Your access received a Bad Request")

    elif x == 401:
        print(status_code)
        print("Your access has been denied")

    elif x == 200:
        print("you have been successfully authenticated!!!\n")
    else:
        print("This error has been received:{}".format(status_code))
    return()

# This function allows to select with platform you would like to work


def select_controller():
    print("\n")
    print('\033[0;36;40m"Welcome to network programmability software to interact with CISCO controllers"')
    print("\nPlease select the platform you are interested in:\n")
    print("1: Cisco DNA Center\n")
    print("2: Cisco Meraki Cloud\n")
    a = input()
    return(a)

# This function allows to select different options for DNA Center API REST


def get_option():
    print("\nPlease select your option:\n\n")
    print("1: View all your network devices\n")
    print("2: Get count of all discovery jobs\n")
    print("3: Get Vlans details\n")
    print("4: Get Physical Topology\n")
    print("5: View Sites\n")
    print("6: Create a new site\n")
    r = input()
    return(r)

# This function allows to select different options for Meraki API REST


def get_option2():
    print("\nPlease select your option:\n\n")
    print("1: View all your organizations\n")
    print("2: List the networks of your Loyoli organization\n")
    print("3: List the networks of your Cisco Live US 201 organization\n")
    print("4: List the networks of your Forest City - Other organization\n")
    print("5: List the networks of your DevNet Sandbox organization\n")
    print("6: List inventory detail for specific organization\n")
    r = input()
    return(r)

# This funtion prints inventory for specific organization ID for Meraki


def print_meraki_inventory(inv_dict):
    for device in inv_dict:
        print("   Model {}".format(device["model"]))
        print("   Public IP: {}".format(device["publicIp"]))
        print("   Mac: {}".format(device["mac"]))
        print("   Serial: {}".format(device["serial"]))
        print("   Network ID: {}".format(device["networkId"]))
        print("")
        print("Press ENTER to see the next platform\n")
        input()
    return


def meraki_detail(inv_dict, org):
    print("Information for {} organization\n".format(org))
    total = 0
    count_mv71 = 0
    count_mv21 = 0
    count_mv12 = 0
    count_mv12we = 0
    count_mr84 = 0
    count_mr62 = 0
    count_mr53 = 0
    count_mr52 = 0
    count_mr42 = 0
    count_mr34 = 0
    count_mr33 = 0
    count_mr24 = 0
    count_mr18 = 0
    count_mr12 = 0
    count_mr32 = 0
    count_mrh30 = 0
    count_outdoor = 0
    count_ms225_24p = 0
    count_ms220_8p = 0
    count_ms220_8 = 0
    count_ms120_8fp = 0
    count_mc74 = 0
    count_mx250 = 0
    count_mx84 = 0
    count_mx67 = 0
    count_mx65 = 0
    count_mx65w = 0
    count_mx64 = 0
    for device in inv_dict:
        total = total + 1
        if device["model"] == 'MR84':
            count_mr84 = count_mr84 + 1
        elif device["model"] == 'MR62':
            count_mr62 = count_mr62 + 1
        elif device["model"] == 'MR53':
            count_mr53 = count_mr53 + 1
        elif device["model"] == 'MR52':
            count_mr52 = count_mr52 + 1
        elif device["model"] == 'MR42':
            count_mr42 = count_mr42 + 1
        elif device["model"] == 'MR34':
            count_mr34 = count_mr34 + 1
        elif device["model"] == 'MR33':
            count_mr33 = count_mr33 + 1
        elif device["model"] == 'MR32':
            count_mr32 = count_mr32 + 1
        elif device["model"] == 'MRH30':
            count_mrh30 = count_mrh30 + 1
        elif device["model"] == 'MR24':
            count_mr24 = count_mr24 + 1
        elif device["model"] == 'MR18':
            count_mr18 = count_mr18 + 1
        elif device["model"] == 'MR12':
            count_mr12 = count_mr12 + 1
        elif device["model"] == 'Outdoor':
            count_outdoor = count_outdoor + 1
        elif device["model"] == 'MV71':
            count_mv71 = count_mv71 + 1
        elif device["model"] == 'MV21':
            count_mv21 = count_mv21 + 1
        elif device["model"] == 'MV12W':
            count_mv12 = count_mv12 + 1
        elif device["model"] == 'MV12WE':
            count_mv12we = count_mv12we + 1
        elif device["model"] == 'MS225-24P':
            count_ms225_24p = count_ms225_24p + 1
        elif device["model"] == 'MS220-8P':
            count_ms220_8p = count_ms220_8p + 1
        elif device["model"] == 'MS220-8':
            count_ms220_8 = count_ms220_8 + 1
        elif device["model"] == 'MS120-8FP':
            count_ms120_8fp = count_ms120_8fp + 1
        elif device["model"] == 'MC74':
            count_mc74 = count_mc74 + 1
        elif device["model"] == 'MX250':
            count_mx250 = count_mx250 + 1
        elif device["model"] == 'MX84':
            count_mx84 = count_mx84 + 1
        elif device["model"] == 'MX67':
            count_mx67 = count_mx67 + 1
        elif device["model"] == 'MX65':
            count_mx65 = count_mx65 + 1
        elif device["model"] == 'MX65W':
            count_mx65w = count_mx65w + 1
        elif device["model"] == 'MX64':
            count_mx64 = count_mx64 + 1
    print("There are a total of {} equipments in this organization\n".format(total))
    print("{} MV71 cameras in your organization\n".format(count_mv71))
    print("{} MV21 cameras in your organization\n".format(count_mv21))
    print("{} MV12W cameras in your organization\n".format(count_mv12))
    print("{} MV12WE cameras in your organization\n".format(count_mv12we))
    print("{} MR84 wireless access points in your organization\n".format(count_mr84))
    print("{} MR62 wireless access points in your organization\n".format(count_mr62))
    print("{} MR53 wireless access points in your organization\n".format(count_mr53))
    print("{} MR52 wireless access points in your organization\n".format(count_mr52))
    print("{} MR42 wireless access points in your organization\n".format(count_mr42))
    print("{} MR34 wireless access points in your organization\n".format(count_mr34))
    print("{} MR33 wireless access points in your organization\n".format(count_mr33))
    print("{} MR32 wireless access points in your organization\n".format(count_mr32))
    print("{} MRH30 wireless access points in your organization\n".format(count_mrh30))
    print("{} MR24 wireless access points in your organization\n".format(count_mr24))
    print("{} MR18 wireless access points in your organization\n".format(count_mr18))
    print("{} MR12 wireless access points in your organization\n".format(count_mr12))
    print("{} Outdoor wireless access points in your organization\n".format(count_outdoor))
    print("{} MS225-24P switches in your organization\n".format(count_ms225_24p))
    print("{} MS220-8P switches in your organization\n".format(count_ms220_8p))
    print("{} MS220-8 switches in your organization\n".format(count_ms220_8))
    print("{} MS120-8FP switches in your organization\n".format(count_ms120_8fp))
    print("{} MC74 voice phone in your organization\n".format(count_mc74))
    print("{} MX250 routers in your organization\n".format(count_mx250))
    print("{} MX84 routers in your organization\n".format(count_mx84))
    print("{} MX67 routers in your organization\n".format(count_mx67))
    print("{} MX65 routers in your organization\n".format(count_mx65))
    print("{} MX65W routers in your organization\n".format(count_mx65w))
    print("{} MX64 routers in your organization\n".format(count_mx64))
    return
# main function to interact with DNA Center


def dna():

    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

    print('"Welcome to Cisco DNA Center Platform API Programmability"')
    print("\nPress ENTER to connect to our Cisco DNA Center \n")
    input()
    print('Connecting to Cisco DNA Center...\n')

    # To get the token you need first to POST user and password
    response = requests.request("POST", url, auth=HTTPBasicAuth(
        'devnetuser', 'Cisco123!'), headers=headers)
    status_code = response.status_code
    get_status_code(status_code)

    mytoken = response.json()["Token"]

    print("For your reference, this is your token for future interactions:\n")
    print(mytoken)
    print("\nPress ENTER to continue\n")
    input()

    headers2["x-auth-token"] = mytoken
    answer = 'n'
    while answer != 'y':
        selection = get_option()

        print("\nYou selected option: {}\n".format(selection))

        print("\nLooking for your selection.  Please wait...\n\n")
        time.sleep(1)
        if selection == '2':
            response2 = requests.get(url2, headers=headers2, verify=False)
            mydata = response2.json()["response"]
            print("\nThe count of all discovery option are {}".format(mydata))
            print("\nPress ENTER to continue\n")
            input()
        elif selection == '1':
            response2 = requests.request("GET", url1, headers=headers2, verify=False)
            # response2 body is in json() format.
            mydata = response2.json()["response"]
            # mydata is now a dictionary in python.
            # response2.json() is like json.loads(response2.text)
            print(mydata)
            print("\nLet's print out in a friendly fashion\n")
            print("\nPress ENTER to continue\n")
            input()
            # we work with a simple python dictionary
            for device in mydata:
                print("{} in family {}".format(device["hostname"], device["family"]))
                print("   Management IP: {}".format(device["managementIpAddress"]))
                print("   Role: {}".format(device["role"]))
                print("   Platform Type: {}".format(device["platformId"]))
                print("   Software Version: {}".format(device["softwareVersion"]))
                print("")
                print("Press ENTER to see the next platform\n")
                input()
        elif selection == '3':
            response2 = requests.request("GET", url3, headers=headers2, verify=False)
            mydata = response2.json()["response"]
            print(mydata)
            print("\nPress ENTER to continue\n")
            input()
        elif selection == '4':
            # we work with a list that contains dictionaries
            response2 = requests.request("GET", url4, headers=headers2, verify=False)
            mydata = response2.json()["response"]
            print(mydata)
            print("\nLet's print out in a friendly fashion\n")
            print("\nPress ENTER to continue\n")
            input()
            leng = len(mydata["nodes"])
            i = 0
            # Due to mydata is a list, I need to go for each item (dict) of the list
            while i < leng:
                print("\nThis platform:\n")
                print(mydata["nodes"][i])
                print("\nis connected to this platform\n")
                print(mydata["nodes"][i+1])
                print("\nPress ENTER to see the neigbhor platform\n")
                input()
                i = i+1
                if i == leng-1:
                    break
        elif selection == '6':
            # analizar como poner un POST para agregar un nuevo dispositivo
            response2 = requests.request("POST", url6, headers=headers2, param=params,
                                         data=json.dumps(mynewsite), verify=False)
            print(response2.status_code)
            mydata = response2.json()
            print(mydata)
            print("\nPress ENTER to continue\n")
            input()
        elif selection == '5':
            response2 = requests.request("GET", url5, headers=headers2, verify=False)
            print(response2.status_code)
            mydata = response2.json()
            print(mydata)
            print("\nPress ENTER to continue\n")
            input()
        else:
            print("You did not select a correct number option\n")
        print("\nWould you like to exit from Cisco DNA Center (y)?\n")
        answer = input()
    print("\nThanks your using API with our Cisco DNA Center\n")
    return()

# main function to interact with Meraki Cloud


def meraki():
    print('\033[0;31;40m"Welcome to Meraki Platform API Programmability"')
    print("\nPress ENTER to connect to our Meraki platform\n")
    input()
    print('Connecting to Meraki cloud...\n')
    response = requests.request("GET", urlm1, headers=headers3)
    status_code = response.status_code
    get_status_code(status_code)
    answer = 'n'
    while answer != 'y':
        selection = get_option2()
        print("\nYou selected option: {}\n".format(selection))
        print("\nLooking for your selection.  Please wait...\n\n")
        time.sleep(1)
        if selection == '1':
            response = requests.request("GET", urlm1, headers=headers3)
            print(response.text)
        elif selection == '2':
            response = requests.request("GET", urlm2, headers=headers3)
            print(response.text)
        elif selection == '3':
            response = requests.request("GET", urlm3, headers=headers3)
            print(response.text)
        elif selection == '4':
            response = requests.request("GET", urlm4, headers=headers3)
            print(response.text)
        elif selection == '5':
            response = requests.request("GET", urlm5, headers=headers3)
            print(response.text)
        elif selection == '6':
            print("Please select your organization to list the inventory\n")
            print("a: Lyoli")
            print("b: Cisco Live US 2019")
            print("c: Forest City - Other")
            print("d: DevNet Sandbox")
            w = input()
            if w == 'a':
                response = requests.request("GET", urlm22, headers=headers3)
                # print(response.text)
                print("\n\n")
                response2 = response.json()
                meraki_detail(response2, "Lyoli")
                print("Press ENTER to see the list of inventory\n")
                input()
                print_meraki_inventory(response2)
            elif w == 'b':
                response = requests.request("GET", urlm33, headers=headers3)
                # print(response.text)
                print("\n\n")
                response2 = response.json()
                meraki_detail(response2, "Cisco Live US 201")
                print("Press ENTER to see the list of inventory\n")
                input()
                print_meraki_inventory(response2)
            elif w == 'c':
                response = requests.request("GET", urlm44, headers=headers3)
                # print(response.text)
                print("\n\n")
                response2 = response.json()
                meraki_detail(response2, "Forest City - Other")
                print("Press ENTER to see the list of inventory\n")
                input()
                print_meraki_inventory(response2)
            elif w == 'd':
                response = requests.request("GET", urlm55, headers=headers3)
                # print(response.text)
                print("\n\n")
                response2 = response.json()
                meraki_detail(response2, "Devnet Sandbox")
                print("Press ENTER to see the list of inventory\n")
                input()
                print_meraki_inventory(response2)

        else:
            print("You did not select a correct number option\n")

        print("\nWould you like to exit from Meraki (y)?\n")
        answer = input()
    print("\nThanks your using API with our Meraki cloud\n")
    return()


# Entry point for program
if __name__ == '__main__':
    answer = "n"
    while answer == "n":
        seleccion = select_controller()
        if seleccion == "1":
            dna()
        elif seleccion == "2":
            meraki()
        print("\nWould you like to exit from network programmability software (y)?\n")
        answer = input()
    print("\nThanks for using our controllers with REST API\n")
