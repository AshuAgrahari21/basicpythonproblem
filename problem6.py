#write a python script to print two given words in dictionary order.
word1=str(input())
word2=str(input())
word1=word1.lower()
word2=word2.lower()
print("with out dictionary order",word1,word2)
if word1<word2:
    print ("after dictionary order",word1,word2)
else:
    print("after dictionary order",word2,word1)    