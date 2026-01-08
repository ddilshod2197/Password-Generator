import random
import string

length = int(input("Parol uzunligini kiriting: "))

chars = string.ascii_letters + string.digits + string.punctuation
password = "".join(random.choice(chars) for _ in range(length))

print("Yaratilgan parol:", password)
