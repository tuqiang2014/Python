from urllib import urlopen
data = urlopen('http://peak.telecommunity.com/dist/ez_setup.py')
with open('ez_setup.py', 'wb') as f:
f.write(data.read())