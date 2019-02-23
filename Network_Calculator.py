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
                elif UserChoice == 1:
                    GetLocalIP()
                else:
                    print("Do something")
    return

def GetLocalIP():
    adapters = ifaddr.get_adapters()
    localIP = adapters[6].ips[1].ip + '/' + str(adapters[6].ips[1].network_prefix)
    return localIP

##Main function
Main()