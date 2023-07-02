import random
import string 

def generate_pass(length):
    charcters = string.ascii_letters + string.digits + string.punctuation.replace(" ","")
    password =  ''.join(random.choice(charcters) for _ in range (length))
    return password

if __name__ =='__main__':
    pass_length = int(input("enter the length of the password "))
    generate_pass = generate_pass(pass_length)
    print("password is ", generate_pass)