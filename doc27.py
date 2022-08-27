a= [{'id': 1, 'success': True, 'name': 'Lary'},
 {'id': 2, 'success': False, 'name': 'Rabi'},
 {'id': 3, 'success': True, 'name': 'Alex'}]
key_name=input("Enter the key :- ")
sum=0
c={}
for i in a:
    sum+=i[key_name]
print(sum)

# for i in student:
# #     if i["id"] not in b:
# #         b["id"]=i["id"]
# #     elif i["id"] in b:
# #         b["id"]=b[i["id"]]+i["id"]
# # print(b)
        

