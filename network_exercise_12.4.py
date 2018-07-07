import urllib.request, urllib.parse, urllib.error
import bs4
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url).read()
soup = bs4.BeautifulSoup(html, 'html.parser')

# Retrieve all of the anchor tags
tags = soup('p')
count=0
for tag in tags:
    count = count+1
print(count)