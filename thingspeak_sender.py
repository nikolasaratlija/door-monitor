import urllib.request as ul

ACCESS_TOKEN = None

data = None
field = None

data = ul.urlopen('https://api.thingspeak.com/update?api_key=' + ACCESS_TOKEN + '&field + '+ field + '=' + data)
print(data.read())

