#Write a program to read through a mail log,
#  build a histogram using a dictionary to count
#  how many messages have come from each email address, and print the dictionary.
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

for word,count in dic.items():
    if  count > EmailCount :
        EmailCount = count
        Email = word
print(Email + " " +str(EmailCount))
