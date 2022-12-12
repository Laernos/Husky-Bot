import discord
from discord import File
from discord.ext import commands
from easy_pil import Editor, load_image_async, Font


class Welcome(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self,member):
        channel = member.guild.system_channel
        if channel is not None:
            background= Editor('pic3.png')
            profile_image = await load_image_async(str(member.avatar.url))
            profile = Editor(profile_image).resize((200,200)).circle_image()
            poppins = Font.poppins(size=50, variant='bold')
            poppins_small= Font.poppins(size=20, variant='light')
            background.paste(profile, (756,77))
            background.text((450,140), f'{member.name}#{member.discriminator}', color='white', font=poppins, align='center')
            file= File(fp=background.image_bytes, filename='pic1.jpg')
            await channel.send(f'welcome to my server v2')
            await channel.send(file=file)    

        try:
            if self.bot.muted_users[member.id]:
                role = discord.utils.get(member.guild.roles, name= 'Muted')
                if role:
                    await member.add_roles(role)
                    print(f'Remuted {member.display_name} upon guild entry')
        except KeyError:
            pass


async def setup(bot):
    await bot.add_cog(Welcome(bot))