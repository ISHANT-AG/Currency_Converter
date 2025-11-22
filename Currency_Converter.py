exchange_rates = {
    # Base Currency
    "USD": 1.0,
    # Major World Currencies
    "EUR": 0.869,
    "GBP": 0.763,
    "JPY": 156.56,
    "CHF": 0.809,
    "CAD": 1.410,
    "AUD": 1.549,
    "CNY": 7.109,
    # Asia & Middle East
    "AED": 3.673,
    "AFN": 65.84,
    "BDT": 122.51,
    "BHD": 0.376,
    "BND": 1.307,
    "HKD": 7.786,
    "IDR": 16720.91,
    "INR": 89.56,
    "IQD": 1309.76,
    "IRR": 42235.52,
    "ILS": 3.273,
    "JOD": 0.709,
    "KWD": 0.307,
    "KRW": 1471.50,
    "LKR": 307.79,
    "MYR": 4.148,
    "NZD": 1.783,
    "OMR": 0.385,
    "PHP": 58.82,
    "PKR": 281.45,
    "QAR": 3.640,
    "SAR": 3.750,
    "SGD": 1.307,
    "THB": 32.39,
    "TRY": 42.45,
    "TWD": 31.40,
    "VND": 26352.51,
    # Americas
    "ARS": 1423.26,
    "BRL": 5.391,
    "CLP": 938.80,
    "COP": 3801.35,
    "CRC": 500.86,
    "DOP": 63.54,
    "MXN": 18.46,
    "PEN": 3.388,
    # Europe (Non-Euro)
    "CZK": 21.07,
    "DKK": 6.492,
    "HUF": 333.13,
    "ISK": 127.78,
    "NOK": 10.25,
    "PLN": 3.686,
    "RON": 4.424,
    "RUB": 79.12,
    "SEK": 9.563,
    "UAH": 42.23,
    # Africa
    "DZD": 130.84,
    "EGP": 47.45,
    "GHS": 11.06,
    "KES": 129.37,
    "LYD": 5.46,
    "MAD": 9.296,
    "NGN": 1454.45,
    "ZAR": 17.37,
    "TND": 2.961,
    "UGX": 3634.42
}

def convert_currency(amount, from_currency, to_currency):
    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        raise ValueError("Invalid currency provided.")
    
    # Convert the amount to USD first (as USD is the base currency)
    amount_in_usd = amount / exchange_rates[from_currency]

    # Convert the USD amount to the target currency
    converted_amount = amount_in_usd * exchange_rates[to_currency]

    print(converted_amount)

# Get user inputs
while True:
    try:
        amount = float(input("Enter the amount to convert: "))
        break
    except ValueError:
        print("Invalid amount. Please enter a number.")

from_currency = input("Enter the currency to convert FROM (e.g., INR, USD): ").upper()
to_currency = input("Enter the currency to convert TO (e.g., USD, EUR): ").upper()

result = convert_currency(amount, from_currency, to_currency)