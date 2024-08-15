# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 09:26:12 2024

@author: PhanHoangTien 23704241

"""

print (" Giai phuong trinh bac nhat ax+b=0")
a=float(input('a='))
b=float(input('b='))
if a==0 and b==0:
    print("Phuong trinh vo so nghiem")
elif a==0 and b!=0:
    print ("Phuong trinh vo nghiem")
elif a!=0:
    print(-b/a)
else:
    print ("Khong xac dinh")