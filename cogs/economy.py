import discord
from discord.ext import commands
from discord import app_commands


class Economy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def create_account(self, ctx,):
        member= ctx.author
        data = {
            '_id': member.id,
            'coin': 100,
            'inventory': []
        }
        await self.bot.db.economy.insert(data)

    @commands.hybrid_command(name='balance', description = 'Check your wallet', aliases=['bal','coin'])
    async def balance(self,ctx):
        member= ctx.author        
        find= await self.bot.db.economy.find_one({'_id': member.id})
        embed=discord.Embed(description=f'You have {find["coin"]} coins', color=0xff0000)
        await ctx.send(embed=embed)


    
    @commands.command()
    async def asa(self, ctx,):
        data = {
            '_id':'Alper',
        }
        self.bot.test.insert_one(data)

    @commands.command()
    async def update(self, ctx,):
        data = {
            '_id':'Alper',
        }
        self.bot.test.update_one({'_id': 'Alper'}, {'$set':{'age':'20'}})    

    @commands.command()
    async def find(self,ctx):
        server=self.bot.test.find_one({'_id':'Alper'})
        age = server['age']
        await ctx.send(age)

async def setup(bot):
    await bot.add_cog(Economy(bot))



    