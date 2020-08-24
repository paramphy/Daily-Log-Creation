import os
from textblob import TextBlob

path = r'C:\Users\param\Desktop\Daily_logs'
d = 1
while d < 24:
    try:
        date = str(d) + ".8.2020.txt"
        completepath = os.path.join(path, date)
        f = open(completepath,'r')
        massage = f.read()
        #print(massage)
        f.close()
        f1 = open("demofile4.txt", "a")
        f1.write(massage)
        f1.write('\n')
        f1.close()            
        d += 1
    except: 
        pass
        d += 1

f2 = open("demofile4.txt","r")
pullData = f2.read()
dataArray = pullData.split('\n')
text = '.'
for eachline in dataArray:
    if len(eachline)>1:
        text= text + eachline
blob = TextBlob(text)

print(blob.sentences)
for sentence in blob.sentences:
    print(sentence)
    print("\n")
    print(sentence.sentiment)
    print("\n")

    