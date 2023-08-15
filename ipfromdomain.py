#use ; python file.py
import sys
import socket
import time
import random
import colorama
from multiprocessing.dummy import Pool as ThreadPool

colorama.init()

def getIP(site):
    site = site.strip()
    try:
        if 'http://' not in site:
            IP1 = socket.gethostbyname(site)
            print("IP: " + IP1)
            with open('ips2.txt', 'a') as file:
                file.write(IP1 + '\n')
        elif 'http://' in site:
            url = site.replace('http://', '').replace('https://', '').replace('/', '')
            IP2 = socket.gethostbyname(url)
            print("IP: " + IP2)
            with open('ips2.txt', 'a') as file:
                file.write(IP2 + '\n')

    except:
        pass

nam = input('Domain List name: ')
with open(nam) as f:
    domains = f.readlines()

pool = ThreadPool(100)

results = pool.map(getIP, domains)
pool.close()
pool.join() 