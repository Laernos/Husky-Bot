import discord
from discord.ext import commands
from discord import app_commands


class Select(discord.ui.Select):
    def __init__(self):
        options=[
            discord.SelectOption(label="Option 1",emoji="👌",description="This is option 1!"),
            discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
            ]
        super().__init__(placeholder="Select an option",max_values=1,min_values=1,options=options)
    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content=f"Your choice is {self.values[0]}!",ephemeral=True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())


class Annen(discord.ui.View):
    @discord.ui.select(options=[
            discord.SelectOption(label="asd",emoji="👌",description="This is option 1!"),
            discord.SelectOption(label="Option 2",emoji="✨",description="This is option 2!"),
            discord.SelectOption(label="Option 3",emoji="🎭",description="This is option 3!")
            ])
    

    async def select_callback(self, interaction:discord.interactions, select:discord.ui.Select):
        if select.values[0] == 'asd':
            await interaction.response.send_message('anneni gotten')
        elif select.values[0] == 'Option 2':
            await interaction.response.send_message('basdasd') 
        elif select.values[0] == 'Option 3':
            await interaction.response.send_message('anneni gotten')               

    @discord.ui.button(label='Disable', style=discord.ButtonStyle.green)
    async def disable_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_message(f'yarrak')






class Selection(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def menu(self,ctx):
        await ctx.send("Menus!",view=Annen( )) 

        





    

async def setup(bot):
    await bot.add_cog(Selection(bot))