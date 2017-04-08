import urllib.request
import re
import urllib.parse

url = 'http://www.urbandictionary.com/define.php?term=eat%20shit'

req = urllib.request.Request(url)
resp = urllib.request.urlopen(req)
respData = resp.read()

paragraphs = re.findall(r'^$',str(respData))
for eachP in paragraphs:
    print(eachP)
