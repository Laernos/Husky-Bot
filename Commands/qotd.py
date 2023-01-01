import discord
from discord.ext import commands
from discord import app_commands
import random

class QuestionofDay(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.questions=[
        "What is your favorite color?",
        "What is your favorite food?",
        "What is your favorite hobby?",
        "What is your favorite movie?",
        "What is your favorite book?",]
        self.counter = 0

    @commands.command()
    async def question_of_the_day(self,ctx):
        global counter

        # Select the current question from the list
        question = self.questions[self.counter]

        # Increment the counter
        self.counter += 1

        # Reset the counter if it reaches the end of the list
        if self.counter >= len(self.questions):
            self.counter = 0

        # Send the question to the user
        await ctx.send(question)


    

async def setup(bot):
    await bot.add_cog(QuestionofDay(bot))