import discord
from discord.ext import commands
from discord import app_commands, File
from easy_pil import Editor, load_image_async, Font

games_list = {
    "unrailed": {
        "title": "Unrailed",
        "url": "https://cdn.cloudflare.steamstatic.com/steam/apps/1016920/header.jpg?t=1667079473"
    },
    "valorant": {
        "title": "Valorant",
        "url": None
    },
    "csgo": {
        "title": "Counter-Strike: Global Offensive",
        "url": "https://cdn.cloudflare.steamstatic.com/steam/apps/730/header.jpg?t=1668125812"
    },
    "other": {
        "title": "a game",
        "url": None
    }
}

class ReadyOrNotView(discord.ui.View):

    joined_users = []
    declined_users = []
    tentative_users = []

    initiatior: discord.User=None
    players: int = 0

    async def send(self,interaction: discord.Interaction):
        self.joined_users.append(interaction.user.display_name)
        embed=self.create_embed()
        await interaction.response.send_message(view=self, embed=embed)
        self.message= await interaction.original_response()

    async def cancel(self):
        game_image= await load_image_async(str(self.game['url']))
        cancel_image = await load_image_async(str('https://imgur.com/saXKIHY.png'))
        game= Editor(game_image).resize((460,215))
        cancel = Editor(cancel_image).resize((230,230))
        game.paste(cancel, (90,0))
        file= File(fp=game.image_bytes, filename='pic1.png')        
        return file

    def convert_user_list_to_str(self, user_list, default_str='No one'):
        if len(user_list):
            return '\n'.join(user_list)
        return default_str
        
    def disable_all_buttons(self):
        self.join_button.disabled= True
        self.decline_button.disabled = True
        self.tentative_button.disabled = True

    def check_players_full(self):
        if len(self.joined_users) >= self.players:
            return True
        return False        

    async def update_message(self):
        if self.check_players_full():
            self.disable_all_buttons()
            
        embed=self.create_embed()
        await self.message.edit(view=self, embed=embed)

    def create_embed(self):
        desc = f"{self.initiatior.mention} is looking for another {self.players - 1} players to play {self.game['title']}"
        embed = discord.Embed(title="Lets get together", description=desc)

        if self.game['url']:
            embed.set_image(url=self.game['url'])
        
        embed.add_field(inline=True, name='✅Joined', value=self.convert_user_list_to_str(self.joined_users))
        embed.add_field(inline=True, name='❤️Declined', value=self.convert_user_list_to_str(self.declined_users))
        embed.add_field(inline=True, name='🛡️Tentative', value=self.convert_user_list_to_str(self.tentative_users))
        return embed

    @discord.ui.button(label='Join', style=discord.ButtonStyle.green)
    async def join_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()

        if interaction.user.display_name not in self.joined_users:
            self.joined_users.append(interaction.user.display_name)
        if interaction.user.display_name in self.declined_users:
            self.declined_users.remove(interaction.user.display_name)
        if interaction.user.display_name in self.tentative_users:
            self.tentative_users.remove(interaction.user.display_name)            
        await self.update_message()

    @discord.ui.button(label='Decline', style=discord.ButtonStyle.green)
    async def decline_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()

        if interaction.user.display_name in self.joined_users:
            self.joined_users.remove(interaction.user.display_name)
        if interaction.user.display_name not in self.declined_users:
            self.declined_users.append(interaction.user.display_name)
        if interaction.user.display_name in self.tentative_users:
            self.tentative_users.remove(interaction.user.display_name)            
        await self.update_message()

    @discord.ui.button(label='Maybe', style=discord.ButtonStyle.green)
    async def tentative_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()

        if interaction.user.display_name in self.joined_users:
            self.joined_users.remove(interaction.user.display_name)
        if interaction.user.display_name in self.declined_users:
            self.declined_users.remove(interaction.user.display_name)
        if interaction.user.display_name not in self.tentative_users:
            self.tentative_users.append(interaction.user.display_name)            
        await self.update_message()

    @discord.ui.button(label='Cancel', style=discord.ButtonStyle.red)
    async def cancel_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()

        if interaction.user.display_name in self.joined_users:
            self.joined_users.remove(interaction.user.display_name)
        if interaction.user.display_name in self.declined_users:
            self.declined_users.remove(interaction.user.display_name)
        if interaction.user.display_name not in self.tentative_users:
            self.tentative_users.append(interaction.user.display_name) 
        file=await self.cancel()
        embed=self.create_embed()
        embed.set_image(url='attachment://pic1.png')
        await interaction.message.edit(view=None, embed=embed, attachments=[file])


class Play(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name= 'play', description='Shows member count')
    @app_commands.choices(game=[
        app_commands.Choice(name="Unrailed", value="unrailed"),
        app_commands.Choice(name="Valorant", value="valorant"),
        app_commands.Choice(name="CS:GO", value="csgo"),
        app_commands.Choice(name="Other", value="other"),
    ])    
    async def play(self, interaction: discord.Interaction, game:app_commands.Choice[str], players: int):
        view=ReadyOrNotView(timeout=60)
        view.initiatior= interaction.user
        view.game = games_list[game.value]
        view.players= players
        await view.send(interaction)


    

async def setup(bot):
    await bot.add_cog(Play(bot))