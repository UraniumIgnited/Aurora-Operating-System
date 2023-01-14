import os
import sys
import string
import random
import time
import shutil
import socket
from getpass import getpass

drive_letter = ""
counter = 0
running = True
host = []
__aurora_version__ = "0.0.1"

class Drive:
    class Operations:
        def AssignDriveLetter():
            drive_letter = random.choice(string.ascii_uppercase)
            drive_ = open("System12/Drive/drive_letter.system_requirements", "w")
            drive_.write(drive_letter)
            drive_.close()
            return drive_letter
        
        def FindDriveLetter():
            drive_ = open("System12/Drive/drive_letter.system_requirements", "r")
            drive_letter = drive_.read()
            drive_.close()
            return drive_letter
        
        def CalculateDriverLetter():
            if os.path.exists("System12/Drive/drive_letter.system_requirements"):
                drive_letter = Drive.Operations.FindDriveLetter()
            elif not os.path.exists("System12/Drive/drive_letter.system_requirements"):
                drive_letter = Drive.Operations.AssignDriveLetter()
            return drive_letter


class Host:
    def SystemInfo():
        global host
        host_ = open("System12/Host/host_section.system_requirements", "r")
        host = host_.read().splitlines()
        host_.close()

# Starting Operations
drive_letter = Drive.Operations.CalculateDriverLetter()

username = "ravin"
path = drive_letter + f":\\Users\\{username}\\Desktop"
end = ">"
sudo_password = "1234567890"
user_is_sudo = False


while running:
    zeno = input(path + end)

    if zeno == "aurora.system -stop" or zeno == "aurora.system -Stop" or zeno == "aurora.system -s" or zeno == "aurora.system -S":
        running = False

    elif zeno == "-help" or zeno == "--help" or zeno == "-h" or zeno == "--h" or zeno == "-H" or zeno == "--H":
        print("All the Commands are:\n\n")
        print("aurora.system -stop  ## Some versions of this command also work ")
        print("\nclear / cls  #'Clears the console'")
        print("\nipconfig / ifconfig  #'Allows a user to get information about the device'")
        print("\naurora.system --version  ## Some version of this command also work")
        print("\n--crash  #'Allows a user to crash the program' :Sudo Required:")
        print("\nsudo  #'This allows a user to get admin access'")
        print("\nsudo --change -p  #'This allows the default sudo password to be changed' :Sudo Requried:")
        print("\n\n")

    elif zeno == "clear" or zeno == "cls":
        if os.name == "nt":
            cls = "cls"
        elif os.name != "nt":
            cls = "clear"
        os.system(cls)

    elif zeno == "ipconfig" or zeno == "ifconfig":
        print("\nThis systems hostname and ip address:\n")
        if len(host) > 0:
            print("Hostname: " + host[0])
            print("\n")
            print("IP Address: " + host[1])
            print("\n\n")
        elif len(host) == 0:
            print("No Data Available\n")
    
    elif zeno == "aurora.system --version" or zeno == "aurora.system -version" or zeno == "aurora.system -v" or zeno == "aurora.system -V" or zeno == "aurora.system --v" or zeno == "aurora.system --V":
        print("\nAurora System  -|-  Version\n")
        print("Aurora Operating System Version:", __aurora_version__)
    
    elif zeno == "--crash" or zeno == "--Crash":
        if user_is_sudo:
            print("Crashing Operating System")
            print("\nPlease Note: System will not save anything")
            print("\n\nError Operating System has crashed, please restart system to continue using it")
            sys.exit()
        else:
            print("User requires Admin Permissions")
    
    elif zeno == "Sudo" or zeno == "sudo":
        if not user_is_sudo:
            user_given_sudo_password = getpass("Enter Sudo Password: ")
            if user_given_sudo_password == sudo_password:
                print("*** Password Accepted ***")
                user_is_sudo = True
            else:
                print("Password Incorrect")
        elif user_is_sudo:
            print("User is already Admin")

    elif zeno == "sudo --change -p":
        if user_is_sudo:
            print("Changing Sudo Password")
            sudo_password = input("Enter New Sudo Password: ")
            print("Sudo Password has been set to:", sudo_password)
        else:
            print("User requires Admin Permissions")
    
    elif zeno == "sudo -logout" or zeno == "sudo -Logout" or zeno == "Sudo -logout" or zeno == "Sudo -Logout":
        if user_is_sudo:
            print("User is no longer Admin")
            user_is_sudo = False
        elif not user_is_sudo:
            print("User was not Admin in the first place")