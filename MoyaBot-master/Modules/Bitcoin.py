import requests
import pyupbit
import discord
import json


class get_coin:



    def get_coin_price(self, *keyword):
        with open('./coin.json','r') as f:
            json_data = json.load(f)
        
        #print("sssssss")

        #for x in json_data:
        #    print(x['korean_name'])
        if len(keyword) == 1:
            keywordstr = str(keyword[0])
            CoinPriceEmbed = discord.Embed(title = keywordstr, description = " ", color = 0x87cefa)
            
            for x in json_data:
                #print(x['korean_name'])
                if x['korean_name'] == keywordstr:
                    coinprice = pyupbit.get_current_price(x['market'])
                    CoinPriceEmbed.add_field(name = x['market'], value = str(coinprice))
            
            return CoinPriceEmbed
        else:
            ErrorEmbed = discord.Embed(title = "키워드가 주어지지 않았습니다!", description = " ", color = 0x87cefa)
            return ErrorEmbed
