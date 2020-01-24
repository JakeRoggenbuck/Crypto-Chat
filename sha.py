from Crypto.Cipher import AES
import firebase_communicator

def encrypt(name, key, iv, message):
    obj = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = obj.encrypt(message)
    firebase_communicator.send(ciphertext, name)

def decrypt():
    keyword = input("Key: ")
    iv = input("iv? ")

    data = firebase_communicator.recive()
    messages = list(data.values())
    messages_length = len(messages)
    for text in range(messages_length):
        ciph = messages[text]
        thing = ciph[1]
        
        obj2 = AES.new(key, AES.MODE_CBC, iv)
        bar = obj2.decrypt(thing)
        print(bar)

def convert(mode):
    if mode == "en":
        name = input("Name: ")
        keyword = input("Key: ")
        iv = input("iv? ")
        message = input("Message: ")
        foo = encrypt(name, keyword, iv, message)
    
    elif mode == "de":
        decrypt()    

def main():
    mode = input("mode en/de")
    convert(mode)

main()
