print("Welcome to rollercoster tickets shop!")
height = float(input("What is your height (m)?\n"))
bill = 0
pic = 3
if height >= 1.2:
    age=int(input("Enter your age\n"))
    if age >= 18:
        bill = 7
        #input(f"Adult ticket price is {bill} EUR.\n")
    elif age >= 12:
        bill = 4
        #input(f"Child ticket price is {bill} EUR.\n")
    else:
        print("Sorry, You cannot purchase a rollercoster ticket at the moment. Minimum age to be able to purchase rollercoster tickets is 12 years.")
    wants_pic = (input("Would you like additionally to take a picture on rollercoster for 3 EUR? Type 'Y' for Yes or 'N' for No:\n"))
    
    if wants_pic == "Y":
        #add 3 EUR to the bill
        bill += pic
    print(f"Total amount to pay is: {bill} EUR.")
else:
    print("You can't buy a ticket at the moment. Minimum height to be able to purchase rollercoster tickets is 1.2m.")
