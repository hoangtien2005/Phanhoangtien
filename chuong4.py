# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 18:24:27 2024

@author: PhanHoangTien 23704241
"""

import random 
luachon = ("kéo","búa","bao")
nguoichoi = input("lựa chọn(kéo-búa-bao):")
may = random.choice(luachon)
print(f"banchon: {nguoichoi}:")
print(f"may chon: {may}:")
if nguoichoi == may:
    print("hoa")
elif may == "bua" and nguoichoi == "keo" or\
     may == "bao" and nguoichoi == "bua" or\
     may == "keo" and nguoichoi == "bao":
           print("may thang")
else:
    print("may thua")