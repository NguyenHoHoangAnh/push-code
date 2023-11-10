letter=input("Enter a letter: ")
if letter=="u" or letter=="e" or letter=="o" or letter=="a" or letter=="i":
    print(letter,"is a vowel")
elif letter=="y":
    print("Sometimes ",letter," is a vowel",", sometimes ",letter," is a consonant.",sep="")
else:
    print(letter,"is a consonant")