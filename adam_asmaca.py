#coding:utf-8
import random
import string
kelimeler=['manisa','elma','armut','izmir','bitcoin','bilgisayar','ekran','monitor']

kelimeler=random.choice(kelimeler)

tahminharf=""
can=10

while can>0:
    hatali_harf=0
    print ("Kelime uzunlugu:",len(kelimeler))
    print ("""IPUCU olarak aciga cikan harfler....""")
    print (kelimeler[0])
    print (kelimeler[3])
    print (kelimeler[1])
    for i in kelimeler:
        if i in tahminharf:
            print(i)
        else:           
            print("_")
            hatali_harf+=1
    if hatali_harf==0:
        print("Tebrikler Kelimeyi Dogru Bildiniz..Dogru Kelime:",kelimeler)
        break
    tahmin=input("Yeni Karakter Girin: ")
    tahminharf+=tahmin
    if tahmin not in kelimeler:
        can -=1
        print ("Hatali Giris yaptiniz",+can,"hakkiniz kaldi.. dikkatli olun.")
        if can==0:
            print ("üzgünüm kaybettiniz :(((( ")