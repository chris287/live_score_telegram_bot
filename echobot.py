{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [],
   "source": [
    "import json\n",
    "import requests\n",
    "import time\n",
    "import urllib"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [],
   "source": [
    "TOKEN=\"1037188250:AAFnK4a1-NQpbO8Cz9TBv9YlU2Se4nNMVE8\"\n",
    "URL=\"https://api.telegram.org/bot{}/\".format(TOKEN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_url(url):\n",
    "    response = requests.get(url)\n",
    "    content = response.content.decode(\"utf8\")\n",
    "    return content"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_json_from_url(url):\n",
    "    content = get_url(url)\n",
    "    js = json.loads(content)\n",
    "    return js"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_updates(offset=None):\n",
    "    url = URL + \"getUpdates?timeout=100\"\n",
    "    if offset:\n",
    "        url += \"&offset={}\".format(offset)\n",
    "    js = get_json_from_url(url)\n",
    "    return js"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_last_update_id(updates):\n",
    "    update_ids = []\n",
    "    for update in updates[\"result\"]:\n",
    "        update_ids.append(int(update[\"update_id\"]))\n",
    "    return max(update_ids)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "def echo_all(updates):\n",
    "    for update in updates[\"result\"]:\n",
    "        try:\n",
    "            text = update[\"message\"][\"text\"]\n",
    "            chat = update[\"message\"][\"chat\"][\"id\"]\n",
    "            send_message(text, chat)\n",
    "        except Exception as e:\n",
    "            print(e)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [],
   "source": [
    "def get_last_chat_id_and_text(updates):\n",
    "    num_updates = len(updates[\"result\"])\n",
    "    last_update = num_updates - 1\n",
    "    text = updates[\"result\"][last_update][\"message\"][\"text\"]\n",
    "    chat_id = updates[\"result\"][last_update][\"message\"][\"chat\"][\"id\"]\n",
    "    return (text, chat_id)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "def send_message(text, chat_id):\n",
    "    text=urllib.parse.quote_plus(text)\n",
    "    url = URL + \"sendMessage?text={}&chat_id={}\".format(text, chat_id)\n",
    "    get_url(url)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [],
   "source": [
    "def main():\n",
    "    last_update_id = None\n",
    "    while True:\n",
    "        print(\"getting updates\")\n",
    "        updates = get_updates(last_update_id)\n",
    "        if len(updates[\"result\"]) > 0:\n",
    "            last_update_id = get_last_update_id(updates) + 1\n",
    "            echo_all(updates)\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n",
      "getting updates\n"
     ]
    }
   ],
   "source": [
    "if __name__ == '__main__':\n",
    "    main()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
