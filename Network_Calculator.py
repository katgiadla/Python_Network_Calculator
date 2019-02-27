import ifaddr
import json
import ipaddress

ComputeNetwork = {
    "NetworkAddress": "",
    "ClassofNetwork": "",
    "SubnetMask": "",
    "BinarySubnetMask": "",
    "BroadcastAddress": "",
    "BinaryBroadcastAddress": "",
    "FirstHostsAddress": "",
    "BinaryHostsAddress": "",
    "MaxCountofHost": 0,
    "BinaryMaxCountofHost": "",
}

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
                    if UserChoice == 1:
                        ComputeNetwork["NetworkAddress"] = GetLocalIP()
                    else:
                        SettedUserIP = input("Entry your IP: ")
                        ComputeNetwork["NetworkAddress"] = GetUserIP(SettedUserIP)

                    ComputeNetwork["ClassofNetwork"] = DefinitionClassofNetwork(ComputeNetwork["NetworkAddress"])
                    ComputeNetwork["SubnetMask"] = ComputeSubnetMask(ComputeNetwork["NetworkAddress"])
                    ComputeNetwork["BinarySubnetMask"] = SetBinarySubnetMask(ComputeNetwork["SubnetMask"])
                    ComputeNetwork["BroadcastAddress"] = SetBroadcastAddress(ComputeNetwork["OnlyIP"], ComputeNetwork["SubnetMask"])

                    print(ComputeNetwork)

    return

def GetLocalIP():
    adapters = ifaddr.get_adapters()
    localIP = adapters[6].ips[1].ip + '/' + str(adapters[6].ips[1].network_prefix)
    return localIP

def GetUserIP(UserIP: str):
    IPtoCheck = UserIP
    while True:
        try:
            ipaddress.ip_network(IPtoCheck)
        except ValueError:
            IPtoCheck = input("Entry correct IP network address: ")
            continue
        break
    return IPtoCheck

def DefinitionClassofNetwork(IPtoCheck: str):
    TableofIPAdressWithSubnetMask = IPtoCheck.split("/")
    TableofIPAdress = TableofIPAdressWithSubnetMask[0].split(".")
    FirstPartofAddres = int(TableofIPAdress[0])
    if FirstPartofAddres >= 0 and FirstPartofAddres <= 127:
        ClassofNetwork = "A"
    elif FirstPartofAddres >= 128 and FirstPartofAddres <= 191:
        ClassofNetwork = "B"
    elif FirstPartofAddres >= 192 and FirstPartofAddres <= 223:
        ClassofNetwork = "C"
    elif FirstPartofAddres >= 224 and FirstPartofAddres <= 239:
        ClassofNetwork = "D"
    else:
        ClassofNetwork = "E"
    return ClassofNetwork

def ComputeSubnetMask(NetworkIP: str):
    interface = ipaddress.IPv4Interface(NetworkIP)
    NetworkIPWithMask = interface.with_netmask
    TableofNetwork = NetworkIPWithMask.split("/")
    SubnetMask = TableofNetwork[1]
    return SubnetMask

def SetBinarySubnetMask(SubnetMask: str):
    TableofSubnetMask = SubnetMask.split(".")
    TableofSubnetMask = list(map(int, TableofSubnetMask))
    BinarySubnetMaskTmp = [bin(TableofSubnetMask[i])[2:] for i in range(0,4)]
    while '0' in BinarySubnetMaskTmp:
        BinarySubnetMaskTmp[BinarySubnetMaskTmp.index("0")] = "00000000"
    BinarySubnetMask = ".".join(BinarySubnetMaskTmp)
    return BinarySubnetMask


def SetBroadcastAddress(NetworkAddress: str):
    Network = ipaddress.IPv4Network()
    BroadcastAddress = Network.broadcast_address
    return BroadcastAddress

##Main function
Main()