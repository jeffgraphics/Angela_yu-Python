age = int(input("what is your current age"))
age_left = int(100 - age)
days = int(365.25*age_left)
weeks = int(52.14*age_left)
months = int(12*age_left)

#this was my print solution which still works but Angela's solution is neater and i learnt how to concatenate more easily
#print ("You have "+ str(days)+"days, "+ str(weeks)+"weeks, and "+ str(months)+"months left.")

message = f"you have {days}days, {weeks}weeks, and {months}months left"

print(message)