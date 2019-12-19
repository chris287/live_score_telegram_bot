import json
import requests
from urllib.request import Request,urlopen

url="http://mapps.cricbuzz.com/cbzios/match/livematches"

def geturl(url):
    headers={'User-Agent': 'Mozilla/5.0','From':'roshalcr7@gmail.com'}
    response = requests.get(url,headers=headers)
    content = response.content.decode("utf8")
    return content

def get_data_from_url(url):
    content = geturl(url)
    js=json.loads(content)
    return js

def main():
    js = get_data_from_url(url)
    print(js)


if __name__ == '__main__':
    main()