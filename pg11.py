#anagram
x=(input("Enter first string:"))
y=(input("Enter second string:"))
if sorted(x.lower())==sorted(y.lower()):
    print("anagram")
else:
    print("not anagram")