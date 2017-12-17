from .models import NmapList, NmapBoundaryList #, NmapContents
from bs4 import BeautifulSoup
import requests, json, asyncio

class NmapListScrapable():

    def request(self,**kwarg):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        header = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36'
            # 'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
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
                if len(results)==100:
                    return boundary
                else:
                    cnt = self.create(results=results, category=category)
                    NmapBoundaryList.objects.create(boundary=results, cnt=cnt)
                    print(str(cnt)+'건 - '+boundary)
                    return 1

    def create(self, **kwarg):
        results = kwarg['results']
        cnt =0
        for result in results:
            try:
                id = int(result['id'][1:])
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
                cnt += 1
            except: pass
        return cnt


    def iter(self):
        category = 'DINING'
        x_min = 126000#12500
        x_max = 128000#13100
        y_min = 36000#3300
        y_max = 38000#3900


        for x in range(x_min, x_max):
            print('x:'+str(x))
            for y in range(y_min, y_max):
                boundary = str(round(x * 0.001,7))+';'+str(round(y * 0.001,7))+';'+ \
                           str(round((x+200)* 0.001,7))+';'+str(round((y+200)* 0.01,7))
                results = self.request(boundary=boundary, category=category)
                if results != 1:
                    for xx in range(0,10):
                        for yy in range(0,10):
                            boundary = str(round(x * 0.001, 7)) + ';' + str(round(y * 0.001, 7)) + ';' + \
                                       str(round((x + 20) * 0.01, 7)) + ';' + str(round((y + 20) * 0.01, 7))
                            result = self.request(boundary=boundary, category=category)
                            if result != 1:
                                for xxx in range(0, 20):
                                    for yyy in range(0,20):
                                        boundary = str(round(x * 0.001, 7)) + ';' + str(round(y * 0.001, 7)) + ';' + \
                                                   str(round((x + 1) * 0.01, 7)) + ';' + str(round((y + 1) * 0.01, 7))
                                        self.request(boundary=boundary, category=category)
                                        y += 2
                                    x += 2
                            y += 20
                        x += 20

                y += 200
            x += 200



# class NmapContentsScrapable():
#     def request(self, id):
#         url = 'https://store.naver.com/restaurants/detail?'
#         header = {}
#         playload = {
#             'id': id
#         }
#         req = requests.get(url, headers=header, params=playload)
#         soup = BeautifulSoup(req.text, 'html.parser')
#         soup_parse = soup.footer.next_sibling.string.split('window.PLACE_STATE=')[1]
#         result = json.loads(soup_parse)
#         return result
