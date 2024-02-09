import random
import string

length = 20
amount = 3

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

