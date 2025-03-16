""" from pyVinted import Vinted

vinted = Vinted()

# search(url, number_of_items, page_number)
items = vinted.items.search("https://www.vinted.fr/catalog?search_text=jean&time=1741536357&order=newest_first&page=1",10,1)
#returns a list of objects: item
print(vars(items[0]))
 """

import os
from dotenv import load_dotenv
import requests
import random

load_dotenv()  # Charge les variables depuis .env en local uniquement

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

NORDVPN_USER = os.getenv("NORDVPN_USER")
NORDVPN_PASS = os.getenv("NORDVPN_PASS")

proxy_list = [
    f"socks5://{NORDVPN_USER}:{NORDVPN_PASS}@amsterdam.nl.socks.nordhold.net:1080",
    f"socks5://{NORDVPN_USER}:{NORDVPN_PASS}@atlanta.us.socks.nordhold.net:1080",
    f"socks5://{NORDVPN_USER}:{NORDVPN_PASS}@dallas.us.socks.nordhold.net:1080",
    f"socks5://{NORDVPN_USER}:{NORDVPN_PASS}@los-angeles.us.socks.nordhold.net:1080",
    f"socks5://{NORDVPN_USER}:{NORDVPN_PASS}@nl.socks.nordhold.net:1080"
]

if not NORDVPN_USER or not NORDVPN_PASS:
    raise ValueError("❌ Erreur : NORDVPN_USER ou NORDVPN_PASS non définis dans .env")

# Sélectionner un proxy aléatoire
random_proxy = random.choice(proxy_list)

proxies = {
    "http": random_proxy,
    "https": random_proxy
}

# Tester la connexion via le proxy
try:
    response = requests.get("http://httpbin.org/ip", proxies=proxies, timeout=10)
    print("✅ Proxy utilisé :", random_proxy)
    print("📡 IP obtenue :", response.json())
except requests.exceptions.RequestException as e:
    print(f"❌ Erreur de connexion au proxy {random_proxy} : {e}")