x = float(input("Enter a number: "))
guess = x / 2
while True:
    new_guess = (guess + x / guess) / 2
    if abs(guess * guess - x) <= 1e-12:
        break
    guess = new_guess

print("The square root of", x, "is", guess)