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

module=''
status=''

async def info_data():
    modules_info = {
        "welcome": {
            "title": "WELCOME",
            "description": "Sends a welcome message to the welcome channel",
           "field":{
                "Thins": 'you can do lots of things',
                "More":'you can do whatever you want',
                "Message":'message'
            }
        },
        "logging": {
            "title": "LOGGING",
            "description": "Sends a welcome message to the welcome channel",
           "field":{
                "Thins": 'you can do lots of things',
                "More":'you can do whatever you want',
                "Message":'message'
            }
        },
        "guess": {
            "title": "GUESS NUMBER",
            "description": "Sends a welcome message to the welcome channel",
           "field":{
                "Thins": 'you can do lots of things',
                "More":'you can do whatever you want',
                "Message":'message'
            }
        },
        "count": {
            "title": "COUNT",
            "description": "Sends a welcome message to the welcome channel",
           "field":{
                "Thins": 'you can do lots of things',
                "More":'you can do whatever you want',
                "Message":'message'
            }
        },       
    } 
    return modules_info   

async def data(interaction, update=None):
    moduller= await interaction.client.server_config.find_document(interaction.guild.id, 'modules')
    fields= moduller[module]
    global status
    try:
        channel= await interaction.client.server_config.find_field_value(interaction.guild.id,'modules', module,'channel')
    except KeyError:
        pass
    try:  
        hint= await interaction.client.server_config.find_field_value(interaction.guild.id,'modules', module,'hint')
    except KeyError:
        hint='hint'
    try:
        message= await interaction.client.server_config.find_field_value(interaction.guild.id,'modules', module,'message')
    except KeyError:
        message='message'          

    stat=''
    if status is True:
        stat= f'{e.true_png_top}\n{e.true_png_buttom}'
    elif status is False:
        stat=f'{e.false_png_top}\n{e.false_png_buttom}'

    if update == 'enable':
        stat= f'{e.true_gif_top}\n{e.true_gif_buttom}'
    elif update == 'disable':
        stat= f'{e.false_gif_top}\n{e.false_gif_buttom}'

    modules_list = {
        "welcome": {
            "title": "WELCOME",
            "description": "Sends a welcome message to the welcome channel",
           "field":{
                "Status": stat,
                "Channel":f'<#{channel}>',
                "Message":message
            }
        },
        "Logging": {
            "title": "LOGGING",
            "description": "Logs everything happening in the server.",
            "field":fields
        },
        "guess": {
            "title": "GUESS NUMBER",
            "description": "Members try to guess the random generated number",
            "field":{
                "Status": stat,
                "Channel": f'<#{channel}>',
                "Hint":hint,
                "Give Role":f'{e.true_png_top}\n{e.true_png_buttom}',
                "Roles":"None"
            }
        },
        "Count Number": {
            "title": "LOGGING",
            "description": "Logs everything happening in the server.",
            "field":{
                "Status": "ON",
                "Channel":"<#1053109369761452032>",
                "Current Number":"0",
                "Give Role":f'{e.true_png_top}\n{e.true_png_buttom}',
                "Role": ""
            }
        }           
    }
    return modules_list

async def create_info(interaction, update=None):
    modules= await data(interaction, update)
    modules=modules[module]
    embed=discord.Embed(
        title= modules['title'],
        description=modules['description'],
        color= 0x303434)
    for key, value in modules['field'].items():
        embed.add_field(name=key, value=value)
    embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)
    return embed

async def modules_info(interaction):
    modules= await info_data()
    modules=modules[module]
    embed=discord.Embed(
        title= modules['title'],
        description=modules['description'],
        color= 0x303434)
    for key, value in modules['field'].items():
        embed.add_field(name=key, value=value)
    embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)
    return embed

def SecondEmbed(self, interaction):
    embed=discord.Embed(title=f'Modules for {interaction.guild.name} ', description='You can enabled or disable modules for your server.')
    embed.add_field(name='GENERAL MODULES', value= f'Welcome\nLogging', inline=True)
    embed.add_field(name='SECURITY MODULES', value='Invite Deletion\nFlagged Links', inline=True)
    embed.add_field(name='FUN MODULES', value='Guess Number\nCount Number', inline=True)  
    return embed  

