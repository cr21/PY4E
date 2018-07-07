import urllib.request, urllib.parse, urllib.error
urlname = input('enter url :')
fhand =  urllib.request.urlopen(urlname)
len_line = 0
for line in fhand:
    len_line +=  len(line)
    if(len_line<3000):
        
        print(line.decode().rstrip())
print(len_line)
    
