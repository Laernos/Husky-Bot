import discord
from discord.ext import commands
from discord import app_commands, ui
from datetime import datetime
import platform
import psutil
from dateutil.relativedelta import relativedelta
import emotes as e
import asyncio




class Bug(discord.ui.Modal, title='Bug Report'):
    
    description = ui.TextInput(label='Description', style=discord.TextStyle.paragraph, placeholder='A brief description of the bug.')
    reproduce = ui.TextInput(label='Steps to Reproduce', style=discord.TextStyle.paragraph, placeholder='Please list each action necessary to make the bug happen.')
    result = ui.TextInput(label='Expected Result', style=discord.TextStyle.paragraph, placeholder='What should happen if the bug wasn\'t there?')
    ac_result = ui.TextInput(label='Actual Result', style=discord.TextStyle.paragraph, placeholder='What actually happens if you follow the steps.')
    add_info=ui.TextInput(label='Additional Info (optional) ', style=discord.TextStyle.paragraph, placeholder='More info or screenshot urls (https://imgur.com/6IS1jmH.png)', required=False)

    async def on_submit(self, interaction:discord.Interaction):
        channel= interaction.client.get_channel(1055696376404639916)
        dm= await interaction.user.create_dm()
        embed1=discord.Embed(title='Bug Report Submission', description='')
        embed1.add_field(name='USER', value=f'{interaction.user.name}#{interaction.user.discriminator}\n`{interaction.user.id}`')
        embed1.add_field(name='GUILD', value=f'{interaction.guild.name}\n`{interaction.guild_id}`')
        embed1.add_field(name='MEMBER #', value= len(interaction.guild.members))
        embed2=discord.Embed(title='Description', description=self.description,)
        embed3=discord.Embed(title='Steps to Reproduce', description=self.reproduce)
        embed4=discord.Embed(title='Expected Result', description=self.result)
        embed5=discord.Embed(title='Actual Result', description=self.ac_result)
        embed6=discord.Embed(title='Additional Info', description=self.add_info,timestamp= datetime.now())
        embeds=[embed1,embed2,embed3,embed4,embed5,embed6]
        await channel.send(f'New Bug Reported! <@344034871230070784>')
        try:
            await dm.send(f'Here is a copy of your submission')
            await interaction.response.send_message(f'Thank you for your submission! A copy of your subbmission has been sent to your dms', ephemeral=True)
        except:
            await interaction.response.send_message(f'Thank you for your submission! Copy couldn\'t send because your dm\'s are closed.', ephemeral=True)    
        #To DO: Bot doesnt send copy if user dms are closed
        for embed in embeds:
            try:
                await dm.send(embed=embed)
            except:
                pass
            await channel.send(embed=embed)


