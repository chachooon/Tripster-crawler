from .models import NmapRaw
from bs4 import BeautifulSoup
import requests, json

class NmapRawScrapable():

    def reqlist(self,**kwargs):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        category = "DINING"
        x= 127
        y= 37
        max = kwargs['max']
        min = kwargs['min']

        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        while x < x + 1:
            while y < y + 1:
                playload = {
                    'type': category,
                    'boundary': str(x+0.0000001)+';'+str(y+0.0000001)+';'+str(x +0.02)+';'+str(y +0.02),# '127.0248326;37.4818077;127.0455129;37.4967971', #
                    'pageSize': '100'
                }
                req = requests.get(url, headers=header, params=playload)
                r = req.json()
                results = list(req.json()['result']['site'])
                for result in results:
                    yield result

    def reqdata(self, **kwargs):
        url = 'https://store.naver.com/restaurants/detail?'
        header = {
        }
        for list in self.reqlist(**kwargs):
            playload = {
                'id': list['id'][1:]
            }
            req = requests.get(url, headers=header, params=playload)
            soup = BeautifulSoup(req.text, 'html.parser')
            soup_parse = soup.footer.next_sibling.string.split('window.PLACE_STATE=')[1]
            detail = json.loads(soup_parse)
            resultset = {
                'category': 'DINING',
                'list': list,
                'detail': detail
            }
            yield resultset

    def create(self,**kwargs):
        for resultset in self.reqdata(**kwargs):
            NmapRaw.objects.create(
                category=resultset['category'],
                list=resultset['list'],
                contents=resultset['detail']
            )
        return NmapRaw.objects.all()