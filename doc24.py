data=[{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
sum=0
b={}
for i in data:
    if i["item"] not in b:
        b[i["item"]]=i["amount"]
    else:
        b[i["item"]]=b[i["item"]]+i["amount"]
print(b)

        

