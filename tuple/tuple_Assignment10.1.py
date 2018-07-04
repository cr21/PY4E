#Write a program to read through a mail log,
#  build a histogram using a dictionary to count
#  how many messages have come from each email address, and print the dictionary.

###
###Exercise 1: Revise a previous program as follows: Read and parse the "From" lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.
dic ={}
fname = input("enter file name")
handle = open(fname)
count =0 
for line in handle :
    line = line.rstrip()
    if not line.startswith('From:') : continue
    words = line.split()
    
    email = words[1]
    

    dic[email]= dic.get(email,0)+1



EmailCount = -1
Email = None



## convert (word,count) -> (count,word)

tmp = []

for word,count in dic.items():
    newT = (count,word)
    tmp.append(newT)

tmp = sorted(tmp,reverse=True)
print(tmp[0])
## above thing can be done using List comprehension in just one line
""" List Comprehension solution
answer = sorted([(count,word) for word,count in dic.items()],reverse=True)[0]
print(answer)"""

