import random
import string
try:
    length = int(input("number of characters in the password: "))
    amount = int(input("number of passwords:"))
except ValueError:
    print("Invalid number")

uppercase = string.ascii_uppercase
lowercase = string.ascii_lowercase
digits = string.digits
punctuation = string.punctuation

upper, lower, digi, punc = True, True, True, True

all = ""
if upper:
    all += uppercase

if lower:
    all += lowercase

if digi:
    all += digits

if punc:
    all += punctuation

for i in range(amount):
    password = "".join(random.sample(all, length))
    print(password)

