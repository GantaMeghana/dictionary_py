my_dict = {'C1':[1,2,3],'C2':[5,6,7],'C3':[9,10,11]}
b=[]
for i in my_dict:
    print(i,end="")
    b.append(my_dict[i])
print(b)
# c=[]
i=0
while i<len(b):
    j=0
    while j<len(b[i]):
       sum=b[j][i]
       print(sum,end=" ")
       j=j+1
    print()
    i=i+1


    