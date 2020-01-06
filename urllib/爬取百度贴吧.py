import urllib.parse
import urllib.request
import re
import ssl
import os


class TieBaSpider(object):
    def __init__(self):
        self.url = 'http://tieba.baidu.com/f?'
        self.turl = "http://tieba.baidu.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:71.0) Gecko/20100101 Firefox/71.0'
        }

    def send_request(self, url):
        # 第一步构造request
        request = urllib.request.Request(url=url, headers=self.headers)

        # 发送请求
        content = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=content)

        if response.status == 200:
            content = response.read()
            self.write_html(content)
            self.parse(content).decode('utf8')
        else:
            print('出错了！', response.status)

    # 详情发送请求
    def send_detail_request(self, detail_url):
        # 第一步构造request
        request = urllib.request.Request(url=detail_url, headers=self.headers)

        # 发送请求
        content = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=content)

        if response.status == 200:
            content = response.read()
            self.parse_detail(content.decode('utf8'))
        else:
            print('出错了！', response.status)

    def parse_detail(self, content):
        obj = re.compile(r'<img.*class="BDE_Image".*src="(.*)".*>', re.S)
        pic_list = obj.findall(content)
        print(pic_list)


    def parse(self, content):
        content = content.decode('utf-8')
        obj = re.compile(r'<a\srel="noreferrer"\shref="(/p/.*)"', re.S)
        link_list = obj.findall(content)
        for link in link_list:
            detail_url = self.turl + link
            print(detail_url)
            self.send_detail_request(detail_url)

    # 爬取的图片存储到本地
    def write_content(self, content, name):
        path = 'tieba'
        if not os.path.exists(path):
            os.mkdir(path)
        with open(path + '/' + name, 'wb') as f:
            f.write(content)

    def write_html(self, content):
        with open('tieba.html', 'wb') as f:
            f.write(content)

    def start(self):
        kw = input("请输入爬取的贴吧名字")
        page = int(input("请输入你爬取多少页"))  # 5
        for i in range(1, page + 1):
            pn = (i - 1) * 50
            keyword = {'kw': kw, 'pn': pn, 'ie': 'utf-8'}
            result = urllib.parse.urlencode(keyword)
            full_url = self.url + result
            self.send_request(full_url)

if __name__ == '__main__':
    tbs = TieBaSpider()
    tbs.start()