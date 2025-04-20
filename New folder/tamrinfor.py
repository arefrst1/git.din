
'''

my_list = ["aref","ali","abas","arian","sina","aria"]

abc =[]

for name in my_list:
    if name[-1]== "a":          # print(name)
      abc.append(name)

print (abc)      


'''
a =["aref","ali","emad","dani","bati"]
b =["aref","sina","dani","emad","reza"]

c =[]

for v in a:
    for x in b:
        if v == x:
            c.append(v)

print (c)            