import numpy as np
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#-------Create Vigenere matrix----------------------------------
def createVignere(letters):
  vignere = np.arange(676)
  vignere = list(map(lambda x: '',  vignere)) #Convert array to numpy so it can admit strings
  vignere = np.array(vignere).reshape((26,26)) #Shape the array to matrix

  for i in range(26):
    counter=i
    for j in range(26):
      vignere[i][j]=letters[counter%26]
      counter=counter+1
  return vignere
#-------------------------------------------------------------



print("Welcome to the Vigenere Cipher app!")
choice=input("Insert 1 for ciphering a message or 0 for deciphering a message\n")

if choice == '1':#Encrypt
    
  message=input("Please insert the message to be deciphered: ")
  key=input("Please insert the key to codify: ")
  t=input("Please insert the t parameter: ")


  #----Change and fix format-------

  #Eliminate blank spaces
  message=message.replace(' ','')

  #Lowercase the strings
  message=message.lower()

  #--------------------

  vignere=createVignere(letters)

  #Create numpy arrays
  message = np.array(list(message)) 
  key = np.array(list(key))
  crypted_message=np.copy(message)

  letters2=np.array(letters)

  #Codify message
  for i in range(len(message)):
    indexM=np.where(letters2[:]==message[i])
    indexM=list(map(int,indexM))
    indexK=np.where(letters2[:]==key[i%len(key)])
    indexK=list(map(int,indexK))
    crypted_message[i]=vignere[indexK[0]][indexM[0]]


  # Shape the crypted message

  while len(crypted_message)%int(t) != 0:
    crypted_message = np.append(crypted_message,[' '])

  print(str(crypted_message.reshape((-1,int(t)))).replace('[',' ').replace(']',' ').replace('\'','').replace('\n','').replace('  ',' '))

elif choice == '0':#Decrypt
  crypted_message=input("Please insert the message to be deciphered: ")
  key=input("Please insert the key to codify: ")
  t=input("Please insert the t parameter: ")

  #----Change and fix format-------

  #Eliminate blank spaces
  crypted_message=crypted_message.replace(' ','')

  #Lowercase the strings
  crypted_message=crypted_message.lower()

  #--------------------

  vignere=createVignere(letters)

  #Create numpy arrays
  crypted_message = np.array(list(crypted_message)) 
  key = np.array(list(key))

  letters2=np.array(letters)

  #Decode message
  for i in range(len(crypted_message)):
    #indexM=np.where(letters2[:]==message[i])
    #indexM=list(map(int,indexM))

    indexK=np.where(letters2[:]==key[i%len(key)])
    indexK=list(map(int,indexK))

    indexV=np.where(vignere[indexK,:]==crypted_message[i])
    indexV=list(map(int,indexV))

    crypted_message[i]=letters2[indexV[1]]

  # Shape the crypted message

  while len(crypted_message)%int(t) != 0:
    crypted_message = np.append(crypted_message,[' '])

  print(str(crypted_message.reshape((-1,int(t)))).replace('[',' ').replace(']',' ').replace('\'','').replace('\n','').replace('  ',' '))

else:
  print("Please insert a valid option")