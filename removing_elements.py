CAR_DETAILS={
"brand": "Ford",
"model": "jason",
"year": 1964
}
CAR_DETAILS.pop("model")
print(CAR_DETAILS)


CAR_DETAILS={
"brand": "Ford",
"model": "jason",
"year": 1964
}
CAR_DETAILS.popitem()
print(CAR_DETAILS)

# CAR_DETAILS={
# "brand": "Ford",
# "model": "jason",
# "year": 1964
# }
# del CAR_DETAILS("brand")
# print(CAR_DETAILS)

# person={
# 'name':'jack',
# 'id':22,
# 'place':'dharamsala'
# }

# del person('place')
# print(person)

Dic= {
1: 'NAVGURUKUL',
2: 'IN',  
3:{
'A' : 'WELCOME',
'B' : 'To',
'C' : 'DHARAMSALA'
}
}
Dic.pop(3["A"])
print(Dic)