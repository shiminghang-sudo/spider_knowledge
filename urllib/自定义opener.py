import urllib.request

"""
    自定义urlopen()函数，名叫oper，可以支持IP代理
    
"""

url = 'http://www.baidu.com/'
# urllib.request.urlopen()

# # 构建一个HTTPHandler 处理器对象，支持处理HTTP请求
http_handler = urllib.request.HTTPHandler()

proxy = {
    'http':'61.138.33.20:808',
    # 'https':'120.69.82.110:44693',
}
#构建支持代理的handler
proxy_handler = urllib.request.ProxyHandler(proxies=proxy)


# 调用urllib.request.build_opener()方法，创建支持处理HTTP请求的opener对象
opener = urllib.request.build_opener(proxy_handler)

response = opener.open(url)
print(response.status)

urllib.request.install_opener(opener)
"""
    # 1. 如果按照上面代码，只有使用opener.open()方法发送
    请求才使用自定义的代理，而urlopen()则不使用自定义代理。
    response = opener.open(request)
    
    # 2. 将自定义的opener设置为全局的opener，之后所有的，不管是
    opener.open()还是urlopen() 发送请求，都将使用自定义代理。
    # request.install_opener(opener)
    # response = urlopen(request)
"""


