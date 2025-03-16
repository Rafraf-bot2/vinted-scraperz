# Description: Bot Discord qui permet de rechercher des articles sur Vinted à partir d'un lien.
import discord
from pyVinted import Vinted

import os
from dotenv import load_dotenv
import random

load_dotenv()  # Charge les variables depuis .env en local uniquement

TOKEN = os.getenv("DISCORD_BOT_TOKEN")
vinted = Vinted()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'✅ Connecté en tant que {self.user} (ID: {self.user.id})')
        print('------')

    async def on_message(self, message):
        channel = message.channel
        # pas de reponse a soit meme 
        if message.author.id == self.user.id:
            return

        if message.content.startswith('!hello'):
            await channel.send('Hello!')
            
        if message.content.startswith('!manuel'):
            embed = discord.Embed(
                title="📖 Manuel d'utilisation du bot",
                description="Voici la liste des commandes disponibles :",
                color=discord.Color.green()
            )

            embed.add_field(name="👋 `!hello`", value="Le bot vous répond avec un simple 'Hello!'.", inline=False)
            embed.add_field(name="🔍 `!search <lien_vinted>`", value="Effectue une recherche sur Vinted avec le lien fourni et affiche les 5 premiers articles trouvés.", inline=False)
            embed.add_field(name="ℹ️ Exemple :", value="`!search https://www.vinted.fr/vetement?order=newest_first&price_to=60&currency=EUR`", inline=False)
            embed.add_field(name="☁️ Hébergement", value="Le bot est hébergé sur **AWS** pour une disponibilité 24/7.", inline=False)
            embed.add_field(name="🔗 Contribuer", value="[Code source sur GitHub](https://github.com/Rafraf-bot2/vinted-scraperz)", inline=False)
            embed.set_footer(text="Développé par rafraf 🚀")

            await channel.send(embed=embed)
            
        if message.content.startswith('!search'):
            parts = message.content.split(" ", 1)
            if len(parts) < 2:
                await channel.send('❌ Merci de fournir un lien après `!search`.')
                return
            url = parts[1].strip()
            
            try:
                items = vinted.items.search(url, 10, 1)
                
                if not items:
                    await channel.send('⚠️ Aucun article trouvé sur Vinted avec ce lien.')
                    return
                for item in items[:5]:
                    embed = discord.Embed(title=item.title, url=item.url, color=discord.Color.blue())
                    embed.set_thumbnail(url=item.photo)
                    embed.add_field(name="💰 Prix", value=f"{item.price} {item.currency}", inline=True)
                    embed.add_field(name="🏷️ Marque", value=item.brand_title or "N/A", inline=True)
                    
                    await channel.send(embed=embed)
            except Exception as e:
                await channel.send(f'❌ Une erreur est survenue: {e}')


intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

client.run(TOKEN)