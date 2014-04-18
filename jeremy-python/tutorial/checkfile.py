import urllib2
url = "http://google.com/"
response = urllib2.urlopen(url)
info = response.read()

FileHandle2 = open('testfile3','w')

print >> FileHandle2, info
