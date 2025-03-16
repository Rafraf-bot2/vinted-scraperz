""" from pyVinted import Vinted

vinted = Vinted()

# search(url, number_of_items, page_number)
items = vinted.items.search("https://www.vinted.fr/catalog?search_text=jean&time=1741536357&order=newest_first&page=1",10,1)
#returns a list of objects: item
print(vars(items[0]))
 """

import os
from dotenv import load_dotenv

load_dotenv()  # Charge les variables depuis .env en local uniquement

TOKEN = os.getenv("DISCORD_BOT_TOKEN")

print(TOKEN)