import requests
from urllib import parse

data={'city':'北京'}
city=parse.urlencode(data).encode('utf-8')
url=''