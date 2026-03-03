import discord

def Tomato_embed(Title, Description, ImageNumber):
    myemb = discord.Embed()
    myemb.title = Title
    myemb.description = Description
    myemb.color = discord.Color.dark_orange()

    img = discord.File(f"imgs//tomato{ImageNumber}.gif", "Image.gif")
    myemb.set_image(url="attachment://Image.gif")

    return myemb, img

def getAvatar(ctx):
    return ctx.author.display_avatar.url

def getDesc(number:int, X, Y):
    descricoes = [
        f"{X} abriu a boca pra falar besteira… e {Y} abriu a plantação inteira e mandou um tomate na cara dele.",
        f"{X} achou que tava arrasando no discurso, mas {Y} achou que era stand-up ruim e resolveu tomatar sem dó.",
        f"{X} falou com tanta confiança que {Y} ficou com pena… e jogou um tomate pra ajudar a cair na real.",
        f"{X} soltou a frase proibida do servidor, e {Y} ativou o modo fazendeiro e partiu pro tomate.",
        f"{X} mal terminou de falar… {Y} já tava com o tomate engatilhado. Acerto crítico na vergonha alheia.",
        f"{X} achou que aquela ideia era genial… {Y} achou que era caso de tomate urgente.",
        f"{X} falou tão sério que {Y} pensou que era piada — e respondeu no único idioma possível: tomate.",
        f"{X} terminou a frase confiante. {Y} terminou a paciência. Tomate lançado com sucesso.",
        f"{X} tentou argumentar. {Y} tentou dialogar. O tomate falou mais alto.",
        f"{X} abriu a boca achando que ia convencer alguém… {Y} abriu a geladeira e pegou o tomate.",
        f"{X} disse isso em público. {Y} acionou o protocolo anti-vergonha: tomate imediato.",
        f"{X} entrou no personagem do palestrinha. {Y} entrou no personagem do agricultor profissional.",
        f"{X} jogou a opinião no chat. {Y} jogou o tomate na testa.",
        f"{X} mandou a mensagem mais duvidosa do dia. {Y} respondeu com um tomate perfeitamente maduro.",
        f"{X} falou achando que ia passar batido. {Y} não deixou — passou foi o tomate."
    ]
    return descricoes[number]
    