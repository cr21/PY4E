
#Write a program that categorizes each mail message by which day of the week the commit was done. To do this look for lines that start with "From", then look for the third word and keep a running count of each of the days of the week. At the end of the program print out the contents of your dictionary (order does not matter).

#Sample Line:

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
dic ={}
fname = input("enter file name")
handle = open(fname)
count =0 
for line in handle :
    line = line.rstrip()
    if not line.startswith('From') : continue
    words = line.split()
    if len(words) > 2 :
        day = words[2]
        print(day)
        dic[day]= dic.get(day,0)+1
print(dic)

