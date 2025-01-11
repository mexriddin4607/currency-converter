
from exchange_rates import fetch_exchange_rates
from converter import convert_currency
from utils import get_exchange_rate, display_available_currencies

def main():
    print("Currency Converter dasturiga xush kelibsiz!")
    rates = fetch_exchange_rates()
    
    if not rates:
        print("Valyuta kurslarini olishda xatolik yuz berdi.")
        return

    display_available_currencies(rates)

    while True:
        try:
            amount = float(input("\nKonvertatsiya qilinadigan summani kiriting: "))
            from_currency = input("Qaysi valyutadan konvertatsiya qilmoqchisiz (masalan, USD): ").upper()
            to_currency = input("Qaysi valyutaga konvertatsiya qilmoqchisiz (masalan, UZS): ").upper()

            from_rate = get_exchange_rate(rates, from_currency)
            to_rate = get_exchange_rate(rates, to_currency)

            if from_rate is None:
                print(f"Xatolik: {from_currency} valyutasi topilmadi!")
                continue
            if to_rate is None:
                print(f"Xatolik: {to_currency} valyutasi topilmadi!")
                continue

            result = convert_currency(amount, from_rate, to_rate)
            print(f"\nNatija: {amount} {from_currency} = {result:.2f} {to_currency}")

            another = input("\nYana konvertatsiya qilasizmi? (ha/yo'q): ").lower()
            if another != "ha":
                print("Dasturdan foydalanganingiz uchun rahmat!")
                break

        except ValueError:
            print("Iltimos, to'g'ri son kiriting.")


if __name__ == "__main__":
    main()