class ModuleView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.module=None  

    def create_InfoEmbed(self, interaction:discord.Interaction):
        embed=discord.Embed(
            title='Welcome Module',
            description='Commands in this server start with `?`',
            color= 0x303434)
        embed.add_field(name="・Help Panel", value="Welcome to Husky Bot's help panel! We have made a small overview to help you! \
            Make a choice via the menu below.", inline=False)    
        embed.add_field(name="・Links", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1049143343084490862&permissions=8&scope=bot) : [Support Server](https://discord.gg/a2R2KbFVWT) : [Status](https://huskybot1.statuspage.io/)", inline=False)   
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)
        return embed


    def create_embed(self, interaction:discord.Interaction):
        embed=discord.Embed(
            title="",
            description='Commands in this server start with `?`',
            color= 0x303434)
        embed.add_field(name="・Help Panel", value="Welcome to Husky Bot's help panel! We have made a small overview to help you! \
            Make a choice via the menu below.", inline=False)    
        embed.add_field(name="・Links", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1049143343084490862&permissions=8&scope=bot) : [Support Server](https://discord.gg/a2R2KbFVWT) : [Status](https://huskybot1.statuspage.io/)", inline=False)   
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)
        return embed

    async def create_ModuleEmbed(self, interaction:discord.Interaction, wstatus:None):
        if wstatus is None:
            wstatus= f'ㅤ{e.false_png_top}\nㅤ{e.false_png_buttom}'
        try:
            a=await interaction.client.server_config.find_field_value(interaction.guild_id,'commands', 'welcome_cmnd', 'status')  
            if a is True:
                wstatus= f'ㅤ{e.true_png_top}\nㅤ{e.true_png_buttom}'
        except:
            pass  
        embed=discord.Embed(title=f'Module Configs for {interaction.guild.name} ', description='You can enabled or disable modules for your server.')
        embed.add_field(name='WELCOME', value= f'```Sends a welcome message to\nthe welcome channel```', inline=True)
        embed.add_field(name='ㅤ', value=wstatus, inline=True)            
        embed.add_field(name='ㅤ', value='ㅤ', inline=True)
        embed.add_field(name='LOGGING', value= f'```Logs everythin happening in the server.```', inline=True)
        embed.add_field(name='ㅤ', value=wstatus, inline=True)                   
        embed.add_field(name='ㅤ', value='ㅤ', inline=True)   
        return embed 

    @discord.ui.select(placeholder="Select a module first",max_values=1,min_values=1,options=[
            discord.SelectOption(label="Welcome",emoji="⚒️",description="Sends a welcome message to the welcome channel"),
            discord.SelectOption(label="Logging",emoji="⚙️",description="Logs everythin happening in the server.")
            ])         
    async def select_callback(self, interaction: discord.Interaction, select:discord.ui.Select):
        
        try:
            a=await interaction.client.server_config.find_field_value(interaction.guild_id,'commands', 'welcome_cmnd', 'status')  
            if a is True:
                self.enable_button.disabled= True
                self.disable_button.disabled= False
            else:
                self.disable_button.disabled= False
                self.enable_button.disabled= True
        except:
            self.disable_button.disabled= False
            self.enable_button.disabled= True         
        
        
        #buttons= [x for x in self.children]
        #for button in buttons:
        #    button.disabled=False

        if select.values[0] == 'Welcome':
            self.module= 'welcome'
        
        elif select.values[0] == 'Logging':
            self.module= 'logging'     

        await interaction.response.edit_message(view=self)


    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:main:1057073241753124864>')
    async def main_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed= self.create_embed(interaction)
        await interaction.response.edit_message(embed=embed, view=MainView())

    @discord.ui.button(label='Enable', style=discord.ButtonStyle.green, disabled=True)
    async def enable_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.module =='welcome':
            wstatus= f'ㅤ{e.true_gif_top}\nㅤ{e.true_gif_buttom}'
            embed= await self.create_ModuleEmbed(interaction, wstatus)
            self.enable_button.disabled= True             
            self.disable_button.disabled= False             
            await interaction.response.edit_message(embed=embed, view=self)
            await interaction.client.server_config.update_field_value(interaction.guild.id, 'commands','welcome_cmnd', 'status', True)


    @discord.ui.button(label='Disable', style=discord.ButtonStyle.red, disabled=True)
    async def disable_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        if self.module =='welcome':
            await interaction.client.server_config.update_field_value(interaction.guild.id, 'commands','welcome_cmnd', 'status', False)
            wstatus= f'ㅤ{e.false_gif_top}\nㅤ{e.false_gif_buttom}'
            embed= await self.create_ModuleEmbed(interaction, wstatus)
            self.disable_button.disabled= True
            self.enable_button.disabled= False
            await interaction.response.edit_message(embed=embed, view=self)   


    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:info:1057118591733989457>')
    async def info_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed= self.create_embed(interaction)
        await interaction.response.edit_message(embed=embed, view=MainView())



