#!/bin/bash
import optparse
from subprocess import *
import subprocess as sp



print("1- eth0\n2- wlan0")
inputt = int(input("Interface you want to change: "))
print('\n')
match inputt:
    case 1: interface = "eth0"
    case 2:interface = "wlan0"
    case _: print("Please enter the valid input"); exit(1)


print("1 - New\n0 - Default")
ans = int(input("You want new or default:"))
if ans == 1 or ans == 0:
    pass
else:
    print("Please enter valid input")
    exit(2)
a = "ifconfig eth0 down"
c = "ifconfig eth0 up"
two = "2c:f0:5d:86:6e:28"


if ans == 1:
    print("\n")
    print("Note: MAC address should of 12 characters pair of 2 each should be separed by semicolon ( : )")
    print("Eg. 0a:1b:2c:3d:4e:5f\n")
    new_mac = input("Enter a mac address: ")
    length = len(new_mac)
    couunt = new_mac.count(':')

    if length == 17 and couunt == 5:
        print("done")

    else:
        print("Enter valid MAC address")
        exit(2)
    print("[+] Changing MAC address for ", interface, "  to ", new_mac)
    print('\n')
    sp.call(a, shell=True)
    sp.call("ifconfig " +interface+ " hw ether " + new_mac, shell=True)
    sp.call(c, shell=True)


elif ans == 0:
    print("[+] Changing MAC address for",interface, "to", two)
    print('\n')
    sp.call(a, shell=True)
    sp.call("ifconfig " +interface+ " hw ether " + two, shell=True)
    sp.call(c, shell=True)


else:
    print("[+] Changing MAC address for ", interface, "  to ", two)
    print('\n')
    sp.call(a, shell=True)
    sp.call("ifconfig " +interface+ " hw ether " + two, shell=True)
    sp.call(c, shell=True)

sp.call("ifconfig",shell=True)

print("Note: If you want the default mac address run this code again and select '0' for Default")

