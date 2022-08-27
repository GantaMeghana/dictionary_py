# number={}
# def addone(i):
#     if i in number:
#         number[i]+=1
#     else:
#         number[i]=1
# addone("1")
# addone("2")
# addone("3")
# print(len(number))
# print(number)

# Student = {}
# Age = {}
# Details = {}
# Student['name'] = "bikki"
# Age['student_age'] = 14
# Details['Student'] = Student
# Details['Age'] = Age
# print(len(Details["Student"])) 

my_dict = {}
my_dict[(1,2,4)] = 8
my_dict[(4,2,1)] = 10
my_dict[(1,2)] = 12

sum = 0
for k in my_dict:
  sum += my_dict[k]

print(sum)
print(my_dict)
