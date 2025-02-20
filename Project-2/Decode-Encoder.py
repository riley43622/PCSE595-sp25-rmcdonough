from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import os




promt1=input("Enter whether you would like to encode or decode please:")
promt1=promt1.lower()
#file_for_encode=input("Enter the name of the file you would like to encode and don't forget the file type <.txt>")
#file_for_decode=input("Enter the name of the file you would like to decode and don't forget the file type:")

def user_info(prom):
    #this first function gather the information needed to encode or decode
    if prom=="encode":
        file_for_encode = input("Enter the name of the file you would like to encode and don't forget the file type <.txt>:")
        print("Reminder: the amount of digits as follows for each key: AES-128: 16, AES-192: 24, AES-256: 32")
        aes_type=input("Enter the bit of AES strength: options are AES-128,AES-192 and AES-256:")
        key_password=input("Please enter what you would like your key/password to be:")
        return file_for_encode,aes_type,key_password,aes_type
    elif prom=="decode":
        file_for_decode=input("Enter the name of the file you would like to decode and don't forget the file type <.enc>:")
        print("Reminder: the amount of digits as follows for each key: AES-128: 16, AES-192: 24, AES-256: 32")
        aes_type = input("Enter the bit of AES strength: options are AES-128,AES-192 and AES-256:")
        key_password = input("Please enter your key/password:")
        return file_for_decode,aes_type,key_password,aes_type
    else:
        print("Please enter again")
def encoder(file_for_encode,aes_type,key_password):
    #this function encode this file by reading in the txt file than encoding it than writing it to a new file.enc
    key = keyer(key_password, aes_type)
    with open(file_for_encode,'rb') as bruh:
        plaintext=bruh.read()
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
        s = file_for_encode.split(".")
        with open(s[0] + ".enc", 'wb') as f:
            f.write(iv + ciphertext)
def decoder(file_for_decode,aes_type,key_password):
    #this function is meant to decode an ecryption by reading it in than decoding it and writing it to a dec file
    key=keyer(key_password,aes_type)
    with open(file_for_decode, 'rb') as bruh:
        ciphertexto = bruh.read()
        iv = os.urandom(16)
        cipher = AES.new(key, AES.MODE_CBC, iv)
        plaintext = unpad(cipher.decrypt(ciphertexto), AES.block_size)
        s = file_for_decode.split(".")
        with open(s[0] + ".dec", 'wb') as f:
            f.write(plaintext)
def keyer(key_password, aes_type):
    #keyer is meant to verify the size of the key
    key_sizes={"AES-128": 16, "AES-192": 24, "AES-256": 32}
    key_length = key_sizes.get(aes_type, 32)
    return key_password.encode().ljust(key_length, b'\0')[:key_length]
def decision(prom):
    # this determines what type of function to run depending on what is entered
    if prom=="decode":
        decoder(file_for_decode, aes_type, key_password)
    else:
        encoder(file_for_decode, aes_type, key_password)


file_for_decode,aes_type,key_password,aes_type=user_info(promt1)
decision(promt1)


