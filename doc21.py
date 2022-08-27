data=[{"V":"S001"},{"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# b=[]
# for i in data:
# # print(i)
#     for j in i:
# 	    if i[j] not in b:
# 	       b.append(i[j])
# print(b)
    
b=[]
for i in data:
	for j in i:
		if i[j] not in b:
			b.append(i[j])
print(b)

