#Exercise 2: Write a program to prompt for a file name,
#  and then read through the file and look for lines of the form:

#X-DSPAM-Confidence:0.8475

#When you encounter a line that starts with "X-DSPAM-Confidence:" pull apart the line to extract the floating-point number on the line. Count these lines and then compute the total of the spam confidence values from these lines. When you reach the end of the file, print out the average spam confidence.
#
#

fname = input("Please enter file name to open")

try :
    handle =  open(fname)
except :
    print("no file exist please try again")
    exit()
count = 0
sum_confidence = 0

for line in handle :
    
    if line.startswith('X-DSPAM-Confidence'):
        count = count+1
        endPosition = line.find(':')
        sum_confidence = sum_confidence + float(line[endPosition+1:-1].strip())

        

        
    
        
avg_confidence =  sum_confidence/count
print(avg_confidence)
