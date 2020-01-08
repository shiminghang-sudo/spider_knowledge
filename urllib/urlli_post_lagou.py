import urllib.request
import urllib.parse
import ssl
ssl._create_default_https_context = ssl._create_unverified_context
import json

class LaGouSpider():
    def __init__(self):
        self.url = ''
        self.headers = {
            'User-Agent': '',
            'Referer': '',
            'Cookie': '',
        }
        self.result = []        # 保存数据

    def send_request(self, form_data):
        # 创建请求
        request = urllib.request.Request(url=self.url, data=form_data, headers=self.headers)
        # 发送请求
        response = urllib.request.urlopen(request)
        if response.status == 200:
            return response

    def parse(self, response):
        content = response.read().decode()  # 字符串
        dict_result = json.loads(content)   # 解析出json对象

        if not self.result:
            self.result = dict_result
        else:
            self.result['content']['positionResult']['result'] = self.result['content']['positionResult']['result'] \
                + dict_result.get('content').get('positionResult').get('result')


    def write_json(self, content):
        with open('position.json', 'a') as f:
            f.write(content + '\n')


    def start(self):
        for i in range(1, 3):
            form_data = {
                'first': 'true',
                'pn': '1',
                'kd': 'python'
            }
            form_data = urllib.parse.urlencode(form_data).encode('utf-8')
            response = self.send_request(form_data)
            if response:
                self.parse(response)
        self.write_json(json.dumps(self.result))    # 传输的时候必须转回字符串

if __name__ == '__main__':
    lg = LaGouSpider()
    lg.start()









