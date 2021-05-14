#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

os.system("apt-get install figlet")
os.system("clear")
os.system("figlet Mac Adres Degistir ")
print("-"*50)
print("Mac Adres Değiştirme Aracına Hoşgeldin instagram = zumrudu_anka_team")
print("Bu Araç Treangle Tarafından Oluşturulmuştur")
print("-"*50)
print("""
1) MAC Adresi Random Belirle
2) Mac Adresi Elle Belirle
3) Mac Adresi Orjinal Hale Döndür
""")
islemno = input("İşlem No Girin : ")
if(islemno=="1"):
    os.system("ifconfig eth0 down")
    os.system("macchanger -r eth0")
    os.system("ifconfig eth up")
    print("\033[92mYeni MAC Adresi Random Belirlendi...")

if(islemno=="2"):
    macadres = input("Yeni Mac Adresi Girin : ")
    os.system("ifconfig eth0 down")
    os.system("macchanger --mac " + macadres + "eth0")
    os.system("ifconfig eth up")
    print("\033[92mYeni MAC Adresiniz Belirlendi...")

if(islemno=="3"):
    os.system("ifconfig eth0 down")
    os.system("macchanger _p eth0")
    os.system("ifconfig eth0 up")
    print("\033[92mYeni MAC Adresiniz Orjinal Hale Döndürüldü...")

else:
    print("Hatal İşlem Yaptınız Program Yeniden Çalıştırılıyor ...")
    os.system("python MAC.Adres.Değiştirme.py")







