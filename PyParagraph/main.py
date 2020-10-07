import pandas as pd 
import re

filepath1 = "raw_data/paragraph_1.txt"
filepath2 = "raw_data/paragraph_2.txt"

#userinput = input("What file would you like to choose?  1 or 2 " )

#if userinput == "1":
file1 = pd.read_csv(filepath1, sep= " ", header=None, squeeze=bool)
file = file1
#elif userinput == "2":
#    file2 = pd.read_csv(filepath2, sep = "\t", header=None, squeeze=bool)
#    file = file2

#store to words in a list
paragraph=[]
for words in file :
    paragraph.append(str(words))
paragraph = str(paragraph)
#split the file in words following the pattern 
words = paragraph.split()
wordcount = len(words)

sentence = re.DOTALL(paragraph)
print(sentence)
