
"""
ko - 한글
en - 영어
ja - 일본어
zh-CN - 중국어 간체
zh-TW - 중국어 번체
vi - 베트남어
id	인도네시아어
th	태국어
de	독일어
ru	러시아어
es	스페인어
it	이탈리아어
fr	프랑스어

"""
import requests

papaclient_id = ""
papaclient_secret = ""
url = "https://openapi.naver.com/v1/papago/n2mt"

class PaPago:


    def Transalte(self, *keyword):
        
        if len(keyword) == 3:
            try:
                Targetlang = str(keyword[1]);
                encText = str(keyword[2]);

                headers= {"X-Naver-Client-Id": papaclient_id, "X-Naver-Client-Secret":papaclient_secret}
                params = {"source": "ko", "target": Targetlang, "text": encText}
                response = requests.post(url, headers=headers, data=params)
                res = response.json()
                returnstr = encText + " >> " + res['message']['result']['translatedText']
                return returnstr
            except:
                return "번역 실패"
        else: 
            return "명령어 규격이 잘못되었습니다. 문장번역이나, #파파고 <언어> <할 말> 형식으로 입력해주세요."

    def Sentence_Translate(self, *keyword):

        if len(keyword) == 3:
            try:
                Targetlang = str(keyword[1]);
                encText = str(keyword[2]);

                headers= {"X-Naver-Client-Id": papaclient_id, "X-Naver-Client-Secret":papaclient_secret}
                params = {"source": "ko", "target": Targetlang, "text": encText}
                response = requests.post(url, headers=headers, data=params)
                res = response.json()
                returnstr = encText + " >> " + res['message']['result']['translatedText']
                return returnstr
            except:
                return "번역 실패"
        elif len(keyword) > 3:
            print("하위^^")
            try:
                Targetlang = str(keyword[1]);
                encText = ""
                for i in keyword[2:]:
                    encText += i
                    encText += " "

                headers= {"X-Naver-Client-Id": papaclient_id, "X-Naver-Client-Secret":papaclient_secret}
                params = {"source": "ko", "target": Targetlang, "text": encText}
                response = requests.post(url, headers=headers, data=params)

                res = response.json()
                returnstr = encText + " >> " + res['message']['result']['translatedText']
                return returnstr
            except:
                return "번역 실패"
        else: 
            return "명령어 규격이 잘못되었습니다. 문장번역이나, #파파고 <언어> <할 말> 형식으로 입력해주세요."
        
        


            

