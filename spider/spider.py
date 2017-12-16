from .models import NmapList, NmapBoundaryList #, NmapContents
from bs4 import BeautifulSoup
import requests, json
import time, asyncio

class NmapListScrapable():



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

async def iterator():
    y = 3300
    y_pass = []
    async for x in range(12500, 13100):
        if y in y_pass:
            y_pass.pop(y)
            x += 20
        else: x += 10
        for y in range(3300, 3900):
            end_x = x + 20
            end_y = y + 20
            boundary = str(round(x * 0.01,7))+';'+str(round(y * 0.01,7))+';'+str(round(end_x * 0.01,7))+';'+str(round(end_y * 0.01,7))
            results = self.request(boundary=boundary)
            if results != 0:
                NmapBoundaryList.objects.create(boundary=boundary)
                y_pass.append(y).append(y)
                y += 20
                return results
            else:
                y += 10
            return 0

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
