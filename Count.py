introstring=input("enter string")
characterCount=0
wordCount=1
for i in introstring:
    characterCount= characterCount+1
    if(i==' '):
        wordCount= wordCount+1

print(characterCount) 
print(wordCount)