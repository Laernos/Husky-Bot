import discord
from discord.ext import commands
from discord import app_commands
from datetime import datetime
#I'm not proud of myself with this code but it works u know.

class Testa(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    async def set_true(self,ctx:commands.context,log):
        await self.bot.server_config.update_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd',log, 'status',True)

    async def set_false(self,ctx:commands.context,log):
        await self.bot.server_config.update_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd',log, 'status',False)

    async def set_channel(self,ctx:commands.context,log, channel):
        await self.bot.server_config.update_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd',log, 'channel',channel)

    async def check_true(self,ctx:commands.context,log,):
        a=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd',log, 'status')
        return a


    @commands.hybrid_command(name='alper', description= 'enables or disables the logging modules')
    @commands.has_permissions(administrator = True)
    @app_commands.describe(status="statu iste aq ne bilm")
    @app_commands.choices(status=[
        discord.app_commands.Choice(name='Enable', value='enable'),
        discord.app_commands.Choice(name='Disable', value='disable'),
        discord.app_commands.Choice(name='Set Channel', value='channel')        
    ], module=[
        discord.app_commands.Choice(name='All', value='all'),
        discord.app_commands.Choice(name='Server Logging', value='server'),
        discord.app_commands.Choice(name='Member Logging', value='member'),
        discord.app_commands.Choice(name='Moderation Logging', value='moderation'),
        discord.app_commands.Choice(name='Message Logging', value='message'),
        discord.app_commands.Choice(name='Voice Logging', value='voice'),
        discord.app_commands.Choice(name='Invite Logging', value='invite'),
        discord.app_commands.Choice(name='Activity Logging', value='activity')    
    ])
    @commands.cooldown(1,5)
    async def alper(self, ctx:commands.context, status:discord.app_commands.Choice[str], module:discord.app_commands.Choice[str], channel: discord.abc.GuildChannel =None):
        if status.value == 'enable':
            try:
                await self.bot.server_config.find_field(ctx.guild.id, 'commands', 'logging_cmnd')
            except KeyError:
                data ={
                'server':{'status':"",'channel':""},
                'member':{'status':"",'channel':""},
                'moderation':{'status':"",'channel':""},
                'message':{'status':"",'channel': ""},
                'voice':{'status':"",'channel':""},
                'invite':{'status':"",'channel':""},
                'activity':{'status':"",'channel':""}                    
                }
                user_file= {f'commands.logging_cmnd':data}
                await self.bot.server_config.update_dc(ctx.guild.id, user_file)              
            if module.value == 'all':
                a=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                if channel is None:
                    if a!='': server_channel= self.bot.get_channel(int(a))
                    else: server_channel=ctx.message.channel
                else: server_channel= channel
                b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'member', 'channel')
                if channel is None:
                    if b!='': member_channel= self.bot.get_channel(int(b))
                    else: member_channel=ctx.message.channel
                else: member_channel= channel
                c=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'moderation', 'channel')
                if channel is None:
                    if c!='': moderation_channel= self.bot.get_channel(int(c))
                    else: moderation_channel=ctx.message.channel
                else: moderation_channel= channel
                d=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                if channel is None:
                    if d!='': message_channel= self.bot.get_channel(int(d))
                    else: message_channel=ctx.message.channel
                else: message_channel= channel
                e=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'voice', 'channel')
                if channel is None:
                    if e!='': voice_channel= self.bot.get_channel(int(e))
                    else: voice_channel=ctx.message.channel
                else: voice_channel= channel
                f=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'invite', 'channel')
                if channel is None:
                    if f!='': invite_channel= self.bot.get_channel(int(f))
                    else: invite_channel=ctx.message.channel
                else: invite_channel= channel
                g=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'activity', 'channel')
                if channel is None:
                    if g!='': activity_channel= self.bot.get_channel(int(g))
                    else: activity_channel=ctx.message.channel
                else: activity_channel= channel                                
                                                                                                
                await self.set_true(ctx,'server')
                await self.set_true(ctx,'member')
                await self.set_true(ctx,'moderation')
                await self.set_true(ctx,'message')
                await self.set_true(ctx,'voice')
                await self.set_true(ctx,'invite')
                await self.set_true(ctx,'activity')
                await self.set_channel(ctx,'server', server_channel.id)
                await self.set_channel(ctx,'member', member_channel.id)
                await self.set_channel(ctx,'moderation', moderation_channel.id)
                await self.set_channel(ctx,'message', message_channel.id)
                await self.set_channel(ctx,'voice', voice_channel.id)
                await self.set_channel(ctx,'invite', invite_channel.id)
                await self.set_channel(ctx,'activity', activity_channel.id)                    
                await ctx.send(f'all modules are enabled\n**Channels:\nServer Logging:**{server_channel.mention}\n**Member Logging:** {member_channel.mention}\n**Moderation Logging:** {moderation_channel.mention}\n**Message Logging:** {message_channel.mention}\n**Voice Logging:** {voice_channel.mention}\n**Invite Logging:** {invite_channel.mention}\n**Activity Logging:** {activity_channel.mention}\n use`/logging Set Channel` slash command to change channel`')
            elif module.value== 'server':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'server')
                await self.set_channel(ctx,'server', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Server Logging Has been set for this channel')
            elif module.value== 'member':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'member', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'member')
                await self.set_channel(ctx,'member', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Member Logging Has been set for this channel')
            elif module.value== 'moderation':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'moderation', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'moderation')
                await self.set_channel(ctx,'moderation', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Moderation Logging Has been set for this channel')
            elif module.value== 'message':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel      
                await self.set_true(ctx,'message')
                await self.set_channel(ctx,'message', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Message Logging Has been set for this channel')
            elif module.value== 'voice':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'voice', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'voice')
                await self.set_channel(ctx,'voice', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Voice Logging Has been set for this channel')
            elif module.value== 'invite':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'invite', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'invite')
                await self.set_channel(ctx,'invite', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Invite Logging Has been set for this channel')
            elif module.value== 'activity':
                if channel is None:
                    b=await self.bot.server_config.find_field_value_value(ctx.guild.id, 'commands', 'logging_cmnd', 'activity', 'channel')
                    if b != '': channel= self.bot.get_channel(int(b))
                    else: channel=ctx.message.channel                  
                await self.set_true(ctx,'activity')
                await self.set_channel(ctx,'activity', channel.id)
                await ctx.send(f'{module.name} is enabled')
                await channel.send(f'Activity Logging Has been set for this channel')                                                                           
        elif status.value == 'disable':
            try:
                await self.bot.server_config.find_field(ctx.guild.id, 'commands', 'logging_cmnd')
                if module.value == 'all':
                    await self.set_false(ctx,'server')
                    await self.set_false(ctx,'member')
                    await self.set_false(ctx,'moderation')
                    await self.set_false(ctx,'message')
                    await self.set_false(ctx,'voice')
                    await self.set_false(ctx,'invite')
                    await self.set_false(ctx,'activity')
                    await ctx.send('all modules disabled')
                elif module.value== 'server':
                    await self.set_false(ctx,'server')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'member':
                    await self.set_false(ctx,'member')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'moderation':
                    await self.set_false(ctx,'moderation')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'message':
                    await self.set_false(ctx,'message')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'voice':
                    await self.set_false(ctx,'voice')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'invite':
                    await self.set_false(ctx,'invite')
                    await ctx.send(f'{module.name} is disabled')
                elif module.value== 'activity':
                    await self.set_false(ctx,'activity')
                    await ctx.send(f'{module.name} is disabled')                        
            except KeyError:
                await ctx.send(f'Logging is already disabled!')    
        else:
            if channel is not None :
                try:
                    await self.bot.server_config.find_field(ctx.guild.id, 'commands', 'logging_cmnd')
                    if module.value == 'all':
                        a=await self.check_true(ctx,'server')
                        b=await self.check_true(ctx,'member')
                        c=await self.check_true(ctx,'moderation')
                        d=await self.check_true(ctx,'message')
                        e=await self.check_true(ctx,'voice')
                        f=await self.check_true(ctx,'invite')
                        g=await self.check_true(ctx,'activity')
                        if a and b and c and d and e and f and g is True:
                            await self.set_channel(ctx,'server', channel.id)
                            await self.set_channel(ctx,'member', channel.id)
                            await self.set_channel(ctx,'moderation', channel.id)
                            await self.set_channel(ctx,'message', channel.id)
                            await self.set_channel(ctx,'voice', channel.id)
                            await self.set_channel(ctx,'invite', channel.id)
                            await self.set_channel(ctx,'activity', channel.id)                    
                            await ctx.send('channel has been set for all modules')
                        else:
                            await ctx.send('You need to enable the all modules first!')    
                    elif module.value== 'server':
                        d=await self.check_true(ctx,'server')
                        if d is True:
                            await self.set_channel(ctx,'server', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')    
                    elif module.value== 'member':
                        d=await self.check_true(ctx,'member')
                        if d is True:
                            await self.set_channel(ctx,'member', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')  
                    elif module.value== 'moderation':
                        d=await self.check_true(ctx,'moderation')
                        if d is True:
                            await self.set_channel(ctx,'moderation', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')  
                    elif module.value== 'message':
                        d=await self.check_true(ctx,'message')
                        if d is True:
                            await self.set_channel(ctx,'message', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')  
                    elif module.value== 'voice':
                        d=await self.check_true(ctx,'voice')
                        if d is True:
                            await self.set_channel(ctx,'voice', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')  
                    elif module.value== 'invite':
                        d=await self.check_true(ctx,'invite')
                        if d is True:
                            await self.set_channel(ctx,'invite', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')  
                    elif module.value== 'activity':
                        d=await self.check_true(ctx,'activity')
                        if d is True:
                            await self.set_channel(ctx,'activity', channel.id)
                            await ctx.send(f'{channel.name} has been set for {module.name}')
                        else:
                            await ctx.send('You need to enable the module first!')                    
                except KeyError:
                    await ctx.send(f'You need to enable this module first!')             
            else:
                await ctx.send('You need to specify a channel')
#------------------------------------------------------------------------------------------------------
    




    @commands.Cog.listener()
    async def on_message_delete(self,message):
        try:
            if not message.author.bot: 
                await self.bot.server_config.find_field(message.guild.id, 'commands', 'logging_cmnd')
                if await self.bot.server_config.find_field_value_value(message.guild.id, 'commands', 'logging_cmnd', 'message', 'status') is True:
                    b=await self.bot.server_config.find_field_value_value(message.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                    channel=self.bot.get_channel(int(b))
                    embed= discord.Embed(
                        title=f'Message deleted in #{message.channel}',
                        description= message.content,
                        color=discord.Colour.red(),
                        timestamp=datetime.now()
                        )
                    embed.set_author(name=message.author.name, icon_url= message.author.avatar)
                    embed.set_footer(text=f'ID:{message.author.id}')            
                    await channel.send(embed=embed)         
        except KeyError:
            pass


    @commands.Cog.listener()    
    async def on_message_edit(self,before,after):
        try:
            await self.bot.server_config.find_field(before.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'message', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                channel=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title=f'Message edited in #{before.channel}',
                    description= f'**Before:** {before.content}\n**After**:{after.content}', timestamp=datetime.now(),
                    color=discord.Colour.red())
                embed.set_footer(text=f'ID:{before.author.id}')
                embed.set_author(name=before.author.name, icon_url= before.author.avatar)                     
                await channel.send(embed=embed)
        except KeyError:
            pass


    @commands.Cog.listener()    
    async def on_member_update(self,before,after):
        try:
            await self.bot.server_config.find_field(before.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'member', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'member', 'channel')
                channel=self.bot.get_channel(int(b))            
                if len(before.roles) > len(after.roles):
                    role = next(role for role in before.roles if role not in after.roles)
                    embed= discord.Embed(
                        title=f'Role Removed',
                        description=f'<@&{role.id}>',
                        timestamp= datetime.now(),
                        color= discord.Colour.red()
                    )
                elif len(after.roles) >len(before.roles):
                    role= next(role for role in after.roles if role not in before.roles)
                    embed= discord.Embed(
                        title=f'Roles added',
                        description=f'<@&{role.id}>',
                        timestamp= datetime.now(),
                        color= discord.Colour.red()
                    )
                elif before.nick != after.nick: #nickname
                    if before.nick is None:
                        title = 'Added'
                    elif after.nick is None:
                        title= 'Removed'
                    else:
                        title = 'Changed'         

                    embed= discord.Embed(
                        title=f'Nickname {title}',
                        description=f'**Before:** {before.nick}\n**After:** {after.nick}',
                        timestamp= datetime.now(),
                        color= discord.Colour.red()
                    )                       
                else:
                    return
                embed.set_author(name=after.name, icon_url= after.avatar)
                await channel.send(embed=embed)     
        except KeyError:
            pass


    @commands.Cog.listener()    
    async def on_guild_channel_create(self,channel):
        try:
            await self.bot.server_config.find_field(channel.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(channel.guild.id, 'commands', 'logging_cmnd', 'server', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(channel.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                channell=self.bot.get_channel(int(b))         
                embed= discord.Embed(
                    title=f'Channel created',
                    description= f'**Name:** {channel}\n**Category:** {channel.category}',
                    timestamp= datetime.now(),
                    color= discord.Colour.red())  
                await channell.send(embed=embed)
        except KeyError:
            pass

    @commands.Cog.listener()    
    async def on_guild_channel_delete(self,channel):
        try:
            await self.bot.server_config.find_field(channel.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(channel.guild.id, 'commands', 'logging_cmnd', 'server', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(channel.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                channell=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title=f'Channel deleted',
                    description= f'**Name:** {channel}\n**Category:** {channel.category}',
                    timestamp= datetime.now(),
                    color= discord.Colour.red())  
                await channell.send(embed=embed)
        except KeyError:
            pass

    @commands.Cog.listener()    
    async def on_guild_role_create(self,role):
        try:
            await self.bot.server_config.find_field(role.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(role.guild.id, 'commands', 'logging_cmnd', 'server', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(role.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                channell=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title=f'New Role Created',
                    description= f'**Name:** {role.mention}',
                    timestamp= datetime.now(),
                    color= discord.Colour.red())  
                await channell.send(embed=embed)
        except KeyError:
            pass

    @commands.Cog.listener()    
    async def on_guild_role_delete(self,role):
        try:
            await self.bot.server_config.find_field(role.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(role.guild.id, 'commands', 'logging_cmnd', 'server', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(role.guild.id, 'commands', 'logging_cmnd', 'server', 'channel')
                channell=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title=f'A Role Deleted',
                    description= f'**Name:** {role}',
                    timestamp= datetime.now(),
                    color= discord.Colour.red())  
                await channell.send(embed=embed)
        except KeyError:
            pass                                

    @commands.Cog.listener()    
    async def on_voice_state_update(self,member,before,after):
        try:
            await self.bot.server_config.find_field(member.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(member.guild.id, 'commands', 'logging_cmnd', 'voice', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(member.guild.id, 'commands', 'logging_cmnd', 'voice', 'channel')
                channel=self.bot.get_channel(int(b))
                description= f'{member.name}{after.channel}'
                if before.channel is None:
                    title = 'Joined'
                elif after.channel is None:
                    title= 'Left'
                    description= f'{member.name}{before.channel}'
                else:
                    title = 'Moved'
                embed= discord.Embed(
                    title=f'Member {title} Voice Channel',
                    description= description, timestamp=datetime.now(),
                    color=discord.Colour.red())
                embed.set_footer(text=f'ID:{member.id}')
                embed.set_author(name=member.name, icon_url= member.avatar)                     
                await channel.send(embed=embed)
        except KeyError:
            pass


    @commands.Cog.listener()    
    async def on_member_ban(self,guild,user):
        try:
            await self.bot.server_config.find_field(guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(guild.id, 'commands', 'logging_cmnd', 'moderation', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(guild.id, 'commands', 'logging_cmnd', 'moderation', 'channel')
                channell=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title='<:ban:1054132708688809985>  __BAN__  <:ban:1054132708688809985>',
                    description= f'<:prisoner:1054134753504268361> **USER:** {user.name}\n<:log:1054135131855671366> **REASON:**',
                    timestamp= datetime.now(),
                    color= discord.Colour.red()) 
                embed.set_footer(text=f'🆔 {user.id}')
                embed.set_author(name=user.name, icon_url= user.avatar)                      
                await channell.send(embed=embed)
        except KeyError:
            pass

    @commands.Cog.listener()    
    async def on_member_unban(self,guild,user):
        try:
            await self.bot.server_config.find_field(guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(guild.id, 'commands', 'logging_cmnd', 'moderation', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(guild.id, 'commands', 'logging_cmnd', 'moderation', 'channel')
                channell=self.bot.get_channel(int(b))
                embed= discord.Embed(
                    title=f'Member Unbanned',
                    description= f'**Name:** {user.name}',
                    timestamp= datetime.now(),
                    color= discord.Colour.red())  
                await channell.send(embed=embed)
        except KeyError:
            pass          

# TO DO
#If user start playing when listening to spotify bot doesnt send message
    @commands.Cog.listener()    
    async def on_presence_update(self,before,after):
        try:
            await self.bot.server_config.find_field(before.guild.id, 'commands', 'logging_cmnd')
            if await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'message', 'status') is True:
                b=await self.bot.server_config.find_field_value_value(before.guild.id, 'commands', 'logging_cmnd', 'message', 'channel')
                channel=self.bot.get_channel(int(b))
                a=(str(before.activity).lower())
                d=(str(after.activity).lower())
                if 'spotify' in a:
                    return
                elif 'spotify' in d:
                    return   
                else: 
                    if (before.activity is None) or (before.activity==after.activity):
                        await channel.send(f'{before.name} has started playing {after.activity.name}')   
                    elif after.activity is None:
                        await channel.send(f'{before.name} has stopped playing {before.activity.name}')
        except KeyError:
            pass

async def setup(bot):
    await bot.add_cog(Testa(bot))