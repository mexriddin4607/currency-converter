def get_exchange_rate(rates, currency):
    
    for rate in rates:
        if rate["code"] == currency:
            return float(rate["cb_price"].replace(",", ""))
    return None


def display_available_currencies(rates):
    
    print("\nMavjud valyutalar:")
    available_currencies = [rate["code"] for rate in rates]
    print(", ".join(available_currencies))