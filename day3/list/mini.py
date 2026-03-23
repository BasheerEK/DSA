# create a shopping cart list and: • Add items • Remove items • Display final cart • Count total items
selection = True

Cart_list=[]

while selection:
    print("1. Add Items ")
    print("2. Remove Items ")
    print("3. Display final cart ")
    print("4. Count total items ")
    print("5. Exit ")
    choice=int(input("Select Your Choice  : "))

     
    if choice == 1:
        add=input("Enter the item you need to add : ")
        Cart_list.append(add)
        print("Item added to cart ")
        
    elif choice == 2:
        remov=input("Enter the item you need to remove : ")
        if remov in Cart_list:
            Cart_list.remove(remov)
            print("Item Removed from cart ")
                
        else:
            print("Item not found in cart ")    
        
    elif choice == 3:
        print(Cart_list)    
        
    elif choice == 4:
        print(len(Cart_list))    
        
    elif choice == 5:
        selection = False
    else:
        print("Invalid Selection ")
        
     

