from bs4 import BeautifulSoup
import requests, json

class Navermap():
    def __init__(self, category, type, min_x, min_y, max_x, max_y):
        self.category = category
        self.type = type
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.range = 0.02
        self.header = {}

    def setdata(self, category, type, min_x, min_y, max_x, max_y, range):
        self.category = category
        self.type = type
        self.min_x = min_x
        self.min_y = min_y
        self.max_x = max_x
        self.max_y = max_y
        self.range = range

    def reqlist(self):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        x = self.min_x
        y = self.min_y
        while x < self.max_x:
            while y < self.max_y:
                playload = {
                    'type': self.type,
                    'boundary': str(x)+';'+str(y)+';'+str(x + self.range)+';'+str(y + self.range),
                    'pageSize': '100'
                }
                req = requests.get(url, headers=self.header, params=playload)
                results = req.json()['result']['site']
                for i in results:
                    list = results[i]
                    yield list

    def reqdata(self):
        url = 'https://store.naver.com/restaurants/detail?'
        for list in self.reqlist():
            playload = {
                'id': list['id'][1:]
            }
            req = requests.get(url, headers=self.header, params=playload)
            soup = BeautifulSoup(req.text, 'html.parser')
            soup_parse = soup.footer.next_sibling.string.split('window.PLACE_STATE=')[1]
            detail = json.loads(soup_parse)
            resultset = {
                'category': self.category,
                'list': list,
                'detail': detail
            }
            yield resultset

    def insdata(self):
        count = 0
        for resultset in self.reqdata():
            Rawdata.objects.create(
                category=resultset['category'],
                list=resultset['list'],
                detail=resultset['detail']
            )
            print('insert data : '+ str(++count))

#
# new = Navermap()
# new.setdata('Navermap','DINING', 126.7, 37.4, 126.7, 37.4, 0.02)
# new.insdata()
#
