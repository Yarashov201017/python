# # class Word:
# #     def __init__(self,fayl_nomi):
# #         self.fayl=fayl_nomi
# #     def asosoi_bolim(self):
# #         return f"Siz asosiy bo'limdasiz"
# #     def joylashgan_kirish(self):
# #         return "siz joylash bo'limidasiz"
# #     def dizaynga_kirish(self):
# #         return "siz dizayn bo'limidasiz"
# #     def get_file(self):
# #         return f" Siz yaratgan word fayl nomi {self.fayl}"
    
# # fayl1=Word("Meros")
# # print(fayl1.dizaynga_kirish())

# # class Hayvon:
# #     def __init__(self, nomi):
# #         self.nomi = nomi

# #     def tovush_chiqar(self):
# #         print(f"{self.nomi} tovush chiqarmoqda")

# # class It(Hayvon):
# #     def tovush_chiqar(self):
# #         print(f"{self.nomi}: vov-vov!")
# import datetime as dt
# # class Mushuk(Hayvon):
# #     def tovush_chiqar(self):
# #         print(f"{self.nomi}: Miyov!")

# # it = It("itlar")
# # mushuk = Mushuk("Mushuklar")

# # it.tovush_chiqar()
# # mushuk.tovush_chiqar()

# # class Talabe:
# #     def __init__(self,ism,yil,yonalish,universitet):
# #         self.ismi=ism
# #         self.yili=yil
# #         self.yonalishi=yonalish
# #         self.unversisteti=universitet
        
# #     def get_name(self):
# #         return f"Talaba : {self.ismi}"
# #     def get_age(self):
# #         return f"Talaba yoshi {2025-self.yili}"
# #     def get_yonalish(self):
# #         return f"Talaba {self.unversisteti} ning {self.yonalishi} "
# #     def get_info(self):
# #         return f"TAlaba :{self.ismi}\n talaba yili : {2025-self.yili} \n Talaba universisteti :{self.unversisteti} ning {self.yonalishi}"
# # talaba1 = Talabe("Ulug'bek",2010,"Dasturlash","TATU")
# # print(talaba1.get_info())
# # from datetime import datetime
# # class Student:
# #     def __init__(self,ismi,yoshi,baho,hozir):
# #         self.ism=ismi
# #         self.yosh=yoshi
# #         self.bahosi=baho
# #         # self.hozir_date = dt.datetime.now()
# #         self.hozir = hozir
        
# #     def get_ism(self):
# #         return f"student :{self.ism}"
# #     def get_yosh(self):
# #         return f"student : {int(self.hozir)-self.yosh}"
# #     def get_bahosi(self):
# #         return f"student : {self.bahosi}"
# #     def get_info(self):
# #         return f"student :{self.ism} \n student : {self.yosh} \n student : {self.bahosi}"
# # hozir = datem = datetime.today().strftime("%Y")
# # student1=Student("Ulug'bek",2010,5,hozir)
# # print(student1.get_yosh())

# # class Avto:
# #     def __init__(self,nomi,yili,rangi,yurgani):
# #         self.nomi=nomi
# #         self.yil=yili
# #         self.rang=rangi
# #         self.yurgan=yurgani
# #     def get_nom():
# #         return f"Avto mobil nomi: {nomi}"
# #     def get_yil():
# #         return f"Avto mobil yili:{yili}"
# #     def get_rang():
# #         return f"Avto mobil rangi:{rangi}"
# #     def get_yurgani():
# #         return f"Avto mobil yurgani:{yurgani} km"
# #     def get_info():
# #         return f"Avto mobil nomi: {nomi}\n Avto mobil yili:{yili} \n Avto mobil rangi:{rangi} \n Avto mobil yurgani:{yurgani} km"
# # Avtobek=Avto("nexia",2000,'oq',1700,'km')
# # print(Avtobek.get_info())

 
# class Bank:
#     def __init__(self,balans,pul_qosh,pul_ayir):
#         self.balansi=balans
#         self.pulqosh=pul_qosh
#         self.pulayirish=pul_ayir
#     def get_mablag(self):
#         return f" bor mablag'ingiz {balans}"
# 3 Bank kartasi
# class Bank:
#     def __init__(self, balans=0):
#         self.balans = balans
#     def pul_qoshish(self, miqdor):
#         if miqdor > 0:
#             self.balans += miqdor
#             print(f"{miqdor} doll qo'shildi. Yangi balans: {self.balans} doll")
#         else:
#             print("Musbat bo'lishi kerak!")
#     def pul_yechish(self, miqdor):
#         if miqdor <= 0:
#             print("musbat bo'lishi kerak!")
#         elif miqdor > self.balans:
#             print("hiobda pul yoq!")
#         else:
#             self.balans -= miqdor
#             print(f"{miqdor} doll yechildi. Yangi balans: {self.balans} doll")
# hisob = Bank(10000)
# hisob.pul_qoshish(15001)
# hisob.pul_yechish(1)
# # # 4
# # # class Dokon:
# # #     def _init__(self, dokon_nomi):
# # #         self.dokon = dokon_nomi
# # #         self.mahsulot = []
# # #         self.mahsulot_soni = 0
# # #     def add_product(self, mahsulot_nomi):
# # #         self.mahsulot.append(mahsulot_nomi) 
# # #         self.mahsulot_soni +=1
# # #     def delete_product(self,product_name): 
# # #         self.mahsulot.remove(product_name)
# # #         self.mahsulot_soni -=1
# # #     def get_info(self): 
# # #         matn = "\n".join([name for name in self.mahsulot]) 
# # #         return f"{self.dokon} da {self.mahsulot_soni}"
        
