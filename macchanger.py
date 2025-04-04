#!/usr/bin/env python3

import subprocess as sp

print("1 - eth0\n2 - wlan0\n3 - enp37s0")
inputt = int(input("Interface you want to change: "))
print('\n')

match inputt:
    case 1: interface = "eth0"
    case 2: interface = "wlan0"
    case 3: interface = "enp37s0"
    case _: 
        print("Please enter a valid input") 
        exit(1)

print("1 - New\n0 - Default")
ans = int(input("You want new or default: "))
if ans not in [0, 1]:
    print("Please enter valid input")
    exit(2)

a = f"ifconfig {interface} down"
c = f"ifconfig {interface} up"
default_mac = "2c:f0:5d:86:6e:28"

if ans == 1:
    print("\nNote: MAC address should be 12 hex characters (e.g. 0a:1b:2c:3d:4e:5f)\n")
    new_mac = input("Enter a MAC address: ")

    if len(new_mac) == 17 and new_mac.count(':') == 5:
        print("[+] Changing MAC address for", interface, "to", new_mac)
    else:
        print("[-] Invalid MAC address format")
        exit(2)

    sp.call(a, shell=True)
    sp.call(f"ifconfig {interface} hw ether {new_mac}", shell=True)
    sp.call(c, shell=True)

else:
    print("[+] Reverting MAC address for", interface, "to default:", default_mac)
    sp.call(a, shell=True)
    sp.call(f"ifconfig {interface} hw ether {default_mac}", shell=True)
    sp.call(c, shell=True)

sp.call("ifconfig", shell=True)
print("Note: To revert to the default MAC address, run the script again and choose option '0'")
