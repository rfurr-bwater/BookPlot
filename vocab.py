def remove_punctuation(line):
    line = line.replace("—"," ").replace("-"," ").replace("."," ")
    line = line.replace(","," ").replace(";"," ").replace("?"," ")
    line = line.strip("\'").replace(":", " ")
    line = line.replace('“'," ").replace('”'," ").replace("‘"," ")
    line = line.replace(")"," ").replace("("," ").replace("\""," ").replace("!"," ")
    return line

vocab = list()
fhand = open('book.txt',"r", encoding='utf-8')
for line in fhand:
    line = remove_punctuation(line)
    
    pieces = line.split()
    
    #use list comprehension to convert each piece in pieces to lowercase 
    word_list = [w.lower() for w in pieces]

    #in the for-loop, 
    for word in word_list:
        vocab.append(word)

word_set = set(vocab)
count = 0
#print the words and length count
for word in word_set:
    print(word)
    count+=1
    if count> 40: break
print("Total words in the book = ", len(vocab))
print("Number of distinct words = ", len(word_set))

 # write an assert statement to make sure that there are fewer vocab words than total words

assert len(word_set) < len(vocab)