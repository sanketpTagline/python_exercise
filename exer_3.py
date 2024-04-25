
sentences = ["My name is Ram", "He is a good person", "You should be careful while coding", "He can do better", "The person is mysterious", "Jay Shree Ram", "It is my pen."]

name_split = [name.split() for name in sentences]  
  
print("\nword_trees = ",name_split)
 
wordCount = {}

for words in name_split:
    for word in words:
        
        wordCount[word] = wordCount.get(word,0)+1
        
print("\nword count :",wordCount)

 

 
