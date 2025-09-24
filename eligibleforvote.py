age = int (input("enter your age"))
if(age > 12 and  age < 18):
    print("you are tenegeer not eligible for vote")
elif(age < 12 ):
    print("you are  not eligible for vote")
else:
    print(" eligible for vote")