import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email="teli.khushi@gmail.com"
password="isfxsgyrbhwolrjs"
BUY_PRICE=100
url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"
header= {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"}

response=requests.get(url,headers=header)
# print(response)
soup = BeautifulSoup(response.text, 'lxml')
print(soup.prettify())
price=soup.find(class_="a-offscreen").get_text()
price_without_dollar=price.split("$")[1]
price_as_float = float(price_without_dollar)
print(price_as_float)

title = soup.find(id="productTitle").get_text().strip()
print(title)

if price_as_float < BUY_PRICE:
    message=f"{title} is now {price}"
    with smtplib.SMTP("smtp.gmail.com",port=587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="khushboot2595@gmail.com",
                            msg=f"Subject: Amazon Price Drop\n\n{message}\n{url}".encode('utf-8'))
