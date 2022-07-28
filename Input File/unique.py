# Put your code here
inputFile = input("Enter the input file name: ")
inFile = open(inputFile)
uniqueWords = []
for line in inFile:
    words = line.split()
    for currentWord in words:
        currentWord = currentWord.strip(',.?!')
        if currentWord not in uniqueWords:
            uniqueWords.append(currentWord)
inFile.close()
uniqueWords.sort()
print()
for currentWord in uniqueWords:
    print(currentWord)
