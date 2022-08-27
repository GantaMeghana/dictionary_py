my_dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
b=[]
for i in my_dict:
	# print(i)
	if my_dict[i]>50:
		b.append(my_dict[i])
print(b)

my_dict = {
'a':50, 
'b':58,
'c': 56,
'd':40,
'e':100, 
'f':20
}
b=[]
for i in my_dict:
	# print(i)
	if my_dict[i]>50:
		b.append(i)
print(b)
