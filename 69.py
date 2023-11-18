pi = 3
denominator = 4
term = 1
for i in range(1, 15):
    pi += term
    denominator += 2 * i * (i + 1)
    term *= -1
print(f"Approximation {i}: {pi}")