# # # xalimaxon  = Dokon ("Xalimahon")
# # # xalimaxon.add_product("Non")
# # # xalimaxon.add_product("Shakar")
# # # xalimaxon.add_product("Tuz")
# # # xalimaxon.add_product("Qatiq")
# # # magnit = Dokon("Magnit")
# # # magnit.add_product("Olma")
# # # magnit.add_product("Uzum")
# # # magnit.add_product("Anor")
# # # xalimaxon.delete_product("Non")
# # # magnit.delete_product("Uzum")
# # # print(xalimaxon.get_info(), magnit.get_info()) 
 

# #  class Mashina :
# #     def __init__(self , model , tezlik , hudut):
# #         self.model = model 
# #         self.tezlik = tezlik
# #         self.hudut = hudut


# #     def decrease_speed(self , car_speed , hududlar):
# #         hududlar = ['Shahar' , 'aholi_yoq' , 'trassa']
# #         car_speed = [60 , 90 , 150]
# #         if self.hudut == hududlar[0] :

# #             if self.tezlik > car_speed[0] :
# #                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[0]} km/h ga kamaytiring"
            
# #             return 'siz tog\'ri harakat qilayapsiz'
        
# #         elif self.hudut == hududlar[1] :

# #             if self.tezlik > car_speed[1] :
# #                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[1]} km/h ga kamaytiring"
            
# #             return 'siz tog\'ri harakat qilayapsiz'
        
# #         elif self.hudut == hududlar[2] :

# #             if self.tezlik > car_speed[2] :
# #                 return f"{self.model} Haydovchisi tealigingizni {self.tezlik - car_speed[0]} km/h ga kamaytiring"
            
# #             return 'siz tog\'ri harakat qilayapsiz'
    
# #     def increase_speed(self , car_speed , drive_road):
# #         drive_road = ['Shahar' , 'aholi_yoq' , 'trassa']
# #         car_speed = [60 , 90 , 150]
# #         if self.hudut == drive_road[0] :

# #             if self.tezlik > car_speed[0] :
# #                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[0]} km/h gacha oshirishingiz mumkin"
            
# #         if self.hudut == drive_road[1] :

# #             if self.tezlik > car_speed[1] :
# #                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[1]} km/h gacha oshirishingiz mumkin"
            
# #         if self.hudut == drive_road[2] :

