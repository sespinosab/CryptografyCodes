
import numpy as np
letters=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm',
         'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#------------------Function to encrypt----------------------------
def encrypt(message,A):
  #Loop through the array to change each pair of letters
  for i in range(len(message)):

    #Get indexes for the instances of each letter in the A matrix
    letterIndexes1=np.where(A[:,:]==message[i][0])
    letterIndexes1=list(map(int,letterIndexes1))
    letterIndexes2=np.where(A[:,:]==message[i][1])
    letterIndexes2=list(map(int,letterIndexes2))

    if letterIndexes1[0]==letterIndexes2[0]: #Verify if the letters are in the same row
      if letterIndexes1[1]==4: #Verify if the first letter is in the last column
        message[i][0]=A[letterIndexes1[0]][0]
      else:
        message[i][0]=A[letterIndexes1[0]][letterIndexes1[1]+1]
     
      if letterIndexes2[1]==4:#Verify if the second letter is in the last column
        message[i][1]=A[letterIndexes2[0]][0]
      else:
        message[i][1]=A[letterIndexes2[0]][letterIndexes2[1]+1]

    elif letterIndexes1[1]==letterIndexes2[1]: #Verify if the letters are in the same column

      if letterIndexes1[0]==4: #Verify if the first letter is in the last row
        message[i][0]=A[0][letterIndexes1[1]]
      else:
        message[i][0]=A[letterIndexes1[0]+1][letterIndexes1[1]]
     
      if letterIndexes2[0]==4:  #Verify if the second letter is in the last row
        message[i][1]=A[0][letterIndexes2[1]]
      else:
        message[i][1]=A[letterIndexes2[0]+1][letterIndexes2[1]]

    else: #When the letters are neither in the same column or row
      message[i][0]=A[letterIndexes1[0]][letterIndexes2[1]]
      message[i][1]=A[letterIndexes2[0]][letterIndexes1[1]]
  return message
#----------------------------------------------------------------------

#------------------Function to encrypt----------------------------
def decrypt(message,A):
  #Loop through the array to change each pair of letters
  for i in range(len(message)):

    #Get indexes for the instances of each letter in the A matrix
    letterIndexes1=np.where(A[:,:]==message[i][0])
    letterIndexes1=list(map(int,letterIndexes1))
    letterIndexes2=np.where(A[:,:]==message[i][1])
    letterIndexes2=list(map(int,letterIndexes2))

    if letterIndexes1[0]==letterIndexes2[0]: #Verify if the letters are in the same row
      if letterIndexes1[1]==0: #Verify if the first letter is in the first column
        message[i][0]=A[letterIndexes1[0]][4]
      else:
        message[i][0]=A[letterIndexes1[0]][letterIndexes1[1]+-1]
     
      if letterIndexes2[1]==0:#Verify if the second letter is in the first column
        message[i][1]=A[letterIndexes2[0]][4]
      else:
        message[i][1]=A[letterIndexes2[0]][letterIndexes2[1]-1]

    elif letterIndexes1[1]==letterIndexes2[1]: #Verify if the letters are in the same column

      if letterIndexes1[0]==0: #Verify if the first letter is in the first row
        message[i][0]=A[4][letterIndexes1[1]]
      else:
        message[i][0]=A[letterIndexes1[0]-1][letterIndexes1[1]]
     
      if letterIndexes2[0]==0:  #Verify if the second letter is in the last row
        message[i][1]=A[4][letterIndexes2[1]]
      else:
        message[i][1]=A[letterIndexes2[0]-1][letterIndexes2[1]]

    else: #When the letters are neither in the same column or row
      message[i][0]=A[letterIndexes1[0]][letterIndexes2[1]]
      message[i][1]=A[letterIndexes2[0]][letterIndexes1[1]]
  return message
#----------------------------------------------------------------------


#-----Function to create the pairs for the message-------
def create_pairs(message):
  message=np.array(list(message))

  #Loop through the message by pairs
  for i in range(int(message.shape[0]/2)):
    if message[2*i] == message[2*i+1]: #If the pair has the same letter, insert an x
      message=np.insert(message, 2*i+1, 'x')
      
  if message.shape[0]%2 != 0: #If the length of the message is odd, insert an x at the end
    message=np.concatenate((message,['x']),axis=0)

  message=message.reshape((-1,2)) #Reshape the message to an array of pairs
  #print(message)
  return message
#---------------------------------------------------------

#-----Function to create the encryption matrix-------
def create_matrix(key,A):
  for i in range(5):
    for j in range(5):
      if len(key) != 0:
        A[i][j]=key[0]
        letters.remove(key[0])
        key=key.replace(key[0],'')

      else:
        A[i][j]=letters[0]
        letters.remove(letters[0])

  #print(A)
  return A
#-------------------------------------------e-------

print("Welcome to the Playfair Cipher app!")
choice=input("Insert 1 for ciphering a message or 0 for deciphering a message\n")


if choice == '1':#Encrypt
  message=input("Please insert the message to be ciphered: ")
  key1=input("Please insert the desired key to cipher the message: ")

  #----Change and fix format-------

  #Eliminate blank spaces
  message=message.replace(' ','')
  key1=key1.replace(' ','')

  #Lowercase the strings
  message=message.lower()
  key1=key1.lower()

  #Replace all J's to I's
  message=message.replace('j','i') 
  key1=key1.replace('j','i') 

  #--------------------

  A = np.arange(25) #Create array numpy
  A = list(map(lambda x: '', A)) #Convert array to numpy so it can admit strings
  A = np.array(A).reshape((5,5)) #Shape the array to matrix
  A=create_matrix(key1,A) #Fill the key matrix
  
  message=create_pairs(message) #Convert the message to pairs

  message = encrypt(message, A) #Encrypt the message

  print(*message.reshape((1,-1)))
  print(str(message.reshape((1,-1))).replace('[','').replace(']','').replace('\'','').replace('\n','').replace('  ',' ')) #Print de coded message without array format

elif choice=='0':#Decrypt
  ciphered_message=input("Please insert the message to be deciphered: ")
  key2=input("Please insert the desired key to decipher the message: ")

  #----Change and fix format-------

  #Eliminate blank spaces
  ciphered_message=ciphered_message.replace(' ','')
  key2=key2.replace(' ','')

  #Lowercase the strings
  ciphered_message=ciphered_message.lower()
  key2=key2.lower()

  #Replace all J's to I's
  ciphered_message=ciphered_message.replace('j','i') 
  key2=key2.replace('j','i') 

  #--------------------

  A = np.arange(25) #Create array numpy
  A = list(map(lambda x: '', A)) #Convert array to numpy so it can admit strings
  A = np.array(A).reshape((5,5)) #Shape the array to matrix
  A=create_matrix(key2,A) #Fill the key matrix

  ciphered_message=create_pairs(ciphered_message) #Convert the message to pairs

  ciphered_message = decrypt(ciphered_message, A) #Decrypt the message

  print(str(ciphered_message.reshape((1,-1))).replace('[','').replace(']','').replace('\'','').replace('\n','').replace('  ',' ')) #Print de uncoded message without array format

else:
  print("Please insert a valid option")