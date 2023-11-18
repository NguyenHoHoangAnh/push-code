def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
for celsius in range(0, 101, 10):
    fahrenheit = celsius_to_fahrenheit(celsius)
    print(f"{celsius} độ C | {fahrenheit} độ F")