# #             if self.tezlik > car_speed[2] :
# #                 return f"{self.model} mashinasi haydovchisi siz tezligingizni {self.tezlik - car_speed[2]} km/h gacha oshirishingiz mumkin"
# 7
# class Telefon:
#     def __init__(self,brend,bateriya,nomi):
#         self.brend=brend
#         self.bateriya=bateriya
#         self.name=nomi
#     def nom_telefon(self):
#         return f" telefon nomi{self.name}"
#     def phone_info(self):
#         return f" telefon nomi {self.name} \n telefon brendi {self.brend} \n telefon zayredi {self.bateriya}%"
# myphone=Telefon('Samsung',99,'Samsung A06')
# print(myphone.phone_info())
# 8
# class Teacher():
#     def __init__(self,teacher_name,fan,tajriba):
#         self.nomi=teacher_name
#         self.fan=fan
#         self.tajriba=tajriba
#     def get_name(self):
#         return f" Oqituvchi FIO {self.nomi}"
#     def science(self):
#         return f"{self.nomi} Oqituvchi  quyidagi fandan dars beradi {self.fan}"
#     def experience(self):
#         return f"{self.nomi} Oqituvchi tajribasi {self.tajriba}"
#     def teacher_info(self):
#         return f"Oqituvchi FIO {self.nomi} \n{self.fan} kursidan dars beradi \ntajribasi {self.tajriba} yillik"
# myteacher=Teacher("Xusainov Mirzabek","IT",7)
# print(myteacher.teacher_info())
# 9
# class Kompyuter():
#     def __init__(self,ram,hdd,cpu):
#             self.RAM=ram
#             self.HDD=hdd
#             self.CPU=cpu
            
#     def kompyuter_ram(self):
#         return f"kompyuter Rami {self.RAM}"
#     def kompyuter_HDD(self):
#         return f"kompyuter HDD {self.HDD}"
#     def kompyuter_HDD(self):
#         return f"kompyuter CPU {self.CPU}"
#     def info_kompyuter(self):
#         return f"kompyuter Rami {self.RAM}\nkompyuter HDD {self.HDD}\nkompyuter CPU {self.CPU}"
# kampyuter1=Kompyuter(16,"256gb","Inter core 7 Ultra")
# print(kampyuter1.info_kompyuter())
# 10
# class Sinf_student():
#     def __init__(self):
#         self.royhat=[] 
#         self.sudent_soni=0
#     def oquvchilar(self,oquchi):
#         self.royhat.append(oquchi)
#         self.sudent_soni+=1
#     def oquvchilar_haqda(self):
#         royhatt="Sinf o'quvchilari:\n"
#         for index,oquvchi in enumerate(self.royhat,1):
#             royhatt+=f"\n {index}: {oquvchi}"
#         return f"Oquvhilar nomi{royhatt}\n {self.sudent_soni} ta Oquvchilar bor"
# oquchilar=Sinf_student()
# oquchilar.oquvchilar('Valijon')
# oquchilar.oquvchilar("Ulug'bek")
# oquchilar.oquvchilar("Yoqubboy")
# print(oquchilar.oquvchilar)
# 11
# class SHaxslar:
#     def __init__(self,ism,yosh,yashash_joyi,qayerda_ishlashi,habaryubor, telefon_raqam):
#         self.ism=ism
#         self.yosh=yosh
#         self.uyi=yashash_joyi
#         self.work=qayerda_ishlashi
#         self.habar=habaryubor
#         self.tel=telefon_raqam
#     def oddiy_info(self):
#         return f"Shaxsning ismi {self.ism} \n  Shaxs yoshi {self.yosh} \n Shaxsning mobil telefon nomeri {self.tel}"
#     def ish_va_uy(self):
#         return f"Shaxsnig yashash joyi {self.uyi} \n Shaxsning ish:{self.work}"
#     def message(self):
#         return f"Shaxsga habar {self.habar}"
#     def barcha_malumot(self):
#         return f"Shaxsning ismi {self.ism}\nShaxs yoshi {self.yosh}\nShaxsning mobil telefon nomeri {self.tel}\nShaxsnig yashash joyi {self.uyi}\nShaxsning ishi: {self.work}"
# shaxslar=SHaxslar("Valijon",15,"Tuproqqal'a","Yo'q","Salom",955555555)
# print(shaxslar.barcha_malumot())
# 12

# # 14
# class Kutubxona:
#     def __init__(self,kutubxona):
#         self.nomi=kutubxona
#         self.kitoblar=[]
#         self.kitoblar_soni=0
#     def book_add(self,kitob):
#         self.kitoblar.append(kitob)
#         self.kitoblar_soni+=1
#     def show_librarly(self):
#         royhat="Kitoblar:\n"
#         for index,kitob in enumerate(self.kitoblar,1):
#             royhat+=f"\n{index}) {kitob}"
#         return f"{self.nomi} kitobxonasi {self.kitoblar_soni} ta kitob bor:\n{royhat}"
