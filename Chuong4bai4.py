# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 22:36:06 2024

@author: PhanHoangTien 23704241
"""

a= float(input("Nhap canh a: "))
b= float(input("Nhap canh b: "))
c= float(input("Nhap canh c: "))
if a + b > c and a + c > b and b + c > a:
    print("a, b, c la ba canh cua mot tam giac.")
else:
    print("a, b, c khong phai la ba canh cua mot tam giac.")