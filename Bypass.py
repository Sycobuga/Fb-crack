#!/usr/bin/python3
import os
try:
    import requests
except ImportError:
    print('\n [✓] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [✓] installing futures !...\n')
    os.system('pip install futures')

try:
    import bs4
except ImportError:
    print('\n [✓] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as sarfrazssb
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;97m' # 
M = '\033[1;31m' # 
H = '\033[1;32m' # 
K = '\x1b[1;97m' # 
B = '\x1b[1;97m' # 
U = '\x1b[1;97m' # 
O = '\x1b[1;97m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)

logo =                                          """   
 \x1b[1;92m╔═══╗╔══╗╔═══╗╔════╗
 \x1b[1;92m╚╗╔╗║╚╣╠╝║╔═╗║╚══╗═║
 \x1b[1;92m─║║║║─║║─║║─║║──╔╝╔╝
 \x1b[1;92m─║║║║─║║─║╚═╝║─╔╝╔╝
 \x1b[1;92m╔╝╚╝║╔╣╠╗║╔═╗║╔╝═╚═╗
 \x1b[1;92m╚═══╝╚══╝╚╝─╚╝╚════╝
\033[1;92m ｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡
\033[1;92m ⇨𝔸𝕌𝕋ℍ𝕆ℝ    : 𝔻𝕀𝔸ℤ ℍ𝔼𝔸𝕃𝕋ℍ
\033[1;32m ⇨𝕎ℍ𝔸𝕋𝕊𝔸ℙℙ  : +𝟞𝟚𝟠𝟟𝟠𝟚𝟟𝟡𝟞𝟠𝟜𝟟𝟠
\033[1;92m ⇨𝔽𝔸ℂ𝔼𝔹𝕆𝕆𝕂  : 𝔸𝕃𝔻𝕀 𝕄𝔸𝕌𝕃𝔸ℕ𝔸
\033[1;92m ⇨𝕊𝕋𝔸𝕋𝕌𝕊    : ℙℝ𝕀𝔹𝔸𝔻𝕀
\033[1;92m ⇨𝕊ℂℝ𝕀ℙ𝕋    : NAKNYUS
\033[1;92m ⇨CRACK     : TANGAL 10 MEI 2022
\033[1;92m ｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡｡""" 

def sarfraz():

    os.system('clear')
    print(logo)
    ipm = requests.get(url_ip).json()
    todz = ''
    IP = ipm['origin']
    print
    print(' [1] BYPASS MK')
    print(' [2] BYPASS AXI')
    print(' [E] EXIT ')
    print('')
    _sonu___ = input(' [✓] CHOOSE : ')
    if _sonu___ in ('1', '01'):
        os.system('rm -rf BYPASS1 && git clone https://github.com/Sycobuga/BYPASS1.git && cd BYPASS1 && python Bypass.py')
    if _sonu___ in ('2', '02'):
        os.system('rm -rf BYPASS1 && git clone https://github.com/Sycobuga/BYPASS1.git && cd BYPASS1 && python Bypass.py')
    if _sonu___ in ('E', 'ee'):
        pass

sonu()
