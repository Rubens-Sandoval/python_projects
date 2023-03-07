import phonenumbers
from phonenumbers import geocoder

phone = input('Digite um telefone no formato: +5511940028922')

phone_number  = phonenumbers.parse(phone)

print(geocoder.description_for_number(phone_number, 'pt'))