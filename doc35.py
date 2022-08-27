dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# c=0
# b=[]
# for i in dict:
#     b.append(dict[i])
#     for j in b:
#         for k in j:
#            c=c+1
# print(c)
c=0
for i in dict:
    # print(dict[i])
    for j in dict[i]:
        c=c+1
print(c)
    