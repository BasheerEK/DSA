print("the total mark for each subject is 20 ")
phy=input("Enter the mark in physics : ")
phy=int(phy)
eng=input("Enter the mark in english : ")
eng=int(eng)
math=input("Enter the mark in mathematics : ")
math=int(math)
com=input("Enter the mark in computer : ")
com=int(com)
mal=input("Enter the mark in malayalam : ")
mal=int(mal)

mark=phy+eng+math+com+mal
print("Your total mark is : ",mark)
if mark>=90 :
    print("A grade")
elif mark>=80 :
    print("B grade")
elif mark>=70 :
    print("C grade")   
elif mark>=60 :
    print("D grade")
elif mark>=50 :
    print("E grade")   
else :
    print("Failed")    