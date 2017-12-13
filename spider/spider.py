from .models import NmapList#, NmapContents
from bs4 import BeautifulSoup
import requests, json
import time

class NmapListScrapable():
    def request(self):
        url = "http://map.naver.com/search2/interestSpot.nhn?"
        category = "DINING"
        x= 126.0 #125.0
        y= 37.0 #33.0

        header = {
            'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36'
        }

        while x < 128: #131:
            while y < 38: #39:
                boundary = str(round(x,7))+';'+str(round(y,7))+';'+str(round((x + 0.01),7))+';'+str(round((y + 0.01),7))
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
                        for result in results:
                            try:
                                id = int(result['id'][1:])
                                find_id = NmapList.objects.filter(id=id).count()
                                if find_id<1:
                                    # con = NmapContentsScrapable()
                                    # contents = con.request(id)['business']
                                    # c = type(contents)
                                    NmapList.objects.create(
                                        id = id,
                                        name = result['name'],
                                        category = category,
                                        x = result['x'],
                                        y = result['y'],
                                        # contents = contents
                                    )

                            except:
                                pass
                        print('***** '+ str(res) + ' : ' + boundary)
                        time.sleep(3)
                    else:
                        print(str(res) + ' : ' + boundary)
                        print(respond.json())
                        x += 0.0000001
                        y += 0.0000001
                else:
                    print(str(res)+' : '+boundary)
                    x += 0.0000001
                    y += 0.0000001
                x += 0.01
                y += 0.01
        # return NmapList.objects.all()

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
