# 11
# def ismlar():
#     ism=input('ism kiriting=').strip()
#     return f"Salom,<{ism}>!"
# print(ismlar())
# 12
# def kvadrat_qaytar():
#     n=float(input('kvadrat kotaraman='))
#     return n**2
# print(kvadrat_qaytar())
# 13
# def katta_son():
#     bir=float(input('1-son kiriting='))
#     ikki=float(input('2-son kiriting='))
#     return max(bir,ikki)
# print(katta_son())
# 14
# def sonalr_yigindisi():
#     royhat=[]
#     n=int(input('='))
#     for i in range(1,n+1):
#         royhat.append(float(input(f"{i}-son kiritng")))
#     return sum(royhat)
# print(sonalr_yigindisi())
# 15
# def unli_harf():
#     matn=input('soz kiriting=')
#     royhat=[]
#     royhat.append(matn)
#     son=0
#     for i in range(len(matn)):
#         if matn[i]=='a' or matn[i]=='e' or matn[i]=='u' or matn[i]=='i' or matn[i]=='o' or matn[i]=="'":
#             son+=1
#     return son
# print(unli_harf(),'unli bor')
# 16
# vali=20
# def ishlatish():
#     global vali
#     vali
# # 17
# x=lambda son: son**3
# print(x(3))
# 18
# def eng_kichik():
#     m=float(input('1='))
#     n=float(input('2='))
#     a=float(input('3='))
#     return min(m,n,a)
# print(eng_kichik())
# 19
# def sonlarni_olibtashla():
#     m=input('matn kiriting=')
#     royhat=[]
#     nm=[]
#     for i in range(len(m)):
#         if m[i]=='0' or m[i]=='1'  or m[i]=='2' or m[i]=='3' or m[i]=='4' or m[i]=='5' or m[i]=='6' or m[i]=='7' or m[i]=='8' or m[i]=='9':
#             royhat.append(m[i])
#         else:
#             nm.append(m[i])
#     return nm
# print(sonlarni_olibtashla())
# 20
# def kuchli_kuchsiz_parol(parol):
#     if len(parol)>=8:
#         return f'<{parol}> kuchli'
#     else: return f" <{parol}> kuchsiz"
# print(kuchli_kuchsiz_parol('123456789')) 
# https://github.com/Yarashov201017/python.git