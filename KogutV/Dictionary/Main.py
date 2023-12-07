from Currency import *

currencies = {
    'us': Currency('US Dollar'),
    'ca': Currency('Canadian Dollar'),
    'gb': Currency('Pound Sterling'),
    'eu': Currency('Euro'),
}

print("Currencies:")
for country_code, currency_obj in currencies.items():
    print(f"{country_code.upper()}: {currency_obj.full_name}")

country_code = 'us'
if country_code in currencies:
    print(f"Currency for {country_code.upper()}: {currencies[country_code].full_name}")
else:
    print(f"State with code {country_code.upper()} is not found in the dictionary.")

country_code = 'ca'
new_currency_name = '(CAD)'
if country_code in currencies:
    currencies[country_code].full_name = new_currency_name
    print(f"New name for {country_code.upper()}: {currencies[country_code].full_name}")
else:
    print(f"State with code {country_code.upper()} is not found in the dictionary.")

country_code = 'gb'
if country_code in currencies:
    del currencies[country_code]
    print(f"State with code {country_code.upper()} and its currency were deleted.")
else:
    print(f"State with code {country_code.upper()} is not found in the dictionary.")

