# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 150,
    "AMZN": 170
}

stock = input("Enter stock name (AAPL, TSLA, GOOGL, AMZN): ").upper()
quantity = int(input("Enter quantity: "))

if stock in stock_prices:
    total = stock_prices[stock] * quantity
    print(f"\nStock: {stock}")
    print(f"Quantity: {quantity}")
    print(f"Total Investment: ${total}")

    with open("investment.txt", "w") as file:
        file.write(f"Stock: {stock}\n")
        file.write(f"Quantity: {quantity}\n")
        file.write(f"Total Investment: ${total}\n")

    print("Result saved in investment.txt")
else:
    print("Invalid stock name!")
