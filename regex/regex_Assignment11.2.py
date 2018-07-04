import re

fname = input("enter file name")
handle = open(fname)
revision_list = []

for line in handle :
    line = line.rstrip()
    revison = re.findall('^New Revision: ([0-9]+)',line)
    if len(revison) < 1 : continue
    revision_list.append(float(revison[0]))


print(sum(revision_list)/len(revision_list))