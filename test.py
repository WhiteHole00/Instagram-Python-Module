from insta_package import Insta_Follower_Scraper,insta_dm_spammer,insta_Auto_DM,insta_AutoLogin
import insta_package
from only_pc_config import username,password,target
ment = open('ment.txt', 'r', encoding="UTF-8")
real_ment = ment.read().split('\n')
ment.close()


def run():
   insta_dm_spammer.Insta_Auto_DM_Spammer(login_user=username,login_password=password,target=target,Timeout=60,message=real_ment,count=3)


run()    