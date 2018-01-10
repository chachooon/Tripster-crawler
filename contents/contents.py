from urllib.request import Request, urlopen
import json
import csv
#API Key list
class crawler:
    def __init__(self):
        self.radius = 500
        self.start_point
        self.end_point
        self.cur_point
        self.keyList = self.set_key_list()
        self.index = 0
        self.api_key = self.get_API_KEY(index)
        self.query = "https://maps.googleapis.com/maps/api/place/details/json?"

    def set_radius(self,radius):
        self.radius = radius

    def set_start_point(self, lat, lng):
        self.start_point = [lat, lng]
        return self.start_point

    def set_end_location(self, lat, lng):
        self.end_point = [lat, lng]
        return self.end_point

    def set_key_list(self):
        tmpSet = set()
        keys = open('apiKeyList.txt', 'r', encoding='utf-8').readlines()
        self.index = 0
        for key in keys:
            tmpSet.add(key)
        self.keyList = list(tmpSet)

    def get_API_KEY(self, index=None):
        if index is None:
            self.index = 0
        elif type(index) == int and index < self.keyList.length:
            self.index = index

        return self.keyList[index]

    def change_API_KEY(self):
        self.index += 1
        return self.get_API_KEY(self.index)

    def set_query(self, location, type=["search","detail"]):
        url = "http" + location + str(self.radius)

    def send_request(self, location):
        url = ""
        index = 1
        self.get_API_Key(index)
        return url

    def store(self, data):
        self.send_db

    def iter(self, start, end, radius):
        lat_iter = ((end[0] - start[0]) / radius) + 1
        lng_iter = ((end[1] - start[1]) / radius) + 1
        for i in range(0, lng_iter):
            for j in range(0, lat_iter):
                location= ""
                data = self.send_request(location)
                if data['status'] == "OK":
                    self.store(data)
                elif data["status"] == "OVER_QUERY_LIMIT":
                    while data["status"] == "OVER_QUERY_LIMIT":
                        self.change_API_KEY()
                        self.send_request(self.location)
                    self.store(data)




    # 서울 맛집 리스트 파일 열기
    with open("seoul_res_list.txt", "r", encoding="utf-8") as data:
        # 전체 맛집 상세 정보를 담을 객체 선언
        contents_detail = {}
        # 맛집 리스트 읽기
        lines = data.readlines()

        # API Key 리스트 인덱스
        index = 0
        # API Key 선택
        api = api_list[index]

        for line in lines:
            # 맛집 기본 정보를 담을 객체 선언
            tmp_dict = {}
            # 요청 쿼리 작성
            url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + line.rstrip('\n') + "&key=" + api

            # 요청 정보 반환
            raw_result = urlopen(url).read().decode('utf8')
            json_result = json.loads(raw_result)

            if json_result['status'] == "OK":
                dict = json_result["result"]
                # 마지막으로 검색한 맛집의 ID
                last_id = dict["place_id"]
                # 후기 4.0 이상의 맛집 정보 검색
                if "rating" in dict:
                    tmp_dict["Category_ID"] = 1
                    tmp_dict["Contents_Title"] = dict["name"]
                    tmp_dict["Contents_Keyword"] = dict["types"]
                    tmp_dict["Contents_Location"] = dict["formatted_address"]
                    tmp_dict["Contents_Country"] = "Korea"
                    tmp_dict["Contents_City"] = "Seoul"
                    tmp_dict["Contents_Rating"] = dict["rating"]
                    tmp_dict["Contents_View_Cnt"] = 0
                    tmp_dict["Contents_Review_Cnt"] = 0
                    tmp_dict["Contents_Scrap_Cnt"] = 0
                    tmp_dict["Contents_Thumbnail"] = ""
                    tmp_dict["Contents_Target"] = "google"
                    tmp_dict["Contents_Target_ID`"] = dict["place_id"]

                    if "international_phone_number" in dict:
                        contents_detail["Contents_Tel"] = dict["international_phone_number"]
                    if "opening_hours" in dict:
                        contents_detail["Contents_Time"] = dict["opening_hours"]
                    contents_detail["Contents_Lat"] = dict["geometry"]["location"]["lat"]
                    contents_detail["Contents_Long"] = dict["geometry"]["location"]["lng"]

                    # 리뷰 정보 저장
                    if "reviews" in dict:
                        reviews = dict["reviews"]
                        str = ""
                        for review in reviews:
                            if "language" in review:
                                if review["language"] == "ko":
                                    str = str + " " + review["text"]
                        contents_detail["reviews"] = str
                else:
                    continue

            # API Key 교체 및 재검색 요청
            elif json_result['status'] == "OVER_QUERY_LIMIT":
                # API Key 교체
                while json_result['status'] == "OVER_QUERY_LIMIT":
                    index += 1
                    # API Key를 전부 소모한 경우, while 문 break
                    if index > 12:
                        break

                    # API Key, 요청 쿼리 교체
                    api = api_list[index]
                    url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + line.rstrip(
                        '\n') + "&key=" + api
                    # 재검색
                    raw_result = urlopen(url).read().decode('utf8')
                    json_result = json.loads(raw_result)

                # API Key를 전부 소모한 경우, for문 break(검색 중지)
                if index > 12:
                    print("할당량 사용 완료")
                    with open("tbl_Contents(Seoul).json", 'a', encoding="utf-8") as tbl_contents:
                        tbl_contents.write("]")
                    break
                print(api)
                # API Key 소모로 인해 검색하지 정보 재요청
                if json_result['status'] == "OK":
                    dict = json_result["result"]
                    last_id = dict["place_id"]
                    if "rating" in dict:
                        tmp_dict["Category_ID"] = 1
                        tmp_dict["Contents_Title"] = dict["name"]
                        tmp_dict["Contents_Keyword"] = dict["types"]
                        tmp_dict["Contents_Location"] = dict["formatted_address"]
                        tmp_dict["Contents_Country"] = "Korea"
                        tmp_dict["Contents_City"] = "Seoul"
                        tmp_dict["Contents_Rating"] = dict["rating"]
                        tmp_dict["Contents_View_Cnt"] = 0
                        tmp_dict["Contents_Review_Cnt"] = 0
                        tmp_dict["Contents_Scrap_Cnt"] = 0
                        tmp_dict["Contents_Thumbnail"] = ""
                        tmp_dict["Contents_Target"] = "google"
                        tmp_dict["Contents_Target_ID`"] = dict["place_id"]

                        if "international_phone_number" in dict:
                            contents_detail["Contents_Tel"] = dict["international_phone_number"]
                        if "opening_hours" in dict:
                            contents_detail["Contents_Time"] = dict["opening_hours"]
                        contents_detail["Contents_Lat"] = dict["geometry"]["location"]["lat"]
                        contents_detail["Contents_Long"] = dict["geometry"]["location"]["lng"]

                        if "reviews" in dict:
                            reviews = dict["reviews"]
                            str = ""
                            for review in reviews:
                                if "language" in review:
                                    if review["language"] == "ko":
                                        str = str + " " + review["text"]
                            contents_detail["reviews"] = str

            # 맛집 기본 정보 파일에 데이터 추가
            with open("tbl_Contents(Seoul).json", 'a', encoding="utf-8") as tbl_contents:
                json.dump(tmp_dict, tbl_contents)
                tbl_contents.write(",")
            # 맛집 상세 정보 파일에 데이터 추가
            with open("tbl_Contents_Detail(Seoul).json", "a", encoding="utf-8") as tbl_contents_review:
                json.dump(contents_detail, tbl_contents_review)
                tbl_contents_review.write(",")

        # 마지막으로 검색한 맛집 ID 출력
        print(last_id)
        with open("tbl_Contents(Seoul).json", 'a', encoding="utf-8") as tbl_contents:
            tbl_contents.write("]")




            #파리 맛집 상세 검색
