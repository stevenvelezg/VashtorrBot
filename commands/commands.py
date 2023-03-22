from discord.ext import commands

class Commands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="test")
    async def test(self, ctx):
        await ctx.send('Testing functions.')

async def setup(bot):
    await bot.add_cog(Commands(bot))