# tamamo
`tamamo` is a 20-line code golf Discord bot written in Python, using the discord.py library.

# How to run
You'll need to install Python 3.6 or higher, as well as the rewrite branch of discord.py. This is
not a beginner's bot and I will not explain how to install either of those things here. Once
you've got everything set up, create a file called `oauth.txt` and put your bot token into it.
Then run `tamamo.py` and the bot should come online.

# How to use
`tamamo` uses `tam` as a prefix, or you can mention the bot. The full set of commands is listed
below.

* `emojis` - Lists the guild's custom emojis.
* `guild` - Shows information about the current guild.
* `halt` - Halts the bot.
* `help` - Shows the list of commands.
* `ping` - Pings the bot.
* `user` - Shows information about a user.
* `xkcd` - Generates an xkcd URL by number.

# Behavior
Despite its small size and nature as a "novelty bot", `tamamo` largely tries to follow good bot
practices. For example, it responds to mentions, it ignores other bots, and it includes basic
error handling for when a command fails. Because it is based on discord.py's command extension,
`tamamo` also has a functional `help` command. However, it lacks command cooldowns and its outputs
are generally unattractive.