class Channel(discord.ui.Modal, title='Set Channel'):
    channel = ui.TextInput(label='Channel ID', style=discord.TextStyle.short, placeholder='Please provide a channel id')

    async def on_submit(self, interaction:discord.Interaction):
        await interaction.client.server_config.update_field_value(interaction.guild.id,'modules', module, 'channel', str(self.channel))
        embed= await create_info(interaction)
        await interaction.response.edit_message(embed=embed, view=ModuleView())

class Message(discord.ui.Modal, title='Set Message'):
    message = ui.TextInput(label='Message', style=discord.TextStyle.short, placeholder='Please provide a message')

    async def on_submit(self, interaction:discord.Interaction):
        await interaction.client.server_config.update_field_value(interaction.guild.id,'modules', module, 'message', str(self.message))
        embed= await create_info(interaction)
        await interaction.response.edit_message(embed=embed, view=ModuleView())

class Hint(discord.ui.Modal):
    def __init__(self, view:discord.ui.View):
        self.view = view
        self.button=''
        super().__init__(title=f'Set Hint')
    hint = ui.TextInput(label='Hint', style=discord.TextStyle.short, placeholder='Please provide a hint count')

    async def on_submit(self, interaction:discord.Interaction):
        await interaction.client.server_config.update_field_value(interaction.guild.id,'modules', module, 'hint', str(self.hint))
        view=ModuleView()
        mdlview=ModuleView()
        self.button=ui.Button(label='Set Hint', style=discord.ButtonStyle.green)
        view.add_item(self.button)   
        self.button.callback= mdlview.hint_callback
        embed= await create_info(interaction)
        await interaction.response.edit_message(embed=embed, view=view)


class Setup(discord.ui.Modal):
    def __init__(self, view:discord.ui.View, view2:discord.ui.View):
        self.view = view
        self.view2= view2
        super().__init__(title=f'Setup')

    channel = ui.TextInput(label='Channel ID', style=discord.TextStyle.short, placeholder='Please provide a channel id')
    
    async def on_submit(self, interaction:discord.Interaction):
        global status
        data ={'status':True,'channel':str(self.channel)}
        view=ModuleView()
        if module=='welcome':
            data.update({'message': str(self.view.hint)})          
        elif module=='guess':
            view=ModuleView()
            mdlview=ModuleView()
            self.button=ui.Button(label='Set Hint', style=discord.ButtonStyle.green)
            view.add_item(self.button)   
            self.button.callback= mdlview.hint_callback            
            data.update({'hint': str(self.view.hint)})       

        user_file= {f'modules.{module}':data}
        await interaction.client.server_config.update_dc(interaction.guild.id, user_file)
        status= True
        embed= await create_info(interaction)
        await interaction.response.edit_message(embed=embed, view=view)
        

class NodbView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.hint= '' 

    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:main:1057073241753124864>')
    async def back_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(embed=SecondEmbed(self,interaction), view=NewModuleView())

    @discord.ui.button(label='Setup', style=discord.ButtonStyle.primary)
    async def setup_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        view2=ModuleView()
        modal=Setup(self, view2)
        
        if module == 'welcome':
            self.hint= ui.TextInput(label='Message', style=discord.TextStyle.short, placeholder='Please provide a message')
        elif module == 'guess':
            self.hint= ui.TextInput(label='Hint', style=discord.TextStyle.short, placeholder='Please provide a hint count')
        modal.add_item(self.hint) 
        await interaction.response.send_modal(modal)


