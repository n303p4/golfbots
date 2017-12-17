import discord # This bot is released into the public domain, under the terms of the Unlicense. See http://unlicense.org/ for details.
from discord.ext import commands
bot = commands.AutoShardedBot(command_prefix=commands.when_mentioned_or("tam ", "tam"))
bot.description = "This is Tamamo, a discord.py bot written in no more than 20 lines. Using semicolons is cheating."
bot.check(lambda ctx: not ctx.author.bot) # Prevent the bot from replying to other bots.
@bot.event # Two-line error handler that avoids unknown command messages and check failure responses.
async def on_command_error(ctx, exc): (await ctx.send(exc)) if not isinstance(exc, (commands.CommandNotFound, commands.CheckFailure)) else None
@bot.command(aliases=["pong", "echo", "say"], help="Pings the bot.")
async def ping(ctx, *, message:str=None): (await ctx.send("\u200b" + message)) if message else (await ctx.send(":ping_pong:"))
@bot.command(name="user", aliases=["uinfo", "userinfo"], help="Shows information about a user.")
async def _user(ctx, *, user:discord.Member): await ctx.send(f"**{user.name}#{user.discriminator}** ({user.id})\nNickname: {user.nick}\nBot? {user.bot}\nStatus: {user.status.name}\nJoined guild: {user.joined_at.ctime()}\nJoined Discord: {user.created_at.ctime()}\n{user.avatar_url_as(format='png', size=128)}")
@bot.command(aliases=["server", "sinfo", "serverinfo", "ginfo", "guildinfo"], help="Shows information about the current guild.")
async def guild(ctx): await ctx.send(f"**{ctx.guild.name}** ({ctx.guild.id})\nOwner: {ctx.guild.owner.name}#{ctx.guild.owner.discriminator}\nMembers: {len(ctx.guild.members)}\nText channels: {len(ctx.guild.text_channels)}\nVoice channels: {len(ctx.guild.voice_channels)}\nRoles: {len(ctx.guild.roles)}\nCustom emojis: {len(ctx.guild.emojis)}\nRegion: {ctx.guild.region}\n{ctx.guild.icon_url}")
@bot.command(aliases=["elist"], help="Lists the guild's custom emojis.")
async def emojis(ctx): (await ctx.send(f"{''.join(list(str(emoji) for emoji in ctx.guild.emojis))}")) if len(ctx.guild.emojis) else (await ctx.send("This guild has no custom emojis."))
@bot.command(aliases=["xk"], help="Fetches an xkcd comic by number.")
async def xkcd(ctx, number:int=None): (await ctx.send(f"https://xkcd.com/{number}")) if number else (await ctx.send("https://xkcd.com/"))
@bot.command(aliases=["shutdown", "kys"], help="Halts the bot. Owner only.")
async def halt(ctx): (await bot.logout()) if (await bot.is_owner(ctx.author)) else (await ctx.send("You do not own this bot."))
bot.run(open("oauth.txt").read().strip("\n")) # Token should be stored in oauth.txt. The bot won't run without it.
