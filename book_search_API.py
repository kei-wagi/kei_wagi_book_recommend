import requests
import random
from linebot import LineBotApi
from linebot.models import TextSendMessage



def make_ISBN():
    a1 = 0
    a2 = 2
    a = str(a1) + str(a2)
    b1 = 2
    b2 = 9
    b3 = 5
    b4 = random.randint(0, 2)
    if b4 == 2:
        b5 = 0
    b5 = random.randint(0, 9)
    b6 = random.randint(0, 9)
    b = str(b1) + str(b2) + str(b3) + str(b4) + str(b5) + str(b6)

    c = 10 - ((40 + (a2 * 3) + (b1 * 1) + (b2 * 3) + (b3 * 1) + (b4 * 3) + (b5 * 1) + (b6 * 3)) % 10)
    if c == 10:
        c = 0

    ISBN = '9784' + a + b + str(c)
    return ISBN


ISBN = make_ISBN()
url = f'https://api.openbd.jp/v1/get?isbn={ISBN}'
book_data = requests.get(url).json()

c = 0

while c != 1:
    try:
        data_name = book_data[0]["onix"]['DescriptiveDetail']['TitleDetail']['TitleElement']['TitleText']['content']
    except TypeError:
        ISBN = make_ISBN()
        url = f'https://api.openbd.jp/v1/get?isbn={ISBN}'
        book_data = requests.get(url).json()
    else:
        c = 1
        


data_URL = "https://www.amazon.co.jp/s?k=" + ISBN



print(data_name)
print(ISBN)

ACCESS_TOKEN = "dgoJZr62Luppa0SIDBF+JFOdRm/ugpwIpDmVfQr/oa3X+XupoBhSx/ic0F/jnHI4K6bkk1Rmk8qYkOb7WAbZkt85G06iJIK9+19H2cltcA7Jveej/V+VcUCT64b+tyCGMoJFlUaM9j5hjjX//tYbSQdB04t89/1O/w1cDnyilFU="
SECRET = "YOUR_CHANNEL_SECRET"


line_bot_api = LineBotApi(ACCESS_TOKEN)

line_bot_api.push_message('Ub1f0ad249ec9b1adc4e51fe1dd6d68fc', TextSendMessage(text='おはようございます！\n今日のおすすめの本はこちらです！！'))
line_bot_api.push_message('Ub1f0ad249ec9b1adc4e51fe1dd6d68fc', TextSendMessage(text= data_name))
line_bot_api.push_message('Ub1f0ad249ec9b1adc4e51fe1dd6d68fc', TextSendMessage(text= data_URL))



