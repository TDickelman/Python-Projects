# Put your code here
# Request the inputs
codedText = input("Enter the coded text: ")
distanceValue = int(input("Enter the distance value: "))
# Calculate the decryption
plainText = ""
for ch in codedText:
    ordvalue = ord(ch)
    cipherValue = ordvalue - distanceValue
    plainText += chr(cipherValue)
print(plainText)
