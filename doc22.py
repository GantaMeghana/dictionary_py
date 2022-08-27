# a={'1':['a','b'], '2':['c','d']}
# b=[]
# for i in a:
#     for j in a[i]:
#         for k in j:
#             b.append(k)
# # print(b)
# # l=0
# while l<len(b):
#     m=0
#     while m<len(b):
#         n=0
#         while n<len(b):
#             if l!=j and m!=n and n!=l and  m!=l and l!=n and n!=m:
#                 print(l,m,n)
            

dic = {'1':['a','b'],'2':['c','d']}
b=[]   
for x ,y in dic.values():
    c=(x,y)
    print(c)
    
    

    


