# -*- coding: utf-8 -*-

"""
Author : D3pl0yzz Epysp
Telegram : @ImTheNinja

"""

import os
import requests
import json

os.system("clear")



vezes = 1

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
  
  de = int(input("[1] - Sim\n[2] - Não\nDeseja Consultar Outro Ip ? : "))
  
  if de == 1:
    
    vezes = 1 
    
  else:
    
    vezes = 2

while vezes == 1:
  
  IpLocation()

