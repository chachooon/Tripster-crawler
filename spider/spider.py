from .models import NmapRaw
from bs4 import BeautifulSoup
import requests, json

class NmapRawScrapable():

    def reqlist(self,**kwargs):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        category = "DINING"
        x= kwargs['x']
        y= kwargs['y']
        xy_max = kwargs['max']
        xy_weight = kwargs['min']

        header = {
            'accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'accept-encoding':'gzip, deflate, br',
            'accept-language':'ko,en-US;q=0.9,en;q=0.8,pt;q=0.7,la;q=0.6',
            'cache-control':'max-age=0',
            'upgrade-insecure-requests':'1',
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        while x < x + xy_max:
            while y < y + xy_max:
                playload = {
                    'type': category,
                    'boundary': str(x)+';'+str(y)+';'+str(x + xy_weight)+';'+str(y + xy_weight),
                    'pageSize': '100'
                }
                req = requests.get(url, headers=header, params=playload)
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