# dic={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
# b={}
# for i in dic:
#     for j in (dic[i]):
#         b.update({dic[i]:len(dic[i])})
# print(b)

dic={'1': 'Austin Little', '2': 'Natasha Howard', '3': 'Alfred Mullins', '4': 'Jamie Rowe'}
b={}
for i in dic:
    for j in dic[i]:
        b.update({dic[i]:len(dic[i])})
print(b)
