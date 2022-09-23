def Encrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open("Enc-" + filename, "wb")
    file.write(data)
    file.close()

def Decrypt(filename, key):
    file = open(filename, "rb")
    data = file.read()
    file.close()

    data = bytearray(data)
    for index, value in enumerate(data):
        data[index] = value ^ key
    
    file = open("Dec-" + filename, "wb")
    file.write(data)
    file.close()

key = int(input("Ask for a key between 1 - 100: "))
filename = input("Please enter your file name with the extension: ")

Option = int(input("1. Encryption\n2. Decryption\nChoose the algorithm to perform: "))

if(Option == 1):
    Encrypt(filename, key)
elif(Option == 2):
    Decrypt(filename, key)
else:
    print("Choose between 1 or 2")
