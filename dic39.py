dic={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
d={}
for i in dic:
    if dic[i]>170:
        d.update({i:dic[i]})
print(d)
        # print(i,dic[i])