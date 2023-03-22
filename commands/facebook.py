from discord.ext import commands
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

class Facebook(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        
    def generate_selenium(self):
        options = Options()
        options.headless = True
        url = "https://www.facebook.com/WarhammerPlainview/"
        driver = webdriver.Chrome(options=options)
        driver.get(url)
        # driver.implicitly_wait(10)
        html = driver.page_source
        soup = BeautifulSoup(html, "html.parser")
        return soup
    
    @commands.command(name="get")
    async def get(self, ctx):
        soup = self.generate_selenium()
        # posts = soup.select(".x11i5rnm, .xat24cr, .x1mh8g0r, .x1vvkbs, .x126k92a > div::text")
        posts = soup.select(".x1iorvi4, .x1pi30zi, .x1swvt13, .xjkvuk6 > div > div > span > div")
        results = [r.text.strip() for r in posts]
        print(results)
        print(results.__len__())

        # await ctx.send(soup.prettify())

    @commands.command(name="ftest")
    async def ftest(self, ctx):
        await ctx.send("Facebook test")


async def setup(bot):
    await bot.add_cog(Facebook(bot))