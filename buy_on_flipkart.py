import requests
import re 
import subprocess 
import time

# sudo apt-get install sox
# sudo apt-get install libsox-fmt-mp3


FileName = "/home/next/Downloads/bell-ringing-01.mp3"
http_proxy  = "http://secureon:secure123@192.168.10.1:3128"
https_proxy = "https://secureon:secure123@192.168.10.1:3128"
ftp_proxy   = "ftp://secureon:secure123@192.168.10.1:3128"

proxyDict = {
              "http"  : http_proxy,
              "https" : https_proxy,
              "ftp"   : ftp_proxy
            }


def find_Moto_E3_Plus():

	flipkart_url = 'https://www.flipkart.com/moto-e3-power-black-16-gb/p/itmekgt2fbywqgcv'
	flipkart_fetch = str(requests.get(flipkart_url , proxies=proxyDict).content)
	product = re.findall('This item is currently out of stock',flipkart_fetch)
	if len(product) == 0:
		message = "*******************Your product is back in stock at Flipkart************************"
		subprocess.Popen(['notify-send', "BUYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYYY!!!!!!!!!!!!########"])
		subprocess.call(['play', FileName])
		print(message)
	
	else:
		print ('Your product is not available ')
		

while True:
	find_Moto_E3_Plus()
	time.sleep(20)

