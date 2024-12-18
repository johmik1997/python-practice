# def gret_with(name,location):
#     print(f"hello {name}")
#     print(f"how is the weather of {location}")
# gret_with(name='yohannes',location='addis-ababa')

alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
   
def caesar(startText,shift,cipherText):
    endText=""
    if cipherText=='decrypt':
        shift*=-1
    for char in startText:
        if char in alphabet:
           
            pos=alphabet.index(char)
            remainder=(len(alphabet)-1)-pos
            newPos=pos+shift
            if newPos>25:
                newPos=0+remainder
            endText+=alphabet[newPos]
        else:
            endText+=char
    print(f"you encripted text is {endText}")
    
shouldCountinue=True 
while shouldCountinue:
    showDate=input('do you want encrypt or decrypt type "encrypt" or "decrypt": \n').lower()
    plainText=input('enter the pain text that do you want to encrypt: \n').lower()
    shiftNum=int(input('enter the shift number: \n'))       
    shiftNum=shiftNum%26
    caesar(startText=plainText,shift=shiftNum,cipherText=showDate)
    value=input('if you want to again type "yes" other wise type no')
    if value=='no':
        shouldCountinue=False
        print('goodbye')
