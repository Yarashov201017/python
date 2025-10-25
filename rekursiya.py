# def sonni_teskarilash(son):
#     if son < 10 :
#         return son
#     else :
#         return son%10 + sonni_teskarilash(son//10)

# print(sonni_teskarilash(132))

# Lambda

son = lambda a: a%2 == 0 
print(son(10))