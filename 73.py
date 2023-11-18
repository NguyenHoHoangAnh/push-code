import string
phrase=input("Enter a phrase: ")
def process_str(phrase):
    #Convert to lower case
    lowercase_str=phrase.lower()
    #Remove spaces
    no_spaces=lowercase_str.replace(" ","")
    #Remove punctuation marks
    translator=str.maketrans("","",string.punctuation)
    result=no_spaces.translate(translator)
    return result

cleaned_phrase=process_str(phrase)
count=len(cleaned_phrase)
inverted_phrase=""
i=1
while i<=count:
    inverted_phrase=cleaned_phrase[i-1]+inverted_phrase
    i=i+1
if inverted_phrase==cleaned_phrase:
    print(phrase,"is a palindrome")
else:
    print(phrase,"is not a palindrome")