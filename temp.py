import var
import requests
import copy
import MetaTrader5 as mt5

home=requests.get(var.login_url)
if home.status_code != requests.codes.ok:
    print("cant load page:{}",home.raise_for_status())
    exit()

cook=home.cookies

headers = {'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
           'keep-alive':'true'}

captcha=requests.get(var.captcha_url)

r=requests.get(url= var.login_url, cookies=cook)




headers = {'user-agent': 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'}

s = requests.Session()
s_cookies=copy.deepcopy(s.cookies)
home = s.get(var.login_url, headers=headers)

s_cookies=s.cookies



s = requests.Session()
s.headers['User-Agent']= 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'


req = requests.Request('GET',  var.login_url)

prepped = s.prepare_request(req)
# do something with prepped.body
prepped.body = 'Seriously, send exactly these bytes.'

# do something with prepped.headers
prepped.headers['user-agent'] = 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0'

resp = s.send(prepped)

print(resp.status_code)


s=requests.session()
s.headers.


from PIL import Image
from io import BytesIO
i = Image.open(BytesIO(captcha.content))
i.save('D:\\New folder\\a.jpeg')



# login
username="mfdonline317882"
password="Asdf@1342mfd$"
capcha="3642"
url='https://onlineplus.mofidonline.com/login'

data={'username':username,
      'password':password,
      'capcha':capcha
}

r=s.post(url=url,data=data)

p_url='https://onlineplus.mofidonline.com/Home/Default/page-1'




a=mt5.AccountInfo
