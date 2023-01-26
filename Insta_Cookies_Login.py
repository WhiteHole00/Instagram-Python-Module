import requests as r
import uuid
from getpass import getpass as getpw
from bs4 import BeautifulSoup

def header():
    headers = {
    'User-Agent':'Instagram 125.0.0.18.125 (iPhone11,8; iOS 13_3; en_US; en-US; scale=2.00; 828x1792; 193828684)', 
    'Accept':'*/*', 
    'Accept-Encoding':'gzip, deflate', 
    'Accept-Language':'en-US', 
    'X-IG-Capabilities':'3brTvw==', 
    'X-IG-Connection-Type':'WIFI', 
    'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8', 
    'Host':'i.instagram.com'}
    return headers


def login(user,pw):

    try:
        url = 'https://i.instagram.com/api/v1/accounts/login/'
        uuid_ = uuid.uuid4()

        data = {
            '_uuid':uuid_, 
            'username':user, 
            'enc_password':f"#PWD_INSTAGRAM_BROWSER:0:1589682409:{pw}", 
            'queryParams':'{}', 
            'optIntoOneTap':'false', 
            'device_id':uuid_, 
            'from_reg':'false', 
            '_csrftoken':'missing', 
            'login_attempt_count':'0'}

        go = r.post(url=url,data=data,headers=header())

        if 'logged_in_user' in go.text:
            try:
                session_id = go.cookies.get_dict()['sessionid']
                print(session_id)
            except Exception as e:
                #print(e)
                return {"bad":"로그인 실패..","Error":e}
            return {"result":"로그인완료!","data":session_id}

    except Exception as er:
        #print(er)
        return {"bad":"로그인 실패..","Error":er}





def main():
    us = input("유저이름 >> ")
    pwpw = getpw("비번 >> ")
    print(pwpw)

    result_ = login(us,pwpw)

    if result_["result"] == "로그인완료!":
        print(result_["result"])
    else:
        print(result_["bad"])        


main()        



