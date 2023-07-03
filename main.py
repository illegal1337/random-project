import discord; from discord.ext import commands

token = ""

prefix = "$"

name = ""

pfp = open(f'img.png', 'rb')

credits = "made by illegal" # dont remove credits please

intents = discord.Intents.all()

bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def change_name(ctx):
  try:
    await ctx.message.delete()
    await bot.user.edit(username=name)
    print("bot username changed")
  except Exception as e:
    print(e)

@bot.command()
async def change_pfp(ctx):
  await ctx.message.delete()
  await bot.user.edit(avatar=pfp.read())
  print("bot pfp changed")

cmds = print(f"""
                CMDS:
{prefix}change_name - change bot username
{prefix}change_pfp - change bot pfp
this has been {credits}, dont skid""")

bot.run(token)
