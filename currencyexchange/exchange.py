from json import load
with open("C:/Users/Arathy/PycharmProjects/pythonProjectnew/currencyexchange/db.json") as f:
    data=load(f)
rates=data.get("conversion_rates")
amount=int(input("enter the amount>"))
fromCurrencyCode=input("enter source currency code>")
toCurrencyCode=input("enter source currency code>")

rate_fromCurrencycode=rates.get(fromCurrencyCode)
rate_toCurrencyCode=rates.get(toCurrencyCode)

result=(amount/rate_fromCurrencycode)*rate_toCurrencyCode
print(result)