import os
from webdriver import Driver
import logging

logging.basicConfig(filename='logs', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
driver = Driver.Driver('D:\Downloads\Chrome', True).driver

class AnimesVisionBot:
    def list_animes(self):
        print('.: Downaload no Animes Vision :.')
        print('Digite o termo para a pesquisa')
        while True:
            try:
                print('>>',end=' ')
                key = str(input())
                break
            except:
                print('<< Invalido')
                continue
        logging.info('Pesquisando ' + key)
        try:
            driver.get('https://animesvision.biz/search?query=' + key)
            animes = driver.find_elements_by_class_name('thumb')
            if len(animes) == 0:
                print('Nenhum resultado para a sua busca :(')
        except:
            logging.info('Elemnto não encontrado')
        return animes

    def chosse_anime(self, animes):
        if len(animes) == 0:
            logging.info('Nenhum resultado para a sua busca :(')
        for i in range(len(animes)):
            print(i, ' -> ', animes[i].get_attribute("title"))
        print(">> ", end=' ')
        choice = int(input())
        logging.info('Anime escolhido' + animes[choice].get_attribute("title"))
        return animes[choice]

    def select_ep(self, choice):
        url = choice.get_attribute("href")
        logging.debug('indo para ' + url)
        driver.get(url)
        episodes = driver.find_elements_by_xpath("//*[@id='episodes-sv-1']/li/div[1]/a")
        episodes_urls = [ep.get_attribute("href") for ep in episodes]
        size = len(episodes_urls)
        print('O anime possui atualmente', size,
              'episodios\n-1 -> Para o ultimo episodio\n-2 -> Para todos os episodios\n1 a', size,
              '-> Para index especifico')
        while True:
            print(">> ", end=' ')
            try:
                opc = int(input())
                url = []
                if opc == -1:
                    url.append(episodes_urls[-1])
                    return url
                    break
                elif opc == -2:
                    return episodes_urls
                    break
                elif 0 < opc <= size:
                    url.append(episodes_urls[opc - 1])
                    return url
                    break
            except:
                print('<< Valor invalido')
                continue

    def download(self, episodio):
        driver.get(episodio)
        src = driver.find_element_by_css_selector("#playersd > div.jw-wrapper.jw-reset > div.jw-media.jw-reset > video")
        src = src.get_attribute('src')
        best_quality = self.get_qualitys()
        download_url = src.split('/')
        name = download_url[-1]
        download_url[-2] = best_quality
        separetor = '/'
        download_url = separetor.join(download_url)
        import urllib.request
        urllib.request.urlretrieve(download_url, 'video_name.mp4')
        if self.has_error():
            print('Inciando downaload de', name)
        else:
            print('Download falho: ', download_url)
        return name

    def get_qualitys(self):
        px = ['480p', '720p', '1080p']
        qualitys = driver.find_elements_by_xpath('//*[@id="main-content"]/div[1]/div[2]/div[3]/div/div[1]/ul/li/a')
        return px[len(qualitys) -2]

    def has_error(self):
        try:
            driver.find_elements_by_css_selector(
                '#collapsible0 > div.expanded > div.collapsible-content > div:nth-child(2) > span.text')
            return True
        except:
            return False
        pass


class Renamer:
    def rename(self, actual, new):
        os.rename(actual, new)
        pass

