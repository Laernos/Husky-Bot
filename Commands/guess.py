import discord
from discord.ext import commands
from discord import app_commands
import random
import asyncio

class Guess(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.tries= 0
        self.hint1= 0
        self.hint2=  0  

    
    @commands.Cog.listener()    
    async def on_message(self, message):
               


        def hintnumbers(self, number):
            self.hint1= number - random.randint(1, 15)
            self.hint2= number + random.randint(1, 15)

            if self.hint1 < 1:
                self.hint1= 0
            if self.hint2 > 100:
                self.hint2= 100
            return
        
        if message.author.bot:
        # If the message author is a bot then ignore
            return

        if len(message.mentions) <= 0 and (not message.content.isnumeric()) and (not message.author.guild_permissions.administrator):
        # If user's message doesn't contain a mention and the message contains nonstr text and the message author doesn't have administrator permisisons
            reply= await message.reply(f'> To send non-number messages, you must mention someone or reply to someone\'s message!')  
            await reply.delete(delay=5)
            await message.delete(delay=5)   
        elif len(message.mentions) <= 0 and (message.content.isnumeric()):
        # If message doesnt contain any mention and numeric
            try:
                db=await self.bot.server_config.find_field_value(message.guild.id,'modules', 'guess', 'status')
                channel= await self.bot.server_config.find_field_value(message.guild.id,'modules', 'guess', 'channel')
                if db is True and channel == message.channel.id:
                    number=await self.bot.server_config.find_field_value(message.guild.id, 'modules', 'guess', 'number')
                    hint=await self.bot.server_config.find_field_value(message.guild.id, 'modules', 'guess', 'hint')              
                    guess = int(message.content)                    

                    if 0 < guess <= 100:
                    # If guess between 0 and 100   
                        self.tries += 1

                        if self.tries == hint:
                            hintnumbers(self,number)
                            embed=discord.Embed(title='', description=f'The number between **{self.hint1}** and **{self.hint2}**.', color=0xffc107,)
                            embed.set_thumbnail(url='https://imgur.com/ZRXP7ad.png')
                            embed.set_author(name='HINT TIME',)
                            await message.channel.send(embed=embed)                                                                                    
                        if guess == number:
                        # Check if the guess is correct
                        # TODO: Add how many times the user has won the game!
                            # Winner Embed
                            embed=discord.Embed(title='We have a winner!', description='',color=discord.Colour.green(),)
                            embed.add_field(name='Number You Found', value=number)
                            embed.set_author(name= message.author.name, icon_url=message.author.avatar)
                            # New Game Embed
                            embed2=discord.Embed(title='NEW NUMBER CREATED', description='Find this number between 1 and 100, Good Luck :D', color=message.guild.me.top_role.colour,)
                            embed2.add_field(name='Hint Time', value=f'**{hint}**  Wrong Answers')
                            embed2.set_author(name= message.guild.name, icon_url=message.guild.icon)                           
                            await message.channel.send("", embeds=[embed, embed2])
                            number = random.randint(1, 100)   
                            await self.bot.server_config.update_field_value(message.guild.id,'modules', 'guess', 'number', number)
                            self.tries=0
                    else:
                    # Guess is not between 0 and 100    
                        reply= await message.reply(f'> Guess must be between 1 and 100!')  
                        await reply.delete(delay=3)
                        await message.delete(delay=3)           
                
            except KeyError:
                pass        


async def setup(bot):
    await bot.add_cog(Guess(bot))