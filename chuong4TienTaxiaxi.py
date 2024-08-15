# -*- coding: utf-8 -*-
"""
Created on Thu Aug 15 10:00:57 2024

@author: PhanHoangTien 23704241
"""

k = float(input("Nhập độ dài quãng đường đã đi(km):"))
if k <= 1:
    T= 20
    print("So tien phai tra ",T)
elif k <=3:
    T= k *13 
    print("Số tiền phải trả =",T)
elif 4 <= k <= 8:
    T= 3*13+(k-3)*12
    print("Số tiền phải trả =",T)
elif km > 8:
    T= 3*13 + 5*12+(k-8)*10
    print("Số tiền phải trả =", T)
if T > 100:
    T= T*0.9
    print("Số tiền phải trả =",T )

    