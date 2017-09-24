from urllib import request, error


url = 'http://www.baidu.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:55.0) \
Gecko/20100101 Firefox/55.0'
headers = { 'User-Agent' : user_agent }
try:
    req = request.Request(url, headers = headers)
    response = request.urlopen(req)
    print(response.read())
except error.URLError as e:
    if hasattr(e,"code"):
        print(e.code)
    if hasattr(e,"reason"):
        print(e.reason)
