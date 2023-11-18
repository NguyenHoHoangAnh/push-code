string = input("Enter a string: ")
string = string.lower()
is_palindrome = True
for i in range(len(string) // 2):
    if string[i] != string[len(string) - 1 - i]:
        is_palindrome = False
        break
if is_palindrome:
    print(string, "is a palindrome")
else:
    print(string, "is not a palindrome")