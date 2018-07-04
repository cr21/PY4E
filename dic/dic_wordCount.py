
dic ={}
fname = input("enter file name")
handle = open(fname)
count =0 
for line in handle :
    line = line.rstrip()
    words = line.split()
    for word in words :
        dic[word]= dic.get(word,0)+1

BIGCOUNT = -1
BIGWORD = None

for word,count in dic.items():
    if  count > BIGCOUNT :
        BIGCOUNT = count
        BIGWORD = word
print(BIGCOUNT)
print(BIGWORD)