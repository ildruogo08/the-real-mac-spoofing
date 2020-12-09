import os
from randmac import RandMac

print("|\  /|   / \    ___")
print("| \/ |  /___\  |     ")
print("|    | |     | |    ")
print("|    | |     | |___   ")      

new_mac = RandMac()
try:
    print("what is the name of your iface?")
    iface = input(">")
    os.system("sudo ip link set dev " + iface + " down")
    os.system("sudo ip link set dev " + iface + " address " + new_mac)
    os.system("sudo ip link set dev " + iface + " up") 
except:
    print("[+]I am changing your mac address")
    print("[-]Your mac address is not anonymous")
print("[*]Your mac now is:" + str(new_mac))
print("[+]I am changing your mac address")
print("[+]Your mac address is now anonymous")
