from .models import NmapList, NmapBoundaryList #, NmapContents
from bs4 import BeautifulSoup
import requests, json, asyncio

class NmapContentsScrapable():
    async def request(self,**kwarg):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        header = {
            'user-agent':'Mozilla/5.0'
            # +'(Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }
        category = kwarg['category']
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
                return 400
        else:
            print(res)
            return 400

    async def create(self, **kwarg):
        results = kwarg['results']
        if results != 400:
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
                            category=kwarg['category'],
                            x=result['x'],
                            y=result['y'],
                            # contents = contents
                        )
                except: pass

    async def iter(self):
        category = 'category'
        x_min = 12500
        x_max = 13100
        x = x_min
        y_min = 3300
        y_max = 3900
        y = y_min
        y_pass = []

        for x in range(x_min, x_max):
            if y in y_pass:
                x += 20
                y_pass.pop(y)
            else:
                x += 10

            for y in range(y_min, y_max):
                boundary = str(round(x * 0.01,7))+';'+str(round(y * 0.01,7))+';'+ \
                           str(round((x+20)* 0.01,7))+';'+str(round((y+20)* 0.01,7))
                results = await self.request(
                    boundary=boundary,
                    category=category
                )

                if results != 400:
                    await self.create(
                        results=results,
                        category=category
                    )
                    y += 20
                    self.y_pass.append(y).append(y)
                    NmapBoundaryList.objects.create(boundary=boundary)
                else:
                    y += 10




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
