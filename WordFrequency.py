infile = open("sometext.txt","r")
read_file = infile.read()
    
dictionary = {}
word_list=read_file.split(" ")
for value in word_list:
    value = value.lower()
    value = value.replace(',','')
    value = value.replace('.','')
    amount=word_list.count(value)
    dictionary[value]=amount

    for word_list in dictionary:
        if value in word_list:
            dictionary[value] = dictionary[value]+1
        else:
            dictionary[value] =1
    

print(dictionary)
