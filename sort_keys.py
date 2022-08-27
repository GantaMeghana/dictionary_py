# dict={'a':6,'b':2,"c":3}
# mul=1
# for  i in dict:
#     mul=mul*dict[i]
# print(mul)



# k=[1,2,3,4,5,6]
# v=[11,22,33,44,55]
# b={}
# for i in k:
#     for j in v:
#         b.update({v[j]:i})
# print(b)

# a=[3,2,6,0,1,2]
# for i in range(0,len(a)):
#     for j in range(0,len(a)):
#         if a[i]<a[j]:
#             b=a[i]
#             a[i]=a[j]
#             a[j]=b
# print(a)

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
