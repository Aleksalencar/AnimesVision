episodio = 'https://animesvision.biz/animes/bna/episodio-02/legendado'
src = 'https://forja8.animesvision.biz/assistir/XywfeP-MnWZBGp0TX2Bq5w/1586493701/0rM1ni4YIME3FGl1pPDW/ogrimmar2/B/Bna/480p/AnV-02.mp4'
best_quality = '1080p'
download_url = src.split('/')
download_url[-2] = best_quality
separetor = '/'
download_url = separetor.join(download_url)
print(download_url)

