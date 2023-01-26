import requests as r
import uuid
from getpass import getpass as getpw
from bs4 import BeautifulSoup


class Insta_AutoLogin(object):
    def __init__(self,username,password):
        
            def header():
                self.headers = {
                    'User-Agent':'Instagram 125.0.0.18.125 (iPhone11,8; iOS 13_3; en_US; en-US; scale=2.00; 828x1792; 193828684)', 
                    'Accept':'*/*', 
                    'Accept-Encoding':'gzip, deflate', 
                    'Accept-Language':'en-US', 
                    'X-IG-Capabilities':'3brTvw==', 
                    'X-IG-Connection-Type':'WIFI', 
                    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
                    'Host':'i.instagram.com'}
                return self.headers


            
            def main():
                try:
                    self.url = "https://i.instagram.com/api/v1/accounts/login"
                    self.uuid_ = uuid.uuid4()
                    self.data = {
                        '_uuid':self.uuid_, 
                        'username':username, 
                        'enc_password':f"#PWD_INSTAGRAM_BROWSER:0:1589682409:{password}", 
                        'queryParams':'{}', 
                        'optIntoOneTap':'false', 
                        'device_id':self.uuid_, 
                        'from_reg':'false', 
                        '_csrftoken':'missing', 
                        'login_attempt_count':'0'}

                    go = r.post(url=self.url,data=self.data,headers=header())

                    if 'logged_in_user' in go.text:
                            try:
                                session_id = go.cookies.get_dict()['sessionid']
                                print(session_id)
                            except Exception as e:
                                return {"bad":"로그인 실패..","Error":e}
                            return {"result":"로그인완료!","data":session_id}
                            

                except Exception as er:
                        return {"bad":"로그인 실패..","Error":er}
                        
            result__ = main()

            if result__["로그인완료!"]:
                print(result__["result"])
            else:
                print("error")

                      






