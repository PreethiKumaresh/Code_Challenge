import string
n=str(input())
if any(s in n for s in('a','e','i','o','u')): print("Vowel")
elif any(s in n for s in(string.ascii_lowercase[:27])): print("Consonant")
else: print("Invalid")
