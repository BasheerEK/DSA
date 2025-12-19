run=True

while run :
    value = int(input("Choose and enter a value from given option : \n 1.print multiplication table from 1 to 10 \n " \
    "2.print number from 1 to n \n 3.print even numbers between 1 to n \n 4. Exit \n Enter your choice : "))

    #if one is slected
    if value == 1 :
        num1=int(input("Enter a number : "))
        count1=1
        while count1 <= 10:
            print(f"{count1} x {num1} = {count1*num1}")
            count1 = count1 + 1
        print("This is the multiplication table ")

    #if two is slected
    elif value == 2 :   
        n=int(input("Enter a number : "))
        for x in range(1,n+1):
            print(x)
        print("The loop is over")


    #if three is slected
    elif value == 3 : 
        e=int(input("Enter a number : "))
        count=0
        for b in range(1,e):
            if b % 2 != 0: 
               count=count+1 
        print(f"number of even number is : {count}")        
        print("loop finished") 

    #if four is slected
    elif value == 4 : 
        run=False  


    #invalid
    else :
        print("Invalid choice,try again ")

value = int(input("Choose and enter a value from given option : \n 1.print multiplication table from 1 to 10 \n " \
    "2.print number from 1 to n \n 3.print even numbers between 1 to n \n 4. Exit \n Enter your choice : "))        