# csv.field_size_limit(1320720)

# with open("paris_res_list.txt", 'r', encoding="utf-8") as data:
#     lines = data.readlines()
#     tmp_list = []
#     i = 1
#     for line in lines:
#         if i > 999:
#             break
#
#         url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + line.rstrip(
#             '\n') + "&key=AIzaSyCVA7jyxKbkKQ9ZQ7IlXU0kNk6nM0DnJnY"
#         print(url)
#         raw_result = urlopen(url).read().decode('utf8')
#         json_result = json.loads(raw_result)
#
#         if json_result['status'] == "OK":
#             print(json_result['result'])
#             tmp_list.append(json_result['result'])
#         i += 1
#
#     with open('paris_res_detail1.json', 'w', encoding='utf-8') as file:
#         json.dump(tmp_list, file)
#
# file.close()

#서울 리스트 검색
# text_file = "seoul_res_list.txt"
# with open(text_file, "w", encoding="utf-8") as list:
#     location = ""
#     lat = 37.454508
#     tmp_set = set([])
#
#     for i in range(1, 31):
#         lat += 0.007229
#         long = 126.893332
#         for j in range(1, 21):
#             long += 0.010672
#             location = str(lat) + "," + str(long)
#             url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location=" + location + "&radius=500&type=restaurant&key=AIzaSyCyy3h26NFVr2pKno-1q6KmhkWLZ-bGlSM"
#             print(url)
#             raw_result = urlopen(url).read().decode('utf8')
#             json_result = json.loads(raw_result)
#             if json_result['status'] == "OK":
#                 for dict in json_result["results"]:
#                     tmp_set.add(dict["place_id"])
#
#     for element in tmp_set:
#         list.write(element+"\n")
#     list.close()

