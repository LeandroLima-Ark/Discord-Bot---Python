import discord
from discord.ext import commands

from DiscordToken import Discord_Token
import utils.Math
import utils.Embeds

perm = discord.Intents.all()
bot = commands.Bot(".", intents=perm)

@bot.event
async def on_ready():
    print("Bot inicializado com sucesso!")

@bot.event
async def on_reaction_add(react:discord.reaction, user:discord.Member):
    if user.bot:
        return
    
    if str(react.emoji) == "🍅":
        emb, file = utils.Embeds.Tomato_embed(
            f"{user.name} reagiu a {react.message.author.name}",
            utils.Embeds.getDesc(utils.Math.rollnumber(1,14), react.message.author.mention, user.mention),
            utils.Math.rollnumber(1,5))
        
        await react.message.channel.send(embed=emb, file=file)

@bot.command()
async def say(ctx:commands.Context, *, texto):
    await ctx.message.delete()
    await ctx.send(texto)

@bot.command()
async def toma(ctx:commands.Context):
    message = [msg async for msg in ctx.channel.history(limit=2)]
    last = message[1]
    await ctx.message.delete()
    await last.add_reaction("🍅")

@bot.command()
async def love(ctx:commands.Context, *people:discord.Member):
    people = list(people)
    if len(people)==1:
        pessoa = people[0]
        await ctx.reply(f"O amor está no ar!! \nO Nível de amor entre {ctx.author.mention} e {pessoa.mention} é de: {utils.Math.rollnumber(1, 1000)}")
    else:
        p1, p2 = people
        await ctx.reply(f"O amor está no ar!! \nO Nível de amor entre {p1.mention} e {p2.mention} é de: {utils.Math.rollnumber(1, 1000)}")

@bot.command()
async def roll(ctx:commands.Context, faces:int):
    await ctx.send(f"Número: {utils.Math.rollnumber(1, faces)}")

@bot.command()
async def calc(ctx:commands.Context, op, num1: int, num2:int):
    resultado:int = 0
    if op == "soma":
        resultado = utils.Math.func_somar(num1, num2)
    elif op == "sub":
        resultado = utils.Math.func_sub(num1, num2)
    elif op == "mult":
        resultado = utils.Math.func_mult(num1, num2)
    elif op == "div":
        resultado = utils.Math.func_div(num1, num2)
    await ctx.send(f"Resultado: {resultado}")

bot.run(Discord_Token)
