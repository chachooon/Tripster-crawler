from .models import NmapList, NmapBoundaryList #, NmapContents
from bs4 import BeautifulSoup
import requests, json, asyncio

class test:
    def __init__(self):
        self.category = 'category'
        self.x_min = 12500
        self.x_max = 13100
        self.x = self.x_min
        self.y_min = 3300
        self.y_max = 3900
        self.y = self.y_min
        self.y_pass = []


    async def xiter(self):
        for self.x in range(self.x_min, self.x_max):
            if self.y in self.y_pass:
                yield self.x += 20
                self.y_pass.pop(y)
            else:
                yield self.x += 10

    async def yiter(self):
        self.x = await self.xiter()
        for self.y in range(self.y_min, self.y_max):
            boundary = str(round(self.x * 0.01,7))+';'+str(round(self.y * 0.01,7))+';'+ \
                       str(round((self.x+20)* 0.01,7))+';'+str(round((self.y+20)* 0.01,7))
            results = await self.request(boundary=boundary)
            if results != 400:
                yield results
                y += 20
                self.y_pass.append(y).append(y)
                NmapBoundaryList.objects.create(boundary=boundary)
            else:
                yield results
                y += 10

    async def request(self,**kwarg):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        header = {
            'user-agent':'Mozilla/5.0'# +'(Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        category = "DINING"
        boundary = kwarg['boundary']
        playload = {
            'type': category,
            'boundary': boundary,
            'pageSize': '100'
        }
        respond = requests.get(url, headers=header, params=playload)
        res = respond.status_code
        if res == 200:
            if 'result' in respond.json():
                results = list(respond.json()['result']['site'])
                NmapBoundaryList.objects.create(boundary=boundary)
                print(boundary)
                return results
            else:
                print(res)
                return 0
        else:
            print(res)
            return 0

    async def create(self, results):
        category = "DINING"
        if results != 0:
            for result in results:
                try:
                    id = int(result['id'][1:])
                    find_id = NmapList.objects.filter(id=id).count()
                    if find_id < 1:
                        # con = NmapContentsScrapable()
                        # contents = con.request(id)['business']
                        # c = type(contents)
                        NmapList.objects.create(
                            id=id,
                            name=result['name'],
                            category=category,
                            x=result['x'],
                            y=result['y'],
                            # contents = contents
                        )
                except:
                    pass


class NmapListSpider():

    async def request(self,**kwarg):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        category = "DINING"
        boundary = kwarg['boundary']
        playload = {
            'type': category,
            'boundary': boundary,
            'pageSize': '100'
        }
        respond = requests.get(url, headers=header, params=playload)
        res = respond.status_code
        if res == 200:
            if 'result' in respond.json():
                results = list(respond.json()['result']['site'])
                NmapBoundaryList.objects.create(boundary=boundary)
                print(boundary)
                return results
            else:
                print(res)
                return 0
        else:
            print(res)
            return 0

    async def create(self, results):
        category = "DINING"
        if results != 0:
            for result in results:
                try:
                    id = int(result['id'][1:])
                    find_id = NmapList.objects.filter(id=id).count()
                    if find_id < 1:
                        # con = NmapContentsScrapable()
                        # contents = con.request(id)['business']
                        # c = type(contents)
                        NmapList.objects.create(
                            id=id,
                            name=result['name'],
                            category=category,
                            x=result['x'],
                            y=result['y'],
                            # contents = contents
                        )
                except:
                    pass



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
