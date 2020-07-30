# phone number info using python

import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder

# enter phone number with country code.
phone_num=phonenumbers.parse("+917888470956")

# this will print the country name
print(geocoder.description_for_number(phone_num,'en'))

# this will print service provider name
print(carrier.name_for_number(phone_num,'en'))
