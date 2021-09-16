import ipinfo
import pprint

#API token from ipinfo
access_token = 'e5ec838e26c4c3'

handler = ipinfo.getHandler(access_token)

ip_address = input("Enter your value: ")

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
