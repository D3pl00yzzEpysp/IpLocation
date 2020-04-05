# -*- coding: utf-8 -*-

"""
Author : D3pl0yzz Epysp
Contato : (82)981690602
Telegram : @NinjaOFC

"""

import os
import requests
import json

os.system("clear")

def IpLocation():
    print("\n")
    ip = input("Digite O Ip : ")
    print("\n")

    req = requests.post("https://iplocation.com/",{"ip":f"{ip}"})

    resposta = req.json()

    data = []

    for x in resposta:
        data.append(f"{x} : {resposta[x]}")

    print("\n".join(data))

while True:
    IpLocation()

