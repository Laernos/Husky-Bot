import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class Count(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.last_counter= None

    @commands.Cog.listener()    
    async def on_message(self, message):
               
        
        if message.author.bot:
        # If the message author is a bot then ignore
            return
        if len(message.mentions) <= 0 and (not message.content.isnumeric()) and (not message.author.guild_permissions.administrator):
        # If user's message doesn't contain a mention and the message contains nonstr text and the message author doesn't have administrator permisisons
            reply= await message.reply(f'> To send non-number messages, you must mention someone or reply to someone\'s message!')  
            await reply.delete(delay=5)
            await message.delete(delay=5)
        elif len(message.mentions) <= 0 and (message.content.isnumeric()):
            try:
                db=await self.bot.server_config.find_field_value(message.guild.id,'modules', 'welcome', 'status')
                channel= await self.bot.server_config.find_field_value(message.guild.id,'modules', 'welcome', 'channel')
                if db is True and channel == message.channel.id:
                    count=await self.bot.server_config.find_field_value(message.guild.id, 'modules', 'welcome', 'count')
                    ardarda=await self.bot.server_config.find_field_value(message.guild.id, 'modules', 'welcome', 'topic')       
                    number = int(message.content) 
                    next_number= count + 1     

                    if message.author.id != self.last_counter: 
                        if number == next_number:
                            await self.bot.server_config.update_field_value(message.guild.id,'modules', 'welcome', 'count', next_number)
                            self.last_counter= message.author.id

                            if next_number == 10 or next_number == 50  or next_number == 100 or next_number == 300 or next_number == 500 or next_number == 1000 or next_number == 5000:
                                await message.reply(f'We have reached count {next_number}')
                                await message.pin(reason=f'Server reached count {next_number} in {message.channel.name}')

                        else:                        
                            reply= await message.reply(f'> WRONG NUMBER\n Next Number: {next_number}')  
                            await reply.delete(delay=5)
                            await message.delete(delay=5)

                    else:
                        reply= await message.reply(f'> You cannot count by yourself')  
                        await reply.delete(delay=5)
                        await message.delete(delay=5)                        
                    




            except KeyError:
                pass        


async def setup(bot):
    await bot.add_cog(Count(bot))