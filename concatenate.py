# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic4={}
# for i in (dic1,dic2,dic3):
#     dic4.update(i) 
# print(dic4)

# dic={"name":"meghana",'marks':38,"age":20}
# print(dic)
# if "name" in dic:
#     del dic["name"]
#     print(dic)

# dic={"name":45,'marks':38,"age":20}
# for key in sorted(dic):
#     print(key,dic[key])

dic={1:0,2:3,4:2,3:1}
l=[]
c={}
for i in dic:
    l.append(i)
print(l)
for i in range(0,len(l)):
    for j in range(0,len(l)):
        if l[i]<l[j]:
            b=l[i]
            l[i]=l[j]
            l[j]=b
print(l)
for k in range(len(l)):
    for g in dic:
        if dic[g]==l[k]:
            c.update({dic[g]:g})
print(c)



# for i in l:
#     b=l[i+2]
#     if b<l[i]:
#         tem=l[i]
#         l[i]=b
#         b=tem
# print(l)

# # dic={1:4,2:3,4:2,3:1}
# # l=[]
# # max=0
# # for i in dic:
#     l.append(dic[i])
#     for j in range(len(l)):
#         if max<l[j]:
#             max=l[j]
#         # b.update({max:dic[i]})
# print(max) 

