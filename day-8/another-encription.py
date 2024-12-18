# def encryption(encryptText,shift):
#     cipherText=''
#     for letter in encryptText:
#         pos=alphabet.index(letter)
#         remainder=len(alphabet)-pos
#         newPos=pos+shift
#         if newPos>25:
#             newPos=0+remainder
         
#     print(f"you encripted text is {cipherText}")
#     value=input('do you want to encrypt or decrypt again type yes or no').lower()
#     if value=='yes':
#         identifyJob()
#     else:
#         return
# def  decription(deriptText,shift):
#     cipherText=''
#     for letter in deriptText:
#         pos=alphabet.index(letter)
#         newPos=pos-shift
#         remainder=len(alphabet)-pos
#         if newPos <=0:
#             newPos=25-remainder
#         cipherText+=alphabet[newPos]
#     print(f"you encripted text is {cipherText}") 
#     value=input('do you want to encrypt or decrypt again type yes or no').lower()
#     if value=='yes':
#         identifyJob()
#     else:
#         return

# def identifyJob():

#     if showDate=='encrypt':
#         encryption(plainText ,shiftNum)
#         print('encryption')
#     else:
#         decription(plainText,shiftNum)
#         print('decrypt')
# identifyJob()