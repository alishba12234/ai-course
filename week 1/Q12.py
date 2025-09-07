# Currency Converter (USD to PKR)
# Fixed exchange rate 
exchange_rate = 300  
# Input amount in USD
usd = float(input("Enter amount in USD: "))

# Convert to PKR
pkr = usd * exchange_rate

# Display result
print(f"\n{usd} USD = {pkr} PKR")
