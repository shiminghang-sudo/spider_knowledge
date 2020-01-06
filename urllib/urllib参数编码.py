import urllib.request
import urllib.parse
import ssl

kw = {'kw': '美女'}
#
# result = urllib.parse.urlencode(kw)
# print(result)       # kw=%E7%BE%8E%E5%A5%B3
#
# re = urllib.parse.unquote(result)
# print(re)           # kw=美女
#
# url = 'https://tieba.baidu.com/f?'
#
# full_url = url + result
# response = urllib.request.urlopen(full_url)
# print(response.read())

'''
取前10页，把页面的数据保存到本地，用面向对象写

urllib.request.urlopen(url) 只能访问http的网站
如果想要访问https的网站，则需要添加ssl证书验证信息
'''


class TieBaSpider(object):
    def __init__(self):
        self.url = 'https://tieba.baidu.com/f?'

    def send_request(self, url, page):
        print(f'正在发送第{page}页')
        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(url, context=context)
        self.write_file(response.read(), page)

    def write_file(self, content, page):
        print(f'正在保存第{page}页')
        with open(f'tieba{page}.html', 'wb') as f:
            f.write(content)

    def start(self):
        page = int(input('请输入你要爬取的页数:'))
        for i in range(1, page + 1):
            pn = (i - 1) * 50
            kw = {'kw': '美女', 'pn': pn}
            result = urllib.parse.urlencode(kw)
            full_url = self.url + result
            self.send_request(full_url, i)

if __name__ == '__main__':
    tbs = TieBaSpider()
    tbs.start()


