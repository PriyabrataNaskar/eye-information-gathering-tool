import ipinfo
import pprint

#API token from ipinfo
access_token = 'e5ec838e26c4c3'

handler = ipinfo.getHandler(access_token)

ip_address = input("Enter your value: ")

#getting details of that particular IP
details = handler.getDetails(ip_address)

#displaying data
print('###### LOCATION FOR IP %s TRACKED SUCCESSFULLY ######'  % (details.ip))
print('Country Code: %s' % (details.country))
print('Country Name: %s' % (details.country_name))
print('TimeZone: %s' % (details.timezone))
print('Region : %s' % (details.region))
