# tamamo
`tamamo` is a 20-line code golf Discord bot written in Python, using the discord.py library.

# ezo
`ezo` is a very similar 18-line Discord bot.

# How to run
You'll need to install Python 3.6 or higher, as well as the rewrite branch of discord.py. This is
not a beginner's bot and I will not explain how to install either of those things here. Once
you've got everything set up, create a file called `oauth.txt` and put your bot token into it.
Then run the respective `.py` file of whichever bot you want to run, and it should come online.

# How to use
`tamamo` uses `tam` as a prefix, or you can mention the bot. Similarly, `ezo` uses `ezo` as a prefix.
The full sets of commands are listed below.

## tamamo

* `emojis` - Lists the guild's custom emojis.
* `guild` - Shows information about the current guild.
* `halt` - Halts the bot. Owner only.
* `help` - Shows the list of commands.
* `ping` - Pings the bot.
* `user` - Shows information about a user.
* `xkcd` - Generates an xkcd URL by number.

## ezo

* `halt` - Halts the bot. Owner only.
* `help` - Shows the list of commands.
* `ping` - Pings the bot.
* `roll` - Rolls some six-sided dice.
* `safebooru` - Fetches a random image from Safebooru. Optional tags.

# Behavior
Despite their small sizes and natures as "novelty bots", the bots in this repository largely try to
follow good bot practices. For example, they respond to mentions, they ignore other bots, and they
include basic error handling for when commands fail. Because they're based on discord.py's command
extension, they also have functional `help` commands. However, their outputs are generally
unattractive, and `tamamo` in particular has no command cooldowns.
