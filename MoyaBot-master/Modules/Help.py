#Coding "UTF-8"


import discord

class Help:
    def Create_help_embed(self):
        Moya_help = discord.Embed(title = "Moya 명령어!", description = " ", color = 0x87cefa)
        Moya_help.add_field(name = "#명령어", value = "모야에 있는 명령어인데요?",inline=False)
        Moya_help.add_field(name = "#모야", value = "뭐요 모야요.",inline=False)
        Moya_help.add_field(name = "#roll", value = "정해준 범위 내의 랜덤한 수를 출력합니다.(기본 1 ~ 6)",inline=False)
        Moya_help.add_field(name = "#이미지 [키워드]", value = "구글에서 검색해 가장 위에 있는 사진을 보여줍니다.")
        Moya_help.add_field(name = "#업비트 [코인한글이름]", value = "검색하신 코인의 현재 싯가를 보여줍니다.")
        Moya_help.add_field(name = "#고르기 [목] [록] [들]", value = "여러개의 목록들을 입력하면 그 중 하나를 골라줍니다.")
        Moya_help.add_field(name = "#play [링크]", value = "링크에 있는 음악을 재생합니다.",inline=False)
        #이 밑은 구현해야할 것들. 
        Moya_help.add_field(name = "#유튜브 [검색키워드]", value = "유튜브에서 검색 키워드로 검색한 후, 가장 위에 있는 재생목록을 재생합니다.")
        Moya_help.add_field(name = "#큐", value = "현재 재생목록을 보여줍니다.")
        #여기까지 명령어 리스트. 
        Moya_help.set_author(name="나는 모야!", icon_url="https://cdn.discordapp.com/attachments/751451358477156363/787028669793042457/39d50e8028f8e642.jpg")
        Moya_help.set_image(url = "https://64.media.tumblr.com/b090d079a5b7a0e27824f4f046ba938c/1e1fc0a1f330d37e-3c/s1280x1920/13696c716d01a11499ad8a06a7b1b1d6e8aab1f9.jpg")
        Moya_help.set_footer(text = "Ver.2021-4-12")
        return Moya_help

    def Create_Moya_description(self):
        Moya_description = discord.Embed(title = "안녕하세요!", description = "모야!", color = 0x87cefa)
        Moya_description.add_field(name="안내", value="기본 명령어 #[명령어]임. #도움말 로 기본 명령어나 확인하세요.")
        Moya_description.add_field(name="문의", value= "E-mail - eyiuta1@gmail.com 디스코드 - 향림#1522 트위터 - https://twitter.com/H_Rim_D")
        return Moya_description