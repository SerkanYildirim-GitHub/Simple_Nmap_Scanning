# nmapscan organize tool v1.0 by s3rk4n https://github.com/SerkanYildirim-GitHub
# The purpose of this script to make practical nmap scans
# Get the IP range / IP address from a user input
# Select different Nmap scanning options from the given list
# Save the outputs to a directory/filename

import os

print() # prints a blank line at start
print("\t\tWelcome to Nmap Scan & Organizing Tool v1.0")
print("-"*50)
# get the IP address/range from a user input
ip_address = input("Type the IP address/range to scan: ")
print()

# Creating a Case Directory 
def case():
    case_dir = (f"Case_{ip_address}")
    check_dir = os.path.isdir(case_dir) # check if the directory already exist
    if not check_dir:
        os.mkdir(f"Case_{ip_address}")
    else:
        pass
# Selecting nmap option
def main():
    print("\t\tNmap Scan Selector")
    print("-"*50)
    print("\t\t1. Basic Scan\n\t\t2. Service and Version Detection\n\t\t3. Port Range Scan\n\t\t4. OS Detection Scan\n\t\t5. Host Discovery (Only port scan)\n\t\t6. NSE Scripts Scan\n\t\t7. Select Your Script\n\t\t8. Vulnerability Scan")
    tool_selection = input("Select the nmap scan type: ")
    if tool_selection == "1":
        basic()
    elif tool_selection == "2":
        sv()
    elif tool_selection == "3":
        port()
    elif tool_selection == "4":
        osscan()
    elif tool_selection == "5":
        pn()
    elif tool_selection == "6":
        sC()
    elif tool_selection == "7":
        selected()
    elif tool_selection == "8":
        vuln()
    else:
        print("Nice Try..!!! Scan Selections must be 1-5 ")
# Basic nmap Scan nmap <ip_address>    
def basic():
    print(f"basic nmap scan for {ip_address} is initializing")
    print()
    print("*"*50)
    os.system(f"nmap {ip_address} -oN Case_{ip_address}/basicscan.txt")
    print(f"scan result for {ip_address} is saved as basicscan.txt")

# Nmap Service and Version Detection nmap -sV <ip_address>
def sv():
    print()
    print("*"*50)
    os.system(f"nmap -sV {ip_address} -oN Case_{ip_address}/service_version.txt")
    print(f"scan result for {ip_address} is saved as service_version.txt")

# Nmap port range scan
def port():
    print()
    print("*"*50)
    port1 = input("type the beginning port: ")
    port2 = input("type the final port: ")
    port_range = (f"-p {port1}-{port2}")
    os.system(f"nmap {port_range} {ip_address} -oN Case_{ip_address}/portrange.txt")
    print(f"scanned port range results for {ip_address} is saved as portrange.txt")

# Nmap OS Detection    
def osscan():    
    print()
    print("*"*50)
    print("Warning: OS Detection Scan Needs Root Priviliges.")
    os.system(f"sudo nmap -O {ip_address} -oN Case_{ip_address}/osdetect.txt")
    print(f"scanned port range results for {ip_address} is saved as portrange.txt")

# Nmap Disable Host Discovery Scan
def pn():
    print()
    print("*"*50)
    os.system(f"sudo nmap -Pn {ip_address} -oN Case_{ip_address}/hostdiscovery.txt")    
    print(f"scanned port range results for {ip_address} is saved as hostdiscovery.txt")

# Nmap NSE Scripts Scan
def sC():
    print()
    print("*"*50)
    print("Warning: Script Scan Needs Root Priviliges.")
    os.system(f"sudo nmap -sC {ip_address} -oN Case_{ip_address}/scriptscan.txt")    
    print(f"scanned port range results for {ip_address} is saved as scriptscan.txt")

# Nmap Scan with a single script
def selected():    
    print()
    print("*"*50)
    print("Warning: Script Scan Needs Root Priviliges.")
    script_selection = input("which script you want to use: ")
    file_name = input("Type a file name to save as: ")
    os.system(f"sudo nmap --script \"{script_selection}\" {ip_address} -oN Case_{ip_address}/{file_name}")    
    print(f"scanned port range results for {ip_address} is saved as {file_name}")

# Nmap Vulnerability Scan
def vuln():
    print()
    print("*"*50)
    print("Warning: Vulnerability Scan Needs Root Priviliges.")
    os.system(f"sudo nmap -sV --script vulners {ip_address} -oN Case_{ip_address}/vulnerabilityscan.txt")    
    print(f"scanned port range results for {ip_address} is saved as vulnerabilityscan.txt")


# We might add more details later :) Planning to simplfy functions since I used same lines in most of them.  

if __name__ == "__main__":
    case()
    main()  
