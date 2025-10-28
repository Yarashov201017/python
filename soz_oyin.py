import random
from sozlar import uzword
# # while True:
# #         ozgaruvchi=random.choice(uzword)
# #         print(ozgaruvchi)
# #         harf=input('taxminiy harf yozing')
# #         ozgaruvchi==harf
# #         print('togri')
# #         break
# # print(uzword)
# royhat=[1,2,3,4,6,5,9,1,0,11,22,-22,-87,55]
# royhatlar=max(royhat[:-1])
# print(royhatlar)


# 1
# def kavadrat_top():
#     son=float(input('son kiriting kvadrat topaman='))
#     print(son**2)
# kavadrat_top()
# 2
# def kub_top():
#     son=float(input('son kiriting kvadrat topaman='))
#     print(son**3)
# kub_top()
# 3
# def faktoriali():
#     import math
#     n=int(input('son='))
#     print(math.factorial(n))
# faktoriali()
# 4
# def juft_tok_top():
#     n=int(input('='))
#     if n%2==0:
#         print('juft')
#     elif n%2==1:
#         print('tok')
#     else:
#         print('xato')
# juft_tok_top()
# 5
# def ildiz_top():
#     import math
#     n=int(input('ildiz topaman'))
#     return math.sqrt(n)
# print(ildiz_top())
# 6
# def katta_son():
#     bir=float(input('son kiriting='))
#     ikki=float(input('son kiriting='))
#     if bir>ikki:
#         print(f'{bir} katta')
#     elif bir<ikki:
#         print(f'{ikki} katta')
#     else:
#         print('ikkisi ham teng')
# katta_son().
# 7
# def orta_qiymat():
#     bir=float(input('son kiriting='))
#     ikki=float(input('son kiriting='))
#     return (bir+ikki)/2
# print(orta_qiymat())
# 8
# def royhat_yig():
#     royhat=[5,6,1,2,3]
#     r=sum(royhat)
#     return r
# print(royhat_yig())
# 9
# def royhat_katta_top():
#     n=int(input('='))
#     royhat=[]
#     for i in range(1,n+1):
#         royhat.append(str(input('son kiriting=')))
#     return max(royhat)
# print(royhat_katta_top())
# 10
# def royhat_kichik_top():
#     n=int(input('='))
#     royhat=[]
#     for i in range(1,n+1):
#         royhat.append(str(input('son kiriting=')))
#     return min(royhat)
# print(royhat_kichik_top())
# 11
# def royhat_():
#     n=int(input('='))
#     royhat=[]
#     for i in range(1,n+1):
#         royhat.append(str(input('son kiriting=')))
#     return len(royhat)
# print(royhat_())
# 12
# def harf_son():
#     matn=input('soz kiriting=')
#     harflar=0
#     for harf in matn:
#         if harf!=" ":
#             harflar+=1
#     return harflar
# print(harf_son())
# 13
# def royhat_katta_top():
#     n=int(input('='))
#     royhat=[]
#     return sorted(royhat , key=len)
# print(royhat_katta_top())
# 14
# def teskari_yoz():
#     royhat=str(input('son kiriting='))
#     return royhat[::-1]
# print(teskari_yoz())
# 15
# def orta_qiymat():
#     n=int(input('='))
#     orta=[]
#     for i in range(1,n+1):
#         orta.append(int(input('son kiriting=')))
#     return sum(orta)/len(orta)
# print(orta_qiymat())
# 16
# def n_gacha():
#     n=int(input('='))
#     yigindi=0
#     for i in range(1,n+1):
#         yigindi+=i
#     return yigindi
# print(n_gacha())
# 17
# def n_gacha_kopaytmasi():
#     n=int(input('='))
#     yigindi=1
#     for i in range(1,n+1):
#         yigindi*=i
#     return yigindi
# print(n_gacha_kopaytmasi())
# 18
# def juft_qaytar():
#     n=int(input('son kiriting='))
#     if n%2==0:
#         return n
#     else:
#         print('xato')
# print(juft_qaytar())
# 19
# def toq_qaytar():
#     n=int(input('son kiriting='))
#     if n%2==1:
#         return n
#     else:
#         print('xato')
# print(toq_qaytar())
# 20
# def nusbat_son(son):
#     nusbatlar=[]
#     for i in son:
#         if i>0:
#             nusbatlar.append(i)
#     return nusbatlar
# print(nusbat_son([2,-9,-4,5,5,3,2,1,7]))
# 21
# def manfiy_son(son):
#     nusbatlar=[]
#     for i in son:
#         if i<0:
#             nusbatlar.append(i)
#     return nusbatlar
# print(manfiy_son([2,-9,-4,5,-6]))
# 22
# def takror_yoqil():
#     royhat=[]
#     n=int(input('='))
#     for i in range(1,n+1):
#         royhat.append(input('soz kiriting='))
#     return set(royhat)
# print(takror_yoqil())
# 23
# def teskari_yoz():
#     royhat=[]
#     n=int(input('='))
#     for i in range(1,n+1):
#         royhat.append(input('soz kiriting='))
#     return royhat[::-1]
# print(teskari_yoz())
# 24
# def tub(son):
#     if son%3!=1 and son%5!=1 and son%7!=1:
#         return son 
#     else: return 'tub emas'
# print(tub(3))
# # 25
# def tub(son):
#     tublar=[]
#     murakkab=[]
#     for n in range(2, son+1):
#         tubmi=True
#         for m in range(2,int(2**0.5)+1):
#             if n%m==0:
#                 tubmi=False
#                 break
#         if tubmi:
#             tublar.append(n)
#         else:
#             murakkab.append(n)
#     return  tublar, murakkab
# print(tub(100))
###
# def boshharf_sana(matn):
#     harf=0
#     for harflar in matn:
#         if harflar.isupper():
#             harf+=1
#     return harf
# print(boshharf_sana("Python"))
# 26
# def ekub_top(a,b):
#     eng_kichik=min(a,b)
#     ekub=[]
#     for i in range(1,eng_kichik+1):
#         if a%i==0 and b%i==0:
#             ekub.append(i)
#     eng_katta=max(ekub)
#     return eng_katta
# print(ekub_top(10,15))
# 27
# def ekub_top(a,b):
#     eng_kichik=min(a,b)
#     ekub=[]
#     for i in range(1,eng_kichik+1):
#         if a%i==0 and b%i==0:
#             ekub.append(i)
#     eng_katta=max(ekub)
#     return a*b/eng_katta
# print(ekub_top(12,15))
# 30
# def katta_harf_qaytar(matn):
#     return matn.upper()
# print(katta_harf_qaytar('salom'))
# 31
# def kichik_harf_qaytar(matn):
    # return matn.lower()
