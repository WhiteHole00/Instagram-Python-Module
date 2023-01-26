from setuptools import setup, find_packages


lo = """
# InstaGram Package | By WhiteHole


`pip install insta-pkg`

• Example Code

```python
from insta_package import Insta_Follower_Scraper , insta_AutoLogin

username = "로그인에 필요한 유저아이디"
password = "로그인에 필요한 비번"
target = "팔로우 파싱을 할 유저"

Insta_Follower_Scraper.Follower_Parser(login_user=username,login_password=password,target=target,Timeout=60) #팔로우 파싱
insta_AutoLogin.Insta_AutoLogin(username=username,password=password,timeout=60) #오토로그인
   
```



모듈링크 : https://pypi.org/project/insta-pkg/

- Discord : 화이트홀미만잡#8210

- Telegram : @whitehole0906

```
Update Logs

2022-10-01 
- 오토 로그인 개발 [ 오류 패치중 ] ( 버전 : 1.0.4 ) 

2022-10-01 
- 오토로그인 패치 완료 인스타 팔로우 스크래퍼 개발중 ( 버전 : 1.0.1.5 )

2022-10-02
- 오토로그인 & 인스타 팔로우 스크래퍼 개발 거의 완성 & 클래스 나뉨(버전 : 1.1.0.3)

2022-10-02
- pypi 설명 추가 및 인스타 파서 개발 준비중 (버전 : 1.1.0.4)

2022-10-02
- 인스타 팔로워 파서 개발 95% 완성 (버전 : 1.1.0.5)

2022-10-03
- 인스타 팔로잉 ,팔로워 파서 개발완료 [팔로워는 98%개발 현재 인스타 시간제한 먹음] (버전 : 1.1.0.6)

2022-10-04
- 인스타 팔로잉 ,팔로워 파서 개발완료 & 웹훅로그 추가 완료 [ 인스타 파서 개발중 ] (버전 : 1.1.0.7)

2022-10-05
- 인스타 오토디엠 먼저 개발완료 [ 인스타 파서 여젼히 개발중 ] (버전 : 1.2.0.0)

2022-10-05
- 인스타 오토디엠 오류 패치 및 인스타 디엠 도배 개발완료 [ 인스타 파서 여젼히 개발중 ] (버전 : 1.2.0.1)

2022-10-05
- 인스타 파서 개발 중단 및 인스타 오토 로그인 셀레니움 빼고 API로 변경 (버전 : 1.2.0.2)
```

- 추가할까 생각중인거
```
• ...
```

```
추가할거 추천점
```
"""

setup(name='insta_pkg', 

version='1.2.0.2',

long_description=lo,

long_description_content_type='text/markdown',

description='''Instagram Multiple Package''',

author='WhiteHole',

author_email='wlstn7791@gmail.com',

url='https://github.com/WhiteHole00',

license='MIT', 

py_modules=['insta_package'], 

python_requires='>=3',

install_requires=[], 

packages=['insta_package'] 

)