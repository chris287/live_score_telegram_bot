import json
import requests
import urllib


CRICBUZZ_URL = "http://mapps.cricbuzz.com/cbzios/match/"

TOKEN = "993779021:AAHrXJ0apOAqLZmzm-ylnXkp-laFhQZKlZo"
URL = "https://api.telegram.org/bot{}/".format(TOKEN)

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
#################################################################################################################################
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
def get_updates(offset=None):
    url = URL + "getUpdates?timeout=100"
    if offset:
        url += "&offset={}".format(offset)
    js = geturl_data(url)
    return js


def get_last_update_id(updates):
    update_ids = []
    for update in updates["result"]:
        update_ids.append(int(update["update_id"]))
    return max(update_ids)

def get_last_chat_id_and_text(updates):
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    return (text, chat_id)


def send_message(text, chat_id, reply_markup=None):
    text = urllib.parse.quote_plus(text)
    url = URL + \
        "sendMessage?text={}&chat_id={}&parse_mode=Markdown".format(
            text, chat_id)
    if reply_markup:
        url += "&reply_markup={}".format(reply_markup)
    get_url(url)


def build_keyboard(items):
    keyboard = [[item] for item in items]
    reply_markup = {"Keyboard": keyboard, "one_time_keyboard": True}
    return json.dumps(reply_markup)

def handle_updates(updates):
    for update in updates["result"]:
        try:
            text = update["message"]["text"]
            chat = update["message"]["chat"]["id"]
            items = get_live_matches()
            
            if text == "/matches":
                #keyboard = build_keyboard(items)
                #send_message("Live Matches", chat, keyboard) 
                
                i=0
                while(i<len(items)):
                    message = "\n\n\n"+str(i)+"\n\n\n".join(items)
                    i+=1
                send_message(message, chat) 

            else:
                send_message("Under Devolopment.Comming Soon!!!",chat)   
        except KeyError:
            pass

def main():
    last_update_id = None
    while True:
        updates = get_updates(last_update_id)
        if len(updates["result"]) > 0:
            last_update_id = get_last_update_id(updates) + 1
            handle_updates(updates)

if __name__ == '__main__':
    main() 