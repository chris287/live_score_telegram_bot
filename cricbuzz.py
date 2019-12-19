import json
import requests
import urllib.request

class Cricketdata:
    CRICBUZZ_URL = "http://mapps.cricbuzz.com/cbzios/match/"

    TOKEN = "993779021:AAHrXJ0apOAqLZmzm-ylnXkp-laFhQZKlZo"
    BOT_URL = "https://api.telegram.org/bot{}/".format(TOKEN)

################################################COMMON URL DATA FETCHING#########################################################
    def get_url(url):
        headers={'User-Agent':'Mozilla/5.0','From':'roshalcr7@gmail.com'}
        response = requests.get(url)
        content = response.content.decode("utf8")
        return content

    def geturl_data(url):
        content = get_url(url)
        data = json.loads(content)
        return data
#################################################################################################################################

###############################################CRICKET DATA FETCHING METHODS#####################################################
    def get_live_matches():
        URL_LIVE_MATCHES = CRICBUZZ_URL+"livematches"
        data = geturl_data(URL_LIVE_MATCHES)
        final_list=list()
        final_string=""
        for items in data["matches"]:
            final_string=items["team1"]["name"]+" VS "+items["team2"]["name"]+","+items["series_name"]+" - "+items["header"]["match_desc"]
            final_list.append(final_string)
        return final_list
    
#################################################################################################################################
