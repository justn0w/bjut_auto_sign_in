from datetime import datetime, timedelta
import requests
import smtplib
from email.mime.text import MIMEText
import argparse



class Auto:
    date = ""  # 为前一天的日期
    cookie = {}
    userData = {}
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = password
        self.userData = {
            "username": username,
            "password": password
        }

    def login(self):
        cookieUrl = "https://itsapp.bjut.edu.cn/uc/wap/login/check"
        res = requests.post(url=cookieUrl, data=self.userData)
        headerContent = res.headers
        self.cookie = {
            "eai-sess": headerContent['Set-Cookie'].split(";")[0].split("=")[1],
            "UUkey": headerContent["Set-Cookie"].split(";")[4].split(",")[1].split("=")[1]
        }

    def createDate(self):
        now = datetime.now()
        saveNow = now - timedelta(days=1)
        self.date = saveNow.strftime("%Y%M%d")

    def save(self):
        data = {
            "address": "北京市朝阳区劲松街道蓝悦园",
            "area": "北京市  朝阳区",
            "bztcyy": "",
            "city": "北京市",
            "created": 1603068320,
            "date": self.date,  # 此data为当前日期的前一天
            "dqjzzt": "1",
            "fjhbcc": "",
            "fjjtgj": "",
            "fjq_city": "",
            "fjq_province": "",
            "fjq_szdz": "",
            "fjqszgj": "",
            "fjrq": "",
            "fjyy": "",
            "fxyy": "上学",
            "geo_api_info": {
                "type": "complete",
                "info": "SUCCESS",
                "status": 1,
                "ZDa": "jsonp_416174_",
                "position": {
                    "Q": 39.88495,
                    "R": 116.48048,
                    "lng": 116.48048,
                    "lat": 39.88495
                },
                "message": "Get ipLocation success.Get address success.",
                "location_type": "ip",
                "accuracy": "null",
                "isConverted": "true",
                "addressComponent": {
                    "citycode": "010",
                    "adcode": "110105",
                    "businessAreas": [
                        {
                            "name": "大郊亭",
                            "id": "110105",
                            "location": {
                                "Q": 39.888761,
                                "R": 116.48342100000002,
                                "lng": 116.483421,
                                "lat": 39.888761
                            }
                        },
                        {
                            "name": "百子湾",
                            "id": "110105",
                            "location": {
                                "Q": 39.894565,
                                "R": 116.490882,
                                "lng": 116.490882,
                                "lat": 39.894565
                            }
                        },
                        {
                            "name": "南磨房",
                            "id": "110105",
                            "location": {
                                "Q": 39.883719,
                                "R": 116.47472800000003,
                                "lng": 116.474728,
                                "lat": 39.883719
                            }
                        }],
                    "neighborhoodType": "",
                    "neighborhood": "",
                    "building": "",
                    "buildingType": "",
                    "street": "西大望路",
                    "streetNumber": "27号",
                    "country": "中国",
                    "province": "北京市",
                    "city": "",
                    "district": "朝阳区",
                    "township": "劲松街道"
                },
                "formattedAddress": "北京市朝阳区劲松街道蓝悦园",
                "roads": [],
                "crosses": [],
                "pois": []
            },
            "glksrq": "",
            "gllx": "",
            "gtjzzfjsj": "",
            "gwszdd": "",
            "id": 4571828,
            "ismoved": 0,
            "jcbhlx": "",
            "jcbhrq": "",
            "jchbryfs": "",
            "jcjg": "",
            "jcjgqr": "0",
            "jcqzrq": "",
            "jcwhryfs": "",
            "jhfjhbcc": "",
            "jhfjjtgj": "",
            "jhfjrq": "",
            "jrfjhbcc": "",
            "jrfjjtgj": "",
            "jrsfqzfy": "",
            "jrsfqzys": "",
            "ljhbcc": "",
            "ljjtgj": "",
            "ljrq": "",
            "province": "北京市",
            "qksm": "",
            "remark": "",
            "sfcxtz": "0",
            "sfcxzysx": "0",
            "sfcyglq": "0",
            "sfjcbh": "0",
            "sfjchbry": "0",
            "sfjcqz": "",
            "sfjcwhry": "0",
            "sfsfbh": "0",
            "sfsqhzjkk": "",
            "sftjhb": "0",
            "sftjwh": "0",
            "sfxxxbb": "",
            "sfygtjzzfj": 0,
            "sfyqjzgc": "",
            "sfyyjc": 0,
            "sfzx": "1",
            "sqhzjkkys": "",
            "szgj": "",
            "szsqsfty": "",
            "szsqsfybl": 0,
            "tw": "3",
            "uid": "72940",
            "xjzd": ""
        }
        url = "https://itsapp.bjut.edu.cn/ncov/wap/default/save" #提交数据url
        res = requests.post(url=url, data=data, cookies=self.cookie)
        return res

def main(username, password):
    auto = Auto(username, password)
    print("创建用实例")
    auto.createDate()
    print("获取时间")
    auto.login()
    print("获取cookie")
    return auto.save()
    
        


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="输入用户名和密码")
    parser.add_argument('--username', type=str, default=None)
    parser.add_argument('--password', type=str, default=None)
    args = parser.parse_args()
    rs = main(args.username, args.password)
    print("获取打卡结果:" + rs.json()['m'])

        
