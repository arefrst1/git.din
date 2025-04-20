
# def abuteme(age , lastname):
#     print (f"{age} 21 years old")
#     print (f"{lastname} rostami ")


# abuteme ("aref","aref")


# def a (*name):
#     print(f"heloo {name}")


# a ("aref","erfan","emad")    





# def aj (nam ,khan ,*args ,**kwargs):
#     print(nam)
#     print(khan)
#     print(args)
#     print (kwargs)

# aj ('aref','rostami','ava', age=21 , team = "ajkj")  


# def heloo (n):
#     for item in n:
#         print (f"heloo {item}")

# heloo (["aref","efo","emad"])


# def abn(a,b):
#     c = a+b
#     return c
# print (abn(10,17))

username = input ("enter your user name : ")

def key (username):
     if len (username) > 10:
        return False
     else:
         return True 
     
if key(username):
    print ("your use is ok ")
else:
    print ("ridi dashi ")