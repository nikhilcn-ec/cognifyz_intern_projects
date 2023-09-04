import io,os

#open the file 
file=open("myfile.txt","r")

#list containing ascii code for puntuations
l=[33,34,39,44,45,46]

#reading entire file once
unsorted_data=(file.read())

#for each puntuations in list
for i in l:
       
       #replacing puntuations with empty string
       unsorted_data=unsorted_data.replace(chr(i),"")

#coverting to lowercase and splitting the unsorted_data
unsorted_data=(unsorted_data.lower()).split()

#sorting the data in aplhabet wise
sorted_data=sorted(unsorted_data)

#creating empty dictionary
d={}

#for each word in sorted_data
for word in sorted_data:

    #if word in dictionary then increment key
    if word in d:
        d[word]=d.get(word)+1

    #else adding 1 occurence to key
    else:
        d[word]=1

#printing word and its occurence
for i in d:
    print(i,":",d[i])

 
