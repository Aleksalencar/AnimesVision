import AnimesVisionBot
bot = AnimesVisionBot.AnimesVisionBot()


animes = bot.list_animes()
escolha = bot.chosse_anime(animes) #retorna web element
episodios_urls = bot.select_ep(escolha)
video_names = []
for url in episodios_urls:
    video_names.append(bot.download(url))
