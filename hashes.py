import random
# Mas é melhor usar o bycrpt do que outro e para usar, tenho que instalar: pip install bcrypt
import hashlib
import bcrypt

letras_mai: str = 'ABCDEFGHIJKLMNOPQRSTUVXYZWÇ'
letras_min : str = letras_mai.lower()
letras: str = letras_mai + letras_min
passwords_dict: dict = {}

i = 1
while i != 3:
    user_pass = input('Write your password: ')
    c: list = random.sample(letras, random.randint(13, 16)) + random.sample('1234567890', random.randint(3, 6))
    random.shuffle(c)
    salt = bcrypt.gensalt()
    print(salt)
    password: str = ''.join(c) + user_pass
    print(password)

    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    hex_dig = md5.hexdigest()
    print(hex_dig)

    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    print(hashed_password)

    passwords_dict[password] = (hashed_password, hex_dig)
    print(passwords_dict)
    i += 1
