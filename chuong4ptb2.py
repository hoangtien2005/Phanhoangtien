# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:10:00 2024

@author: PhanHoangTien 23704241
"""

print('Giai phuong trinh bac a*(x)**2+b*x+c=0')
a=float(input('a='))
b=float(input('b='))
c=float(input('c='))
if a==0:
    print('Phuong trinh khong phai phuong trinh bac hai')
elif a!=0:
    delta = b**2 - 4*a*c
    if delta<0:
       print('Phuong trinh co nghiem')
    elif delta==0:
        x=-b/(2*a)
        print('Phuong trinh co nghiem kep x=x1=x2',x)
    elif delta>0:
       x1 = (-b+delta**(1/2))/(2*a)  
       x2 = (-b-delta**(1/2))/(2*a)
       print('Phuong trinh co hai nghiem')
       print('x1',x1)
       print('x2',x2)
else:
    print('Khong xac dinh')