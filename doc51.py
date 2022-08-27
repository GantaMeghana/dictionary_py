# dic={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# d={}
# for i in dic:
#     b=[]
#     for j in dic[i]:
#         if j%2==0:
#             b.append(j)
#             d.update({i:b})
# print(d)
            
dic={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
d={}
for i in dic:
    b=[]
    for j in dic[i]:
        if j%2==0:
            b.append(j)
            d.update({i:b})
print(d)


