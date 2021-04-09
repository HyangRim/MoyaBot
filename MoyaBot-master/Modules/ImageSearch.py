import bs4
import lxml
import discord
from urllib.request import urlopen, Request
import urllib
import json
import requests
import random

class Search:
    def get_video_link(self, keyword):
        pass

    def Search_Image(self, keyword):
        title = ''
        for i in keyword:
            title = title + i
        enc_location = urllib.parse.quote(title)
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.google.co.kr/search?hl=en&tbm=isch&q=' + enc_location
        #디버깅용 코드
        #print(url)
        #print(title)
        print(keyword)
        print(enc_location)
        req = Request(url,headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html,"lxml")
        embed = discord.Embed(color = 0x87cefa)
        imgdinfl = bsObj.find_all("img")
        #print(imgdinfl)
        try:
            randomNum = random.randint(0,(len(imgdinfl) - 1))
            imgsrc = imgdinfl[randomNum].get('src')
            embed.set_image(url=imgsrc)
            print(imgsrc)
        except ValueError:
            embed.add_field(name="검색된 사진이 없는데요?",value="없다구요")
        return embed