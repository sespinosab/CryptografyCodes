import numpy as np
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print("Welcome to the Ceasar Cipher app!")
choice=input("Insert 1 for ciphering a message or 0 for deciphering a message\n")

if choice=='1': #Encrypt
    message=input("Please insert the message to be deciphered: ")
    k=input("Please insert the k to codify: ")

    #----Change and fix format-------

    #Eliminate blank spaces
    message=message.replace(' ','')

    #Lowercase the strings
    message=message.lower()

    #--------------------

    message2 = np.arange(len(message)) #Create array numpy
    message2 = list(map(lambda x: '', message2)) #Convert array to numpy so it can admit strings

    for i in range(len(message)):
      for j in range(len(letters)):
        if message[i]==letters[j]:
          message2[i]=letters[(j+int(k))%26]

    print(message2)

elif choice=='0': #Decrypt
  ciphered_message=input("Please insert the message to be deciphered: ")
  k=input("Please insert the k to codify: ")

  #Lowercase the strings
  ciphered_message=ciphered_message.lower()
  
  ciphered_message=ciphered_message.replace(' ','')

  message = np.arange(len(ciphered_message)) #Create array numpy
  message = list(map(lambda x: '', message)) #Convert array to numpy so it can admit strings

  for i in range(len(ciphered_message)):
    for j in range(len(letters)):
      if ciphered_message[i]==letters[j]:
        message[i]=letters[(j-int(k))%26]

  print(message)
else:
  print("Please insert a valid option")