class ModuleView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.view=NewModuleView()
        self.button=self.view.button


    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:main:1057073241753124864>')
    async def back_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(embed=SecondEmbed(self,interaction), view=NewModuleView())


    @discord.ui.button(label='Disable', style=discord.ButtonStyle.red)
    async def on_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        embed=''
        if button.label=='Enable':
            button.label='Disable'
            button.style= discord.ButtonStyle.red
            self.channel_button.disabled=False
            self.message_button.disabled=False
            await interaction.client.server_config.update_field_value(interaction.guild.id,'modules', module, 'status', True)    
            embed= await create_info(interaction, 'enable')
            await interaction.response.edit_message(embed=embed,view=self)
        elif button.label=='Disable':
            button.label='Enable'
            button.style= discord.ButtonStyle.green
            self.channel_button.disabled=True
            self.message_button.disabled=True
            await interaction.client.server_config.update_field_value(interaction.guild.id,'modules', module, 'status', False)    
            embed= await create_info(interaction, 'disable')                  
            await interaction.response.edit_message(embed=embed,view=self)

    @discord.ui.button(label='Set Channel', style=discord.ButtonStyle.green,)
    async def channel_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        view=ModuleView()
        await interaction.response.send_modal(Channel())

    @discord.ui.button(label='Set Message', style=discord.ButtonStyle.green,)
    async def message_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.send_modal(Message())

    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:info:1057118591733989457>', row=1)
    async def info_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.defer()
        await interaction.followup.send(embed= await modules_info(interaction), ephemeral=True)

    async def hint_callback(self, interaction:discord.Interaction):
        await interaction.response.send_modal(Hint(self))
      



class NewModuleView(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.category=None
        self.button=None

    def MainEmbed(self, interaction):
        embed=discord.Embed(
            title="",
            description='Commands in this server start with `?`',
            color= 0x303434)
        embed.add_field(name="・Help Panel", value="Welcome to Husky Bot's help panel! We have made a small overview to help you! \
            Make a choice via the menu below.", inline=False)    
        embed.add_field(name="・Links", value="[Invite](https://discord.com/api/oauth2/authorize?client_id=1049143343084490862&permissions=8&scope=bot) : [Support Server](https://discord.gg/a2R2KbFVWT) : [Status](https://huskybot1.statuspage.io/)", inline=False)   
        embed.set_author(name=interaction.guild.name, icon_url=interaction.guild.icon)        
        return embed

    @discord.ui.select(placeholder="Select a module first",max_values=1,min_values=1, options=[
            discord.SelectOption(label="Welcome",value= "welcome",emoji="⚒️",description="Sends a welcome message to the welcome channel"),
            discord.SelectOption(label="Logging",value= "logging",emoji="⚙️",description="Logs everythin happening in the server."),
            discord.SelectOption(label="Invite Deletion",emoji="⚙️",description="Logs everythin happening in the server."),
            discord.SelectOption(label="Flagged Links",emoji="⚙️",description="Logs everythin happening in the server."),
            discord.SelectOption(label="Guess Number",value= "guess",emoji="💯",description="Logs everythin happening in the server."),
            discord.SelectOption(label="Count Number",value= "count",emoji="⚙️",description="Logs everythin happening in the server."),                  
            ])     
    async def select_callback(self, interaction: discord.Interaction, select:discord.ui.Select):
        global module
        global status
        module=select.values[0]
        try:
            status= await interaction.client.server_config.find_field_value(interaction.guild.id,'modules', module,'status')
            view=ModuleView()
            if status is False:    
                view.on_button.label='Enable'
                view.on_button.style=discord.ButtonStyle.green
                view.channel_button.disabled=True
                view.message_button.disabled=True
            if select.values[0] =='guess':
                mdlview=ModuleView()
                self.button=ui.Button(label='Set Hint', style=discord.ButtonStyle.green)
                view.add_item(self.button)   
                self.button.callback= mdlview.hint_callback
            embed= await create_info(interaction)  
        except KeyError:
            status= False
            view=NodbView()  
            embed= await modules_info(interaction) 
        await interaction.response.edit_message(embed=embed, view=view)


    @discord.ui.button(label='', style=discord.ButtonStyle.primary, emoji='<:main:1057073241753124864>')
    async def back_button(self, interaction:discord.Interaction, button:discord.ui.Button):
        await interaction.response.edit_message(embed=self.MainEmbed(interaction), view=MainView())

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
                    a=await interaction.client.server_config.find_field_value(interaction.guild_id,'modules', 'welcome', 'status')  
                    if a is True:
                        wstatus= f'ㅤ{e.true_png_top}\nㅤ{e.true_png_buttom}'
                except:
                    pass 
                                                                   
                await interaction.response.edit_message(embed=SecondEmbed(self, interaction), view=NewModuleView())
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