import urllib.request as url
import bs4
'''
for installing bs4 and lxml,
1-go to cmd(command prompt)
2-type pip3.9 install bs4/lxml
'''
path='https://www.amazon.in/ASUS-i7-10750H-Graphics-Original-G712LU-H7015T/dp/B08DVLCNKK/ref=sr_1_3?crid=3VWZCHW3ID4Z6&dchild=1&keywords=asus+rog+laptops&qid=1610511795&sprefix=asus+rog%2Caps%2C400&sr=8-3'
response=url.urlopen(path)
data=bs4.BeautifulSoup(response,'lxml')
product_title = data.find('span',id="productTitle")
print("Item Name : ",product_title.text.replace("\n",""))
