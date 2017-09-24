"""from urllib import request, error
from http import cookiejar

filename = 'cookie.txt'
cookie = cookiejar.MozillaCookieJar(filename)
opener = request.build_opener(request.HttpCookieProcessor(cookie))
"""
import requests

r = requests.get('https://github.com', verify=True)
print(r.text)
