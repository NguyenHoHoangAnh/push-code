line = input("Enter 8 bits: ")
while line != "":
    if line.count("0") + line.count("1") != 8 or len(line) != 8:
        print("That wasn't 8 bits... Try again.")
    else:
        ones = line.count("1")
        if ones % 2 == 0:
            print("The parity bit should be 0.")
        else:
            print("The parity bit should be 1.")
    line = input("Enter 8 bits: ")