#파리 리스트 검색v2.0
# text_file = "paris_res_list.txt"
# with open(text_file, "w", encoding="utf-8") as list:
#     location = ""
#     lat = 48.831946
#     tmp_set = set([])
#
#     for i in range(1, 20):
#         lat += 0.007229
#         long = 2.280501
#         for j in range(1, 26):
#             long += 0.010672
#             location = str(lat) + "," + str(long)
#             url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location=" + location + "&radius=500&type=restaurant&key=AIzaSyCb1-Itd2i_3RlBDhbMBYhb9uL6V7HdX6g"
#             print(url)
#             raw_result = urlopen(url).read().decode('utf8')
#             json_result = json.loads(raw_result)
#             if json_result['status'] == "OK":
#                 for dict in json_result["results"]:
#                     tmp_set.add(dict["place_id"])
#
#     for element in tmp_set:
#         list.write(element)
#     list.close()


# #test
# with open('paris_res.txt', 'w', encoding='utf-8') as paris:
#     with open("paris_res_list.txt", "r", encoding="utf-8") as list:
#         lines = list.readlines()
#         s = set([])
#         for line in lines:
#             s.add(line)
#
#     for element in s:
#         paris.write(element)
#     print(s)

#파리 리스트 검색v1.0
# text_file = "paris_res_list.txt"
# writeFp = open(text_file, "w", encoding="utf-8")
#
# location = ""
# lat = 48.831946
# long = 2.280501
#
# for i in range(1,20):
#     lat += 0.003610
#     for j in range(1,26):
#         long += 0.005336
#         location = str(lat)+","+str(long)
#         url = "https://maps.googleapis.com/maps/api/place/radarsearch/json?location=" + location + "&radius=500&type=restaurant&key=AIzaSyCb1-Itd2i_3RlBDhbMBYhb9uL6V7HdX6g"
#         print(url)
#         raw_result = urlopen(url).read().decode('utf8')
#         json_result = json.loads(raw_result)
#         if json_result['status'] == "OK":
#             for dict in json_result["results"]:
#                 writeFp.write("{}\n".format(dict["place_id"]))
# writeFp.close()

#맛집 디테일 검색
# csv.field_size_limit(1320720)
#
# with open("google_list.txt", 'r', encoding="utf-8") as data:
#     lines = data.readlines()
#     list = []
#     for line in lines:
#         url = "https://maps.googleapis.com/maps/api/place/details/json?placeid=" + line.rstrip('\n') + "&key=AIzaSyDyEoRnEfplKfGuKfBuuQMjaqOppEpm4LU"
#         raw_result = urlopen(url).read().decode('utf8')
#         json_result = json.loads(raw_result)
#         if json_result['status'] == "OK":
#             print(json_result['result'])
#             list.append(json_result['result'])
#
#     with open('google_detail.json', 'w', encoding='utf-8') as file:
#         json.dump(list, file)
#
# file.close()

# result = json.loads(raw_result)
#
# addr_detail = result['results'][0]
#
# https://maps.googleapis.com/maps/api/place/radarsearch/json?location=48.859294,2.347589&rankby=prominence&type=restaurant&keyword=?????&key=YOUR_API_KEY
# language=
# radius=50000
# #이전 검색 결과의 다음 검색 결과 반환
# pagetoken
#
# https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=-33.8670522,151.1957362&radius=500&type=restaurant&key=YOUR_API_KEY
#
# # 리스트 반환
# https://maps.googleapis.com/maps/api/place/radarsearch/json?location=51.503186,-0.126446&radius=5000&type=restaurant&key=AIzaSyCb1-Itd2i_3RlBDhbMBYhb9uL6V7HdX6g
# # ID 상세 검색
# https://maps.googleapis.com/maps/api/place/details/json?placeid=ChIJZewrLtIEdkgRtl2nZKboAgk&key=AIzaSyCb1-Itd2i_3RlBDhbMBYhb9uL6V7HdX6g
# https://maps.googleapis.com/maps/api/place/details/json?placeid=8e0f89833f4e273bfb9224e995b93c220318085c&key=AIzaSyCb1-Itd2i_3RlBDhbMBYhb9uL6V7HdX6g