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
                    ComputeNetwork["BinarySubnetMask"] = SetBinaryAddresses(ComputeNetwork["SubnetMask"])
                    ComputeNetwork["BroadcastAddress"] = SetBroadcastAddress(ComputeNetwork["NetworkAddress"])
                    ComputeNetwork["BinaryBroadcastAddress"] = SetBinaryAddresses(ComputeNetwork["BroadcastAddress"])
                    ComputeNetwork["FirstHostsAddress"] = SetFirstHostAddress(ComputeNetwork["NetworkAddress"])
                    ComputeNetwork["BinaryHostsAddress"] = SetBinaryAddresses(ComputeNetwork["FirstHostsAddress"])
                    ComputeNetwork["MaxCountofHost"] = SetCountofHosts(ComputeNetwork["NetworkAddress"])
                    ComputeNetwork["BinaryMaxCountofHost"] = SetBinaryCountofHosts(ComputeNetwork["MaxCountofHost"])

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
            ipaddress.IPv4Network(IPtoCheck, False)
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

def SetBinaryAddresses(AnyAddress: str):
    TableofAnyAddress = AnyAddress.split(".")
    TableofAnyAddress = list(map(int, TableofAnyAddress))
    BinaryAddressTmp = [bin(TableofAnyAddress[i])[2:] for i in range(0, 4)]
    while '0' in BinaryAddressTmp:
        BinaryAddressTmp[BinaryAddressTmp.index("0")] = "00000000"
    while '1' in BinaryAddressTmp:
        BinaryAddressTmp[BinaryAddressTmp.index("1")] = "00000001"
    BinaryAddress = ".".join(BinaryAddressTmp)
    return BinaryAddress

def SetBroadcastAddress(NetworkAddress: str):
    Network = ipaddress.IPv4Network(NetworkAddress, False)
    BroadcastAddress = str(Network.broadcast_address)
    return BroadcastAddress

def SetFirstHostAddress(NetworkAddress: str):
    TableofHHosts = list(ipaddress.IPv4Network(NetworkAddress, False).hosts())
    return str(TableofHHosts[0])

def SetCountofHosts(NetworkAddress: str):
    TableofNetwork = NetworkAddress.split('/')
    ShortSubnetMask = int(TableofNetwork[1])
    CountofHosts = pow(2, 32 - ShortSubnetMask)
    return CountofHosts

def SetBinaryCountofHosts(CountofHosts: int):
    return bin(CountofHosts)[2:]

##Main function
Main()