# print(kichik_harf_qaytar('VALI'))
# 32
# def unli_harf(matn):
#     unlilar=["aieouo"]
#     unlisiz=[]
#     for harf in matn:
#         if harf not in  unlilar:
#             unlisiz.append(harf)
#     matnlar="".join(unlisiz)
#     return matnlar
# print(unli_harf("salom"))
# 33
# def undosh_harf(matn):
#     undosh=["qwrtypsdfghjklzxcvbnm"]
#     undoshsiz=[]
#     for harf in matn:
#         if harf not in undosh:
#             undoshsiz.append(harf)
#     matnga="".join(undoshsiz)
#     return matnga
# print(undosh_harf("salom"))
# bosh harfni katta qilish
# def bosh_katta(matn):
#     return matn.title()
# print(bosh_katta('salom'))
# yigindi hisoblash
# def yigindi():
#     s=0
#     n=int(input('='))
#     for i in range(1,n+1):
#         soni=int(input(f'{i}-son'))
#         s+=soni
#     return s
# print(yigindi())
# yiginding darajasi
# def yigindi_daraja(son):
#     string_shakl=str(son)
#     kopaytma=1
#     for i in string_shakl:
#         kopaytma*=int(i)

#     return kopaytma
# print(yigindi_daraja(25))
# palidrom son
# def son_palidrom_tekshir():
#     n=int(input('son kiriting='))
#     m=[]    
#     m.append(n)
#     if m[::-1]==m:
#         return f'{m}-palidrom'
#     else:
#         return f'{m}-palidrom emas'
# print(son_palidrom_tekshir())
# # palidrom ekanini tekshirish
# def matn_palidrom():
#     n=input('matn kirit=').strip()
#     if n[::-1]==n:
#         return f'{n}-palidrom'
#     else:
#         return f'{n}-palidrom emas'
# print(matn_palidrom())
# royhatdagi elemantlar soni
# def royhat_son():
#     return len(uzword)
# print(royhat_son())
# string qilish
# def string_qilish():
#     matn=" ".join(uzword)
#     return matn
# print(string_qilish())
# tartib bilan chiqar
# def tartib_chiqar():
#     royhat=['1','3','2','4','9','5','8','7','0','6']
#     tartib=sorted( royhat)
#     return tartib
# print(tartib_chiqar())
# royhat=[-5,-1,1,3,2,4,9,5,8,7,0,-9,6]
# juft top
# def juft():
#     juftlar=[]
#     for i in range(len(royhat)):
#         if i%2==0:
#             juftlar.append(i)
#     return juftlar
# print(juft())
# manfiy son
# def manfiy_royhat():
#     son=[]
#     n=int(input('='))
#     for i in range(1,n+1):
#         m=int(input(f'{i}-chi'))
#         if m<0:
#             son.append(m)
#     return son
# print(manfiy_royhat())
# daraja top
# def daraja_top():
#     n=float(input('son='))
#     m=n**2
#     return f'{n}**2={m}'
# print(daraja_top())
# teskari so'z 
# def teskari_matn(soz):
#     matn=[]
#     for i in enumerate(soz):
#         matn.insert(0,i)
#     return matn
# print(teskari_matn(uzword))
# KABISA YILI
# def kabisa_yilli_top():
#     n=int(input('yil='))
#     if n%4==0 and n%100!=0 or n%400==0:
#         return f'{n} kabisa yilli'
#     else:
#         return f'{n} kabisa yilli emas'
# print(kabisa_yilli_top())
# print(kabisa_yilli_top())
# kvadrat topish
# def kvadrat_kub():
#     n=int(input('1='))
#     a=int(input('2='))
#     return n**a
# print(kvadrat_kub())
# kub topish
# def kub_top():
#     n=int(input('1='))
#     return n**3
# print(kub_top())
