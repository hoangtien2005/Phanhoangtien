# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 23:00:19 2024

@author: PhanHoangTien 23704241

"""
a= float(input("Nhap canh a:"))
b= float(input("Nhap canh b:"))
c= float(input("Nhap canh c:"))
if a + b >c:
    if a == b == c:
        print("Day la tam giac deu")
    elif a == b or b == c:
        print("Day la tam giac can")
    elif math.isclose(a**2 + b**2, c**2):
        print("Day la tam giac vuong")
    else:
        print("Day la tam giac thuong")
else:
    print("a, b, c khong phai la ba canh cua mot tam giac")
