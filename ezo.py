from discord.ext import commands # This bot is released into the public domain, under the terms of the Unlicense. See http://unlicense.org/ for details.
bot = commands.Bot(command_prefix=commands.when_mentioned_or("ezo ", "ezo"))
bot.description = "Ezo is yet another code golf Discord bot. Using semicolons is cheating."
bot.check(lambda ctx: not ctx.author.bot) # Prevent the bot from replying to other bots.
@bot.event # Two-line error handler that avoids unknown command messages and check failure responses.
async def on_command_error(ctx, exc): await ctx.send("No results found. Make sure you're using valid tags, such as `fox_ears`. :<") if isinstance(exc, commands.CommandInvokeError) and isinstance(exc.original, IndexError) else ((await ctx.send(exc)) if not isinstance(exc, (commands.CommandNotFound, commands.CheckFailure)) else None)
@bot.command(aliases=["pong", "echo", "say"], help="Pings the bot.")
@commands.cooldown(6, 12, commands.BucketType.user)
async def ping(ctx, *, message:str=None): (await ctx.send("\u200b" + message)) if message else (await ctx.send(":ping_pong:"))
@bot.command(aliases=["dice", "rolldice"], help="Rolls some six-sided dice.")
@commands.cooldown(6, 12, commands.BucketType.user)
async def roll(ctx, number_of_dice:int): await ctx.send(", ".join([str(__import__("random").SystemRandom().randint(1, 6)) for time in range(0, min(max(number_of_dice, 1), 10))]))
@bot.command(aliases=["sbooru", "sb"], help="Fetches a random image from Safebooru. Optional tags.")
@commands.cooldown(6, 12, commands.BucketType.user)
async def safebooru(ctx, *, query=""): await ctx.send("https:" + __import__("random").SystemRandom().choice(__import__("bs4").BeautifulSoup((await(await __import__("aiohttp").request("GET", f"https://safebooru.org/index.php?page=dapi&s=post&q=index&tags={query}")).text())).find_all("post"))["file_url"])
@bot.command(aliases=["shutdown", "kys"], help="Halts the bot. Owner only.")
async def halt(ctx): (await bot.logout()) if (await bot.is_owner(ctx.author)) else (await ctx.send("You do not own this bot."))
bot.run(open("oauth.txt").read().strip("\n")) # Token should be stored in oauth.txt. The bot won't run without it.
