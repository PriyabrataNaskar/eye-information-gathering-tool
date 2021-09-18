import ipinfo
import pprint
import socket
import whois

VER = "0.2"

def banner():

    print('Welcome to: ')
    logo = """
       ███████╗██╗   ██╗███████╗
       ██╔════╝╚██╗ ██╔╝██╔════╝
       █████╗   ╚████╔╝ █████╗  
       ██╔══╝    ╚██╔╝  ██╔══╝  
       ███████╗   ██║   ███████╗
       ╚══════╝   ╚═╝   ╚══════╝
    """
    
    #print(logo.format(VER,colored(getpass.getuser(), 'red', attrs=['bold'])))
    print(logo)
    #print('EYE is an Information Gathering Tool for Ethical Hackers')
    
def findLocation():

    #API token from ipinfo
    access_token = 'e5ec838e26c4c3'

    handler = ipinfo.getHandler(access_token)

    ip_address = input("Enter an IP to trace address (e.g:2409:4060:e82:6d43:a1fc:9657:82fe:43e9): ")

    #ip_address = '2402:3a80:1968:eb17:1864:4daa:c856:8798'

    #getting details of that particular IP
    details = handler.getDetails(ip_address)

    #displaying data
    print('###### LOCATION FOR IP %s TRACKED SUCCESSFULLY ######'  % (details.ip))
    print('Country Code: %s' % (details.country))
    print('Organisation Details: %s' % (details.org))
    print('Country Name: %s' % (details.country_name))
    print('TimeZone: %s' % (details.timezone))
    print('Region : %s' % (details.region))
    
def reverseLookUp():
    an_address = input("Enter an IP (e.g: 127.0.0.1): ")
    domain_name = socket.gethostbyaddr(an_address)[0]
    print(domain_name)

def viewWebsiteData():
    websiteName = input("Enter a website (e.g: www.google.com): ")
    w = whois.whois(websiteName)
    print(w.text)

def driverFunction():
    banner()
    choice = int(input('Press 1. to FIND LOCATION of an IP \nPress 2. to perform REVERSE DNS LOOKUP \nPress 3. to gather Website Information\nPress 4. to exit\n'))
    if choice == 1:
        findLocation()
    elif choice == 2:
        reverseLookUp()
    elif choice == 3:
        viewWebsiteData()
    elif choice == 4:
        return
        
driverFunction()
