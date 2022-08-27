# dic=[{'x': '10', 'y': '20', 'z': '30'}, {'p': '40', 'q': '50', 'r': '60'}]
# d={}
# for i in dic:
#     for j in i:
#         # print(i[j])
#         d.update({j:int(i[j])})
# print(d)

dic=[{'x': '10.12', 'y': '20.23', 'z': '30'}, {'p': '40.00', 'q': '50.19', 'r': '60.99'}]
# d={}
# for i in dic:
#     for j in i:
#         d.update({j:float(i[j])})
# print(d)

d={}
for i in dic:
    for j in i:
        d.update({j:float(i[j])})
print(d)
