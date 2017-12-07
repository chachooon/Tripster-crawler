from selenium import webdriver
import urllib.parse, json



longitude = 126.7
latitude = 37.4
longitude_max = 127.3
latitude_max = 37.8

browser = webdriver.PhantomJS()
browser.implicitly_wait(3)

while longitude < longitude_max and latitude < latitude_max:

    data = {
        'type':'DINING',
        'boundary':str(longitude) +';'+ str(latitude) +';'+ str(longitude + 0.02) +';'+ str(latitude + 0.02) ,
        'pageSize':'100'
    }
    url = "http://map.naver.com/search2/interestSpot.nhn?" + urllib.parse.urlencode(data)
    browser.get(url)
    result = browser.find_element_by_tag_name('pre').text
    result = json.loads(result)
    longitude = longitude + 0.02
    latitude = latitude + 0.02

    print(result['result']['site'])

browser.quit()