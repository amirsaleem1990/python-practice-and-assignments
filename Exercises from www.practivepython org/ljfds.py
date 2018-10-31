a = 'http://norvig.com/ngrams/sowpods.txt'



import urllib.request
htmlfile = urllib.request.urlopen(a)
htmltext = htmlfile.read()
print(htmltext)
