"""
This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the "From" line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

"""


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
        timestamp = words[5]
        print(timestamp)
        hour = timestamp.split(":")[0]
        dic[hour]= dic.get(hour,0)+1
print(dic)


sorted_hout_count = sorted(dic.items())

for hour,count in sorted_hout_count :
    print(str(hour) + " "+  str( count))