class MainView(discord.ui.View):
    def __init__(self):
        super().__init__()   
        self.add_item(discord.ui.Button(label="Support",style=discord.ButtonStyle.link,url="https://discord.gg/a2R2KbFVWT", emoji='<:support:1057062148007792730>'))
    
    @discord.ui.select(placeholder="Select an option",max_values=1,min_values=1,options=[
            discord.SelectOption(label="Commands",emoji="⚒️",description="Show the bot commands",),
            discord.SelectOption(label="Server Config",emoji="⚙️",description="Show the server configs"),
            discord.SelectOption(label="Bot Stats",emoji="📊",description="Show the bot statistics"),
            discord.SelectOption(label="Changelog",emoji="📃",description="Show the bot changelogs"),
            discord.SelectOption(label="Report Bug",emoji="🪲",description="Reports bugs"),
            ])


    async def select_callback(self, interaction: discord.Interaction, select:discord.ui.Select):
        if select.values[0] == 'Report Bug':
            await interaction.response.send_modal(Bug())
        elif select.values[0] == 'Commands':
            embed=discord.Embed(title='・Help Panel', description='View all command categories in the bot here!')
            embed.add_field(name='General Commands', value='`avatar`\n`echo`\n`huskies`\n`stats`')
            embed.add_field(name='Moderation Commands', value='`ban`\n`unban`\n`kick`\n`lock`')
            embed.add_field(name='Server Config Commands', value='`prefix`\n`welcome`\n`logging`')
            embed.add_field(name='Owner Commands', value='`reload`\n`resetdb`')            
            await interaction.response.edit_message(embed=embed, view=None)


        elif select.values[0] == 'Bot Stats':
            delta_uptime = relativedelta(datetime.utcnow(), interaction.client.launch_time)
            days, hours, minutes, seconds = delta_uptime.days, delta_uptime.hours, delta_uptime.minutes, delta_uptime.seconds

            uptimes = {x[0]: x[1] for x in [('days', days), ('hours', hours),
                                            ('minutes', minutes), ('seconds', seconds)] if x[1]}

            last = "".join(value for index, value in enumerate(uptimes.keys()) if index == len(uptimes)-1)
            uptime_string = "".join(
                f"{v} {k}" if k != last else f" and {v} {k}" if len(uptimes) != 1 else f"{v} {k}"
                for k, v in uptimes.items()
            )            
            python_version= platform.python_version()
            dpy_version= discord.__version__
            server_count= len(interaction.client.guilds)
            member_count= len(interaction.guild.members)
            embed=discord.Embed(title= f'{interaction.client.user.name} Bot Statistics', description="<a:ttopleft:1056637361993306192><a:ttopright:1056637363004125274>\n<a:tbuttomleft:1056637360273625168><a:tbuttomright:1056637361259294730>", color=interaction.user.colour, timestamp=interaction.message.created_at)
            embed.add_field(name='Python V.', value= f'```{python_version}```')
            embed.add_field(name='Discord.py V.', value= f'```{dpy_version}```')
            embed.add_field(name='CPU Usage', value=f'```{psutil.cpu_percent()}%```')
            embed.add_field(name='Memory Usage', value=f'```{psutil.virtual_memory().percent}%```')
            embed.add_field(name='Up Time', value=f'{uptime_string}')
            embed.add_field(name='Total Guilds', value=server_count)
            embed.add_field(name='Unique Users', value= member_count)
            embed.set_footer(text=f"Husky | {interaction.client.user.name}")
            embed.set_author(name=interaction.client.user.name, icon_url=interaction.client.user.avatar.url)
            await interaction.response.edit_message(embed=embed, view=None)

        elif select.values[0] == 'Server Config':
            if interaction.user.guild_permissions.administrator or interaction.user.guild_permissions.manage_guild: 
                wstatus= f'ㅤ{e.false_png_top}\nㅤ{e.false_png_buttom}'
                lstatus= f'ㅤ{e.false_png_top}\nㅤ{e.false_png_buttom}'
                try:
                    a=await interaction.client.server_config.find_field_value(interaction.guild_id,'commands', 'welcome_cmnd', 'status')  
                    if a is True:
                        wstatus= f'ㅤ{e.true_png_top}\nㅤ{e.true_png_buttom}'
                except:
                    pass  
                embed=discord.Embed(title=f'Module Configs for {interaction.guild.name} ', description='You can enabled or disable modules for your server.')
                embed.add_field(name='WELCOME', value= f'```Sends a welcome message to\nthe welcome channel```', inline=True)
                embed.add_field(name='ㅤ', value=wstatus, inline=True)            
                embed.add_field(name='ㅤ', value='ㅤ', inline=True)
                embed.add_field(name='LOGGING', value= f'```Logs everythin happening in the server.```', inline=True)
                embed.add_field(name='ㅤ', value=wstatus, inline=True)                   
                embed.add_field(name='ㅤ', value='ㅤ', inline=True)            
                await interaction.response.edit_message(embed=embed, view=ModuleView())
            else:
                await interaction.response.defer()
                await interaction.followup.send('You dont have the permissions to do that!', ephemeral=True)

        else:      
            await interaction.response.send_message(content=f"Your choice is {select.values[0]}!",ephemeral=True)








class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.bot.launch_time = datetime.utcnow()

    @app_commands.command(name= 'help', description='Shows the help embed')
    async def help(self, interaction: discord.Interaction):
        embed=discord.Embed(
            title="",
            description='Commands in this server start with `?`',
            color= 0x303434)
        embed.add_field(name="・Help Panel", value="Welcome to Husky Bot's help panel! We have made a small overview to help you! \
            Make a choice via the menu below.", inline=False)    
        embed.add_field(name="・Links", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1049143343084490862&permissions=8&scope=bot) : [Support Server](https://discord.gg/a2R2KbFVWT) : [Status](https://huskybot1.statuspage.io/)", inline=False)   
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)
        await interaction.response.send_message(embed=embed, view=MainView(), ephemeral=True)




async def setup(bot):
    await bot.add_cog(Help(bot))