import requests
import time

unix_time = int(time.time())

cookie = f"t={unix_time};"

key = "西安"

url = f"https://search.sohu.com/search/meta"


head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:120.0) Gecko/20100101 Firefox/120.0",
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "https://search.sohu.com/?queryType=outside&keyword={key}",
    "X-Requested-With": "XMLHttpRequest",
    "Cookie": cookie,
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
}


data = {
    "keyword": key,
    "terminalType": "pc",
    "SUV": f"{unix_time * 1000}asdfgh",
    "from": "0",
    "size": "10",
    "searchType": "news",
    "queryType": "outside",
    "pvId": f"{unix_time * 1000}qwerty",
    "refer": "https%3A//www.sohu.com/",
    "size": "10",
    "maxL": "15",
    "spm": "",
    "_": unix_time * 1000,
}


res = requests.get(url, params=data, headers=head).json()
news = res["data"]["news"]
for new in news:
    print(new["brief"])
