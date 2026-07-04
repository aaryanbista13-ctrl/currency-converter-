import os
import requests
import pandas as pd
def load_currency():
    if os.path.exists('currency.csv'):
        return pd.read_csv("currency.csv")
    else:
        return pd.DataFrame(columns=["Amount", "From_currency", "To_currency","Final_amount"])
def save_currency(df):
    df.to_csv("currency.csv",index=False)
def currency_converter(df):
    api_key="6221987e956799adb86e9bba"
    try:
        amount=float(input("Enter the amount of currency you want to convert:\n==> "))
    except ValueError:
        print("\nCurrency should be in number.\n")
        return(df)
    from_currency=input("Enter the currency you want to convert from(NPR,EUR,USD):\n==> ").strip().upper()
    to_currency=input("Enter the currency you want to convert to(NPR,EUR,USD):\n==> ").strip().upper()
    url=f"https://v6.exchangerate-api.com/v6/{api_key}/latest/USD"
    response=requests.get(url)
    if response.status_code != 200:
        print("\nSomething went wrong.")
        return(df)
    data=response.json()
    rates=data["conversion_rates"]
    if from_currency not in rates or to_currency not in rates:
        print("\nCurrency not found.")
        return(df)
    rate_from=rates[from_currency]
    final_amount=amount/rate_from
    rates_to=rates[to_currency]
    final_amount1=final_amount * rates_to
    print(f"\n The exchange rate of amount {amount} {from_currency} to {to_currency} = {final_amount1:.2f} {to_currency}")
    next_currency=pd.DataFrame([{
        "Amount":amount,
        "From_currency":from_currency,
        "To_currency":to_currency,
        "Final_amount":round(final_amount1,2)
    }])
    df=pd.concat([df,next_currency],ignore_index=True)
    save_currency(df)
    return df
def history(df):
    print("\nAll history.")
    if len(df)==0:
        print("\nNo currency found.")
        return(df)
    for index, row in df.iterrows():
        print(f"Converting {row['From_currency']} {row['Amount']}: to  {row['To_currency']} = {row['Final_amount']:.2f}")
df=load_currency()
while True:
    print("\n<<<<<<<<<<<<<Welcome-to-Currency-Converter>>>>>>>>>>>>>\n")
    print("1:Currency Converter:")
    print("2:All History:")
    print("3:Exit")
    choice=input("\nChoose your option:\n==> ")
    if choice=="1":
        df=currency_converter(df)
    elif choice=="2":
        df=history(df)
    elif choice=="3":
        print("\nThank you for using Currency Converter")
        break
    else:
        print("\nPlease enter a valid choice.")
