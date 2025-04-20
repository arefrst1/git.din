my_list=["aref","amir","ali"]
my_list.pop(0)
my_list.append("emad")

# print(my_list)

my_set={"ali","sina","mmd"}
# print (type(my_set))
my_set.add(47)
my_set.pop()     # عدد نمیگیره در ست ها
# my_set.remove("ali")

# print(my_set)

tuple=("fff",45,"ven")
# print (type(tuple))
#چیزی نمیشه بع تاپل ها اضافه کرد
# print(tuple)

me={
     "kod":4211150,
     "name":"aref",
     "last_name":"rostami",
     "age":21,
}
# print(type(me))
# me["kod"]=6082616 #add kardan
me.update({"age":22})
print(me)