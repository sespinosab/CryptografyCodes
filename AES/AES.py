import pyaes
import numpy as np
import io
import base64
import cv2
import PIL.Image as Image
from matplotlib import pyplot as plt

 
# load the image and convert into numpy array
#img = Image.open('winged-hussar.jpg')

securityNumber=input("Insert level of security between 128 bits, 192 bits or 256 bits: ")
key=input("Insert the key: ")


if securityNumber != '128' and securityNumber != '192' and securityNumber != '256':
  print("Number not accepted")
else:
  
  securityNumber=int(securityNumber)
  #Pass image to byte array
  with open("winged-hussar.jpg", "rb") as image:
    f = image.read()
    b = bytes(f)

  iv = "InitializationVe"

  byteArrayKey = bytearray(key.encode())


  if len(key) == securityNumber/8:
    #aes = pyaes.AESModeOfOperationCBC(byteArrayKey, iv = iv)
    aes = pyaes.AESModeOfOperationCTR(byteArrayKey)
    #aes = pyaes.AESModeOfOperationCFB(byteArrayKey, iv = iv, segment_size = 2)
    cryptedImage = aes.encrypt(b)

    print("DES encryption: ")
    print(cryptedImage)

    #Encode image using Base 64
    b64Image=base64.b64encode(cryptedImage)

    print()
    print("Base 64 encryption: ")
    print(b64Image)

    #Decrypt Base 64
    decryptedImageB64=base64.b64decode(b64Image)

    aes = pyaes.AESModeOfOperationCTR(byteArrayKey)
    decryptedImage = aes.decrypt(decryptedImageB64)

    np_jpg = np.frombuffer(decryptedImage, dtype=np.uint8)
    img2 = cv2.imdecode(np_jpg, flags=1)
    cv2.imwrite('decryptedImage.jpg', img2)

    img_color = cv2.imread('decryptedImage.jpg',1)
    plt.imshow(cv2.cvtColor(img_color, cv2.COLOR_BGR2RGB))
    plt.axis("off")
    plt.show()
  else:
    print("Inserted key does not match the required security level")
  