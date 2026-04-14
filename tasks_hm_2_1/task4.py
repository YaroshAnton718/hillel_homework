print("Ця програма ціну товару із зазначеною знижкою.")

user_price = float(input("Введіть ціну товару без знижки: "))
discount = int(input("Введіть знижку (%): "))

price_with_discount = user_price * (1 - discount / 100)

print(f"\nЦіна зі знижкою: {price_with_discount}")