import var
import requests
import copy



from PIL import Image
from io import BytesIO


User_Agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

s = requests.Session()

s.headers['User-Agent']= User_Agent

home = s.get(var.login_url)

# get captcha
captcha=s.get(var.captcha_url)

i = Image.open(BytesIO(captcha.content))
i.save('D:\\New folder\\a.jpeg')


# login
username="mfdonline317882"
password="Asdf@1342mfd$"
capcha=

l_url='https://onlineplus.mofidonline.com/login'

data={'username':username,
      'password':password,
      'capcha':capcha
}

l_r=s.post(url=l_url,data=data)

p_url='https://onlineplus.mofidonline.com/Home/Default/page-1'

p_r=s.get(url=p_url)
