n=float(input("Enter a frequency (Hz): "))
if n==261.63:
    print("This is C4")
elif n==293.66:
    print("This is D4")
elif n==329.63:
    print("This is E4")
elif n==349.23:
    print("This is F4")
elif n==392.00:
    print("This is G4")
elif n==440.00:
    print("This is A4")
elif n==493.88:
    print("This is B4")
else:
    print("The frequency does not correspond to a known note!")