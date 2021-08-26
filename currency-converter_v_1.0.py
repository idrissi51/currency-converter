
import requests

# say Welcom
user_name = input("Whats Your name?: ").strip().capitalize()
print("Hello " + user_name + "\n Here you can convert your currency")
test = requests.get('https://api.exchangerate-api.com/v4/latest/USD').json()
test1 = test['rates']

# function for testing if the names of the currencys corrects


def testing():
    if F not in test1 or T not in test1:
        print("The currency name is incorrect")
        put()
    else:
        conv = realtimecurrencyconverter(
            'https://api.exchangerate-api.com/v4/latest/USD')
        print(conv.convert(F, T, M))
        again()


def put():
    global F, T, M
    F = input("From currency: ").upper().strip()
    T = input("To currency: ").strip().upper()
    M = int(input("amount: ").strip())
    testing()


def again():
    print("Do you want to Exit (y or n)")
    opt = input("=> ").strip().lower()
    if opt == "y":
        print("Good bye " + user_name)
    elif opt == "n":
        put()
    else:
        again()


class realtimecurrencyconverter():
    def __init__(self, url):
        self.data = requests.get(
            'https://api.exchangerate-api.com/v4/latest/USD').json()
        self.currencies = self.data["rates"]

    def convert(self, from_currency, to_currency, amount):
        if from_currency != "USD":
            amount = amount / self.currencies[from_currency]
        else:
            amount = amount * self.currencies[from_currency]
        amount = round(amount * self.currencies[to_currency], 4)
        return f"{M} {F} => {amount} {T}"


put()
