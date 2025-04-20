

def pass_word(passss):
    if len(passss)  < 8 :
        print("your pass have less than 8 char")
    elif passss.isnumeric():
        print ("your passs shud to be have one letter")    
    elif passss.isalpha():
        print ("your pass shud to be have  one number")
    else :
        print ("yesss")    


while True:
    passss = input("enter your pass_wored: ")
    pass_word(passss)


