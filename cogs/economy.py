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
        await self.bot.economy.insert(data)

    @commands.hybrid_command(name='balance', description = 'Check your wallet', aliases=['bal','coin'])
    async def balance(self,ctx):
        member= ctx.author        
        find= await self.bot.db.economy.find_one({'_id': member.id})
        if not find:
            await self.create_account(member.id)

        embed=discord.Embed(description=f'You have {find["coin"]} coins', color=0xff0000)
        await ctx.send(embed=embed)





    user = interaction.user.id
    valid = False
    user_info = collection.find({"user": user})




    

async def setup(bot):
    await bot.add_cog(Economy(bot))



    