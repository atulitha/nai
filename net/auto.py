#!/usr/bin/env python
from netmiko import SSHDetect, Netmiko
from getpass import getpass
import codecs
import csv

def write(device):
    with open('devicelist.csv', mode='w', encoding='utf-8-sig') as employee_file:
        employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
        employee_writer.writerow(device)
def writetxt(data):
    with open('result.txt', mode='a+',encoding = 'utf-8-sig') as f:
        f.write(data)
        

def conn(device):
    
##    guesser = SSHDetect(**device)
##    best_match = guesser.autodetect()
##    print(best_match)  # Name of the best device_type to use further
##    print(guesser.potential_matches)  # Dictionary of the whole matching result
    
        device["device_type"] = "linux"
        connection = Netmiko(**device)
        print(connection.find_prompt())
        out = connection.send_command("man man",expect_string="MAN")
        print(out)
        writetxt(out)
        return device
    
ip = "192.168.2.10"
user = "atulitha"
if user != "root":
    device = {
        "device_type": "autodetect",
        "host": ip,
        "username": user,
        "password": "root",}
    write (conn(device))
else:
    print("cannot login using root")


