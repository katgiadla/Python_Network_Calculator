import socket
import ifaddr

def Main():
    StartOption = True
    while StartOption == True:
        print("Choose, what want you to do?")
        print("\n1. Compute network parametrs of local IP "
              "\n2. Entry and compute network parametrs"
              "\n3. Exit ")
        strChoice = input("Your decision: ")
        if strChoice.isdigit() == False:
            print("\nPlease choose 1, 2 or 3")
            continue
        else:
            UserChoice = int(strChoice)
            if UserChoice not in [1, 2, 3]:
                print("\nPlease choose 1, 2 or 3")
            else:
                if UserChoice == 3:
                    exit()
                else:
                    print("Let's do!")
                    break
    return

adapters = ifaddr.get_adapters()
for adapter in adapters:
    print("IPs of network adapter " + adapter.nice_name)
    for ip in adapter.ips:
        print("   %s/%s" % (ip.ip, ip.network_prefix))

# Main()