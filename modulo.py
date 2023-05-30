number=int(input("Which number do you want to check"))
number= number%2

if number >= 1:
    print ("Its an odd number")
else:
    print ("its an even number")
    
# Angela Yu solution
if number % 2 == 0:
    print("This is an even number")
else:
    print("Its an odd number")