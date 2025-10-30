# def sonni_teskarilash(son):
#     if son < 10 :
#         return son
#     else :
#         return son%10 + sonni_teskarilash(son//10)

# print(sonni_teskarilash(100))

# Lambda

# son = lambda a: a%2 == 0 
# print(son(10))
# fakrotilal
# import math
# def fakrotilal(n):
#     if n==0:
#         return n
#     else:
#         i=math.factorial(n)
#     return i
# print(fakrotilal(5))
# fibonchi son
# def fibonchi_son(n):
#     if n==1 or n==2:
#         return n
#     else:
#         return fibonchi_son(n-1) + fibonchi_son(n-2)
# print(fibonchi_son())
# yig'indi hisobla
# def yigindi(son):
#     if son < 10 :
#         return son
#     else :
#         return son%10 + yigindi(son//10)
# print(yigindi(123))
# oxirgi raqam olish
# def oxirgi_raqam(son):
#     if son<10:
#         return son
#     else:
#         return son%10
# print(oxirgi_raqam(19))
# raqam soni
# def raqam_soni(son):
#     if son<1 or son==0:
#         return son
#     else:
#         return 1+ raqam_soni(son//10)
# raqamla soni
# def raqam_soni(son):
#     if son==0:
#         return 0
#     else:
#         return 1+ raqam_soni(son//10)
# print(raqam_soni(16))
# teskarilash
# def teskari(matn):
#     if len(matn)==0:
#         return " "
#     else:
#         return matn[-1]+teskari(matn[:-1])
# print(teskari("salom"))
# royhat yigindisi
# def royhat_yigindisi(royhat):
#     if len(royhat)==0:
#         return 0
#     else:
#         return royhat[0]+royhat_yigindisi(royhat[1:])
# print(royhat_yigindisi([10,10,10,10]))
# Maksimum topish
# def royhat_max(royhat):
#     if len(royhat)==0:
#         return 0
#     else:
#         eng_katta=royhat_max(royhat[1:])
#         if royhat[0]> eng_katta:
#             return royhat[0]
#         else:
#             return eng_katta
# print(royhat_max([80,10,20,30,40,50]))