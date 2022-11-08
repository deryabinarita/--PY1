import string
from random import sample

def get_random_password(n = 8) -> str:
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.digits
    list_ = a + b + c
    password1 = sample(list_, n)
    password = "".join(password1)
    return password

print(get_random_password())
