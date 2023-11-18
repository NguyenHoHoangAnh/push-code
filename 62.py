print('Prices   | Discount| New prices')
print('---------------------------------')
Original = 4.95
while Original <= 24.95:
    Discount = Original * 0.60
    New_prices = Original - Discount
    print(' $%.2f''     |'  %Original, '$%.2f''     |' %Discount, '$%.2f' %New_prices )
    Original = Original + 5