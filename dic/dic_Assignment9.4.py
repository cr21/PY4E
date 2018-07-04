#This program records the domain name (instead of the address) where 
# the message was sent from instead of who the mail came 
# from (i.e., the whole email address). At the end of the program, print out the contents of your dictionary.

dic ={}
fname = input("enter file name")
handle = open(fname)
count =0 
for line in handle :
    line = line.rstrip()
    if not line.startswith('From:') : continue
    words = line.split()
    
    email = words[1]
    domain =  email.split("@")[1]
    
    dic[domain]= dic.get(domain,0)+1



domainCount = -1
domain = None

for word,count in dic.items():
    if  count > domainCount :
        domainCount = count
        domain = word
print(domain + " " +str(domainCount))
