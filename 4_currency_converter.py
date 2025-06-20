# The_Currency_converter
USD, EUR, CAD = "USD" , 'EUR', 'CAD' 
currency_list=[USD, EUR, CAD]

def get_amount():
    try:
        amount=float(input("Enter the amount: "))
    except ValueError:
        print("Enter a valid amount: ")
        amount=get_amount()
    return amount

def get_currencies():
    #get the currencies 
    source_currency=input("Enter source currency (USD/EUR/CAD): ").strip().upper()
    target_currency=input("Enter target currency (USD/EUR/CAD): ").strip().upper()

    #validate the user input
    if ((source_currency not in currency_list) or (target_currency not in currency_list)):
        print("Currency not available! Enter Valid currency.\nEnter correct details to convert: ")
        currency_converter()
    
    return source_currency, target_currency


def currency_converter():
    while True:
        amount=get_amount()
        source_currency, target_currency=get_currencies()

        if source_currency==target_currency:
            print("Source and target currencies are the same!").lower()
            

        elif source_currency==USD:
            if target_currency==EUR:
                print(f"{amount} {USD} is equal {amount*0.88} {EUR}") #
            elif target_currency==CAD:
                print(f"{amount} {USD} is equal {amount*1.37} {CAD}")#

        elif source_currency==EUR:
            if target_currency==USD:
                print(f"{amount} {EUR} is equal {amount/0.88} {USD}") #
            elif target_currency==CAD:
                print(f"{amount} {EUR} is equal {amount*1.56} {CAD}")#

        elif source_currency==CAD:
            if target_currency==USD:
                print(f"{amount} {CAD} is equal {amount/1.37} {USD}")
            elif target_currency==EUR:
                print(f"{amount} {CAD} is equal {amount/1.56} {EUR}")

currency_converter()   
    
















#ask user for input
#validate input into float
#as user for source currency
#ask user for target currency
#convert