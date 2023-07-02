import random
import string 

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation.replace(" ","")
    password = ''.join(random.choice(characters) for  _ in range (length))
    return password

if __name__ == '__main__':
    generate_password = generate_password(10)
    print(generate_password)