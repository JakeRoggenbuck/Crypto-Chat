import firebase_communicator
 
# This function generates the  
# key in a cyclic manner until  
# it's length isn't equal to  
# the length of original text 
def generateKey(string, key): 
    key = list(key) 
    if len(string) == len(key): 
        return(key) 
    else: 
        for i in range(len(string) - 
                       len(key)): 
            key.append(key[i % len(key)]) 
    return("" . join(key)) 


# This function returns the  
# encrypted text generated  
# with the help of the key 
def cipherText(string, key): 
    cipher_text = [] 
    for i in range(len(string)): 
        x = (ord(string[i]) + 
             ord(key[i])) % 26
        x += ord('A') 
        cipher_text.append(chr(x)) 
    return("" . join(cipher_text)) 


# This function decrypts the  
# encrypted text and returns  
# the original text 
def originalText(cipher_text, key): 
    orig_text = [] 
    for i in range(len(cipher_text)): 
        x = (ord(cipher_text[i]) - 
             ord(key[i]) + 26) % 26
        x += ord('A') 
        orig_text.append(chr(x)) 
    return("" . join(orig_text))


def convert(mode):
    if mode == "en":
        name = "Jake"
        string = input("Message: ")
        keyword = input("Key: ")

        key = generateKey(string, keyword)
        cipher_text = cipherText(string, key)
        firebase_communicator.send(cipher_text, name)

    elif mode == "de":
        data = firebase_communicator.recive()
        
        messages = list(data.values())
        messages_length = len(messages)
        for text in range(messages_length):
            print("WOK")
        #    foo = messages[text]
        #    print(foo[1])

        #key = generateKey(string, key)

# Driver code 
if __name__ == "__main__":
    mode = input("Mode de/en: ")
    convert(mode)
