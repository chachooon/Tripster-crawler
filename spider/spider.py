from .models import NmapList#, NmapContents
from bs4 import BeautifulSoup
import requests, json

class NmapListScrapable():
    def request(self,**kwargs):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        category = "DINING"
        x= kwargs['x']
        y= kwargs['y']
        max = kwargs['max']

        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        while x < x + max:
            while y < y + max:
                playload = {
                    'type': category,
                    'boundary': str(x+0.0000001)+';'+str(y+0.0000001)+';'+str(x + 0.02)+';'+str(y + 0.02),
                    'pageSize': '100'
                }
                req = requests.get(url, headers=header, params=playload)
                r = req.json()
                results = list(req.json()['result']['site'])
                for result in results:
                    id = int(result['id'][1:])
                    find_id = NmapList.objects.filter(id=id).count()
                    if find_id<1:
                        con = NmapContentsScrapable()
                        contents = con.request(id)['business']
                        c = type(contents)
                        NmapList.objects.create(
                            id = id,
                            name = result['name'],
                            category = category,
                            x = result['x'],
                            y = result['y'],
                            contents = contents
                        )
        return NmapList.objects.all()

class NmapContentsScrapable():
    def request(self, id):
        url = 'https://store.naver.com/restaurants/detail?'
        header = {}
        playload = {
            'id': id
        }
        req = requests.get(url, headers=header, params=playload)
        soup = BeautifulSoup(req.text, 'html.parser')
        soup_parse = soup.footer.next_sibling.string.split('window.PLACE_STATE=')[1]
        result = json.loads(soup_parse)
        return result
