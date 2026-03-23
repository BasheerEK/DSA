# Write a recursive function to print numbers from n down to 1.

def rev(n):
    if n == 1:
        return 1 
    else :
        print(n)
        return rev(n-1)
    
print(rev(10))    