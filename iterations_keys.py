# states_capitals = {
#   'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
#   }
# for state in states_capitals:
#   print(state)

# a={
#     'Gujarat' : 'Gandhinagar',
#   'Maharashtra' : 'Mumbai',
#   'Rajasthan' : 'Jaipur',
#   'Bihar' : 'Patna'
# }
# for i in a:
#     print(a[i])


# states_capitals = {
# 'Gujarat' : 'Gandhinagar',
# 'Maharashtra' : 'Mumbai',
# 'Rajasthan' : 'Jaipur',
# 'Bihar' : 'Patna'
# }
# for state in states_capitals:
#   print(states_capitals[state])


# details ={
# "name":  "Bijender",
# "age":  17,
# "class":  "10th"
# }
# for x,y in details.items():
#   print(x,y)

# details ={
# "name":  "Bijender",
# "age":  17,
# "class":  "10th"
# }
# for x,y in details.items():
#   print(x,y)


# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',  
# 3:{
# 'A':'WELCOME',
# 'B':'To',
# 'C':'DHARAMSALA'
# }
# }
# Dic.pop 3["A"])
# print(Dic)

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5,]
# dictionary=dict(zip(list1,list2))
# print(dictionary)

# dic={
# "ball":"red",
# "bat":4,
# "wickets":8,
# "ball":"green",
# "bat":3
# }
# print(dic)

# dic={
# 'sonu':85,
# 'Kartik':90,
# 'Deepak':96,
# 'Aman':76,
# 'Somesh':60,
# 'Umesh':85,
# 'Amarpal':70,
# 'Roshan':57,
# 'Riyaz':98,
# 'Shabid':56
# }
# print(dic)


# count = {"M":0,"I":0,"S":0,"P":0}
# word = "MISSISSIPPI"
# for i in word:
# 	if i == "M":
# 		count['M'] = count['M']+1
# 	elif i == "I":
# 		count['I'] = count['I']+1
# 	elif i == "S":
# 		count['S'] = count['S']+1
# 	elif i == "P":
# 		count['P'] = count['P']+1
# print (count)

# dict1 =  {
#    'Alex': ['subj1', 'subj2', 'subj3'], 
#    'David': ['subj1', 'subj2']}
# count=0
# for i in dict1:
#     count=count+dict1[i]
# print(count)


# a=int(input("enter a numebr"))
# d=dict()
# for i in range(1,a+1):
#     d[i]=i*i
# print(d)

# fruit = {}
# def addone(index):
#   if index in fruit:
#     fruit[index]+=1
#   else:
#     fruit[index]=1
# addone('Apple')
# addone('Banana')
# addone('apple')
# addone('Apple')
# print(len(fruit))
# print(fruit)

# box = {}
# jars = {}
# crates = {}
# box['biscuit'] = 1
# box['cake'] = 3
# jars['jam'] = 4
# crates['box'] = box
# crates['jars'] = jars
# print(len([crates]))

# rec = {
# "Name" : "Python", 
# "Age":"20",
# "Addr" : "NJ", 
# "Country" :"USA"
# }
# id1 = id(rec)
# del rec

# rec = {
# "Name" : "Python", 
# "Age":"20", 
# "Addr" : "NJ", 
# "Country" : "USA"
# }
# id2 = id(rec)
# print(id1 == id2)

# details={
# "name":"Shanti",
# "age":12,
# "email":"shanti@navgurukul.org",
# }
# details["last name"]='G'
# # print(details)
# print(details["name"])
# print(details["last name"])
# print(details["age"])

# dict1={1:2,2:3,3:4,4:5}
# sum=0
# for i in dict1:
#     sum=sum+dict1[i]
# print(sum)
# a=int(input())
# c=dict()
# for i in range(1,16):
#    c[i]=i*i
# print(c)

# s={'umesh':21,'bijender':54,'amar':67,'peter':89,'sonu':56}
# a={'python':20,"gaurav":300,'dev':34,"karan":43}
# c={}
# for i in (s,a):
#    c.update(i)
# print(c)

# d ={
# "fantasy": "harrypotter",
# "romance": "me before you",
# "fiction": "divergent"
# }
 
# for i in d.iteritems():
     
#     # prints the items
#     print(i)

# dict={1:"a",2:"b",3:"c",5:"d",2:"b"}
# z={}
# for key,value in dict.items():
#     if key not in z.keys():
#         z[key]=value
# print(z)

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3 = {}
# for i, j in d1.items():
#   for x, y in d2.items():
#     if i == x:
#         d3[i]=(j+y)
# print(d3)

# list1=["one","two","three","four","five"]
# list2=[1,2,3,4,5]
# dic={}
# i=0
# while i<len(list1):
# 	dic.update({list1[i]:list2[i]})
# 	i=i+1
# print(dic)

# Dic= {
# 1: 'NAVGURUKUL',
# 2: 'IN',  
# 3:{
# 'A' : 'WELCOME',
# 'B' : 'To',
# 'C' : 'DHARAMSALA'
# }
# }
# del Dic[3]["A"]
# print(Dic)

# a=[
# {"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}
# ]
# dic={}
# i=0
# while i<len(a):
# 	j=0
# 	while j<len(a[i]):
# 		if a[i][j] in dic:
# 			dic.update(a[i][j])
# 	i=i+1
# print(dic)

# dic={
# 'sonu':85,
# 'Kartik':90,
# 'Deepak':96,
# 'Aman':76,
# 'Somesh':60,
# 'Umesh':85,
# 'Amarpal':70,
# 'Roshan':57,
# 'Riyaz':98,
# 'Shabid':56
# }
# s={}
# i=0
# while i<len(dic):
# 	s.update(dic)
# 	i=i+1
# print(s)

# a="mississipi"
# b={}
# i=0
# while(i<len(a)):
# 	j=0
# 	c=0
# 	while (j<len(a)):
# 		if a[i]==a[j]:
# 			c=c+1
# 		j=j+i
# 	b.update({a[i]:c})
# 	i=i+1
# print(b)

# a=[
# {"first":"1"}, 
# {"second": "2"}, 
# {"third": "1"}, 
# {"four": "5"}, 
# {"five":"5"}, 
# {"six":"9"},
# {"seven":"7"}
# ]
# b=[]
# for i in a:
# 	# print(i)
# 	for j in i:
# 		# if i[j] not in b:
#         #     b.update(i[j])
# 		# print(i[j])
# 		if i[j] not in b:
# 			b.append(i[j])
# print(b)



# # # 	for j in i:
# # 		if a[i][j] not in b:
# # 			b.append()
# # print(b) 



# # my_dict = {'a':50, 'b':58,'c':56,'d':40, 'e':100,'f':20}
# # b=[]
# # for i in my_dict:
# # 	if my_dict[i]>50:
# # 		b.append(my_dict[i])
# print(b)

# my_dict = {
# 'a':50, 
# 'b':58,
# 'c': 56,
# 'd':40,
# 'e':100, 
# 'f':20
# }
# b=[]
# for i in my_dict:
# 	print(i)
# 	if my_dict[i]>50:
# 		b.append(i)
# print(b)

# i=1
# d={}
# while i<3:
#     name=input("enter name")
#     marks=int(input("enter a number"))
#     d[name]=marks
#     i=i+1